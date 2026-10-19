"""Check that the German translations are complete and up to date.

Every translated file starts with a header that names its English source and the
SHA-256 hash of the source at the time of translation:

    <!-- translation-of: README.md | source-sha256: <first 16 hex characters> -->

Checks:
  * the English source has not changed since the translation was last updated
  * all version numbers in the translation match the VERSION file
  * the German questionnaire contains exactly the control IDs and [KO] markers of the checklist
  * Swiss orthography: no "ß"

Usage (from the repository root):

    python3 tools/check-translations.py                    # check all translations
    python3 tools/check-translations.py --stamp README.de.md  # record the current source hash

Use --stamp only after the translation has been updated to match the English source.
"""
import argparse
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HEADER = re.compile(r"^<!-- translation-of: (?P<source>\S+) \| source-sha256: (?P<hash>\S+) -->$")
VERSION_PATTERN = re.compile(r"(?:ACP%20|ACP |Version )(\d+\.\d+(?:\.\d+)?)")
CHECKLIST = ROOT / "assessment" / "assessment-checklist.md"
QUESTIONNAIRE_DE = ROOT / "assessment" / "assessment-questionnaire.de.md"


def source_hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def translations():
    return sorted(p for p in ROOT.rglob("*.de.md") if ".git" not in p.parts)


def read_header(path):
    first_line = path.read_text(encoding="utf-8").splitlines()[0]
    match = HEADER.match(first_line)
    if not match:
        return None
    return ROOT / match["source"], match["hash"]


def controls(text, pattern):
    found = {}
    for control_id, rest in re.findall(pattern, text, re.M):
        found[control_id] = "[KO]" in rest
    return found


def check_questionnaire():
    expected = controls(CHECKLIST.read_text(encoding="utf-8"), r"^(\d+\.\d+) (.+)$")
    actual = controls(QUESTIONNAIRE_DE.read_text(encoding="utf-8"), r"^\| (\d+\.\d+) +\| (.+?) \|")
    problems = []
    if missing := sorted(set(expected) - set(actual), key=lambda c: [int(x) for x in c.split(".")]):
        problems.append(f"missing controls: {', '.join(missing)}")
    if extra := sorted(set(actual) - set(expected)):
        problems.append(f"controls not in checklist: {', '.join(extra)}")
    if ko := sorted(c for c in expected if c in actual and expected[c] != actual[c]):
        problems.append(f"[KO] marker differs: {', '.join(ko)}")
    return problems


def check():
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    failures = 0
    for path in translations():
        name = path.relative_to(ROOT)
        problems = []
        header = read_header(path)
        if header is None:
            problems.append("translation header missing in first line")
        else:
            source, recorded = header
            if not source.exists():
                problems.append(f"source {source.relative_to(ROOT)} not found")
            elif source_hash(source) != recorded:
                problems.append(f"source {source.relative_to(ROOT)} has changed since the last translation update")
        text = path.read_text(encoding="utf-8")
        if wrong := sorted({v for v in VERSION_PATTERN.findall(text) if v != version}):
            problems.append(f"version {', '.join(wrong)} does not match VERSION {version}")
        if "ß" in text:
            problems.append('contains "ß" (Swiss orthography requires "ss")')
        if path == QUESTIONNAIRE_DE:
            problems.extend(check_questionnaire())
        if problems:
            failures += 1
            print(f"FAIL  {name}")
            for problem in problems:
                print(f"      - {problem}")
        else:
            print(f"OK    {name}")
    return failures


def stamp(name):
    path = ROOT / name
    header = read_header(path)
    if header is None:
        sys.exit(f"{name}: translation header missing in first line")
    source, _ = header
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    lines[0] = f"<!-- translation-of: {source.relative_to(ROOT)} | source-sha256: {source_hash(source)} -->\n"
    path.write_text("".join(lines), encoding="utf-8")
    print(f"Stamped {name} with the current hash of {source.relative_to(ROOT)}")


def main():
    parser = argparse.ArgumentParser(description="Check the German translations.")
    parser.add_argument("--stamp", metavar="FILE", help="record the current source hash in FILE")
    args = parser.parse_args()
    if args.stamp:
        stamp(args.stamp)
        return
    sys.exit(1 if check() else 0)


if __name__ == "__main__":
    main()
