"""Build the questionnaire PDFs from the Markdown sources.

    assessment/assessment-questionnaire.md     -> templates/acp-assessment-questionnaire.pdf
    assessment/assessment-questionnaire.de.md  -> templates/acp-assessment-questionnaire-de.pdf

Usage (from the repository root):

    python3 tools/build-questionnaire-pdf.py            # all languages
    python3 tools/build-questionnaire-pdf.py --lang de  # one language

Requires Python 3 and Google Chrome, Chromium or Microsoft Edge. Set the CHROME
environment variable to the browser executable if it is not found automatically.
"""
import html
import os
import re
import shutil
import subprocess
import argparse
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANGUAGES = {
    "en": {
        "source": ROOT / "assessment" / "assessment-questionnaire.md",
        "target": ROOT / "templates" / "acp-assessment-questionnaire.pdf",
        "title": "ACP Assessment Questionnaire",
        "page_breaks": ("Domain", "Result Summary"),
    },
    "de": {
        "source": ROOT / "assessment" / "assessment-questionnaire.de.md",
        "target": ROOT / "templates" / "acp-assessment-questionnaire-de.pdf",
        "title": "ACP-Fragenkatalog",
        "page_breaks": ("Domäne", "Ergebnisübersicht"),
    },
}
BROWSERS = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "google-chrome",
    "chromium",
    "chromium-browser",
    "msedge",
]

CSS = """
@page { size: A4 landscape; margin: 14mm 12mm; }
body { font-family: -apple-system, "Helvetica Neue", Arial, sans-serif; font-size: 9pt; color: #1a1a1a; }
h1 { color: #1f3a5f; font-size: 15pt; border-bottom: 2px solid #2f6db3; padding-bottom: 3px; margin: 14px 0 8px; }
h1:first-of-type { font-size: 20pt; }
hr { display: none; }
table { border-collapse: collapse; width: 100%; margin: 6px 0 8px; page-break-inside: auto; }
tr { page-break-inside: avoid; }
th { background: #1f3a5f; color: #fff; text-align: left; padding: 4px 5px; }
td { border: 1px solid #b8c4d4; padding: 4px 5px; vertical-align: top; }
.q td:nth-child(1) { width: 4%; font-weight: 600; }
.q td:nth-child(2) { width: 17%; }
.q td:nth-child(3) { width: 30%; }
.q td:nth-child(4) { width: 27%; font-size: 8pt; color: #33475b; }
.q td:nth-child(5) { width: 5%; }
.q td:nth-child(6) { width: 17%; }
code { font-family: Menlo, monospace; font-size: 8pt; }
p { margin: 4px 0; }
p.note { border-left: 3px solid #2f6db3; background: #eef3fa; padding: 4px 8px; }
h1 + table, h1 + p { page-break-before: avoid; }
"""


def inline(text):
    text = html.escape(text, quote=False).replace("&lt;br&gt;", "<br>")
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    return re.sub(r"`(.+?)`", r"<code>\1</code>", text)


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def convert(md, lang="en"):
    config = LANGUAGES[lang]
    out, lines, i = [], md.splitlines(), 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("<!--"):
            pass
        elif line.startswith("> "):
            out.append(f'<p class="note">{inline(line[2:])}</p>')
        elif line.startswith("# "):
            brk = ' style="page-break-before: always"' if line[2:].startswith(config["page_breaks"]) else ""
            out.append(f"<h1{brk}>{inline(line[2:])}</h1>")
        elif line.strip() == "---":
            out.append("<hr>")
        elif line.startswith("|"):
            head = cells(line)
            i += 2
            cls = ' class="q"' if len(head) == 6 else ""
            rows = [f"<table{cls}><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr>"]
            while i < len(lines) and lines[i].startswith("|"):
                row = [inline(c) for c in cells(lines[i])]
                if cls and len(row) > 3:
                    # Scoring guidance: highlight the labels "Show:", "2:" and "3:".
                    row[3] = re.sub(r"(^|<br>)([^:<]{1,20}):", r"\1<strong>\2:</strong>", row[3])
                rows.append("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>")
                i += 1
            out.append("".join(rows) + "</table>")
            continue
        elif re.match(r"^\d+\. ", line):
            items = []
            while i < len(lines) and re.match(r"^\d+\. ", lines[i]):
                items.append(f"<li>{inline(lines[i].split('. ', 1)[1])}</li>")
                i += 1
            out.append("<ol>" + "".join(items) + "</ol>")
            continue
        elif line.strip():
            out.append(f"<p>{inline(line.strip())}</p>")
        i += 1
    return (f"<!doctype html><html lang='{lang}'><head><meta charset='utf-8'><title>{config['title']}</title>"
            f"<style>{CSS}</style></head><body>{''.join(out)}</body></html>")


def find_browser():
    candidates = [os.environ["CHROME"]] if os.environ.get("CHROME") else BROWSERS
    for candidate in candidates:
        path = candidate if os.path.isfile(candidate) else shutil.which(candidate)
        if path:
            return path
    sys.exit("No Chrome, Chromium or Edge executable found. Set the CHROME environment variable.")


def build(lang, browser):
    config = LANGUAGES[lang]
    document = convert(config["source"].read_text(encoding="utf-8"), lang)
    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / "questionnaire.html"
        page.write_text(document, encoding="utf-8")
        subprocess.run(
            [browser, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
             f"--print-to-pdf={config['target']}", page.as_uri()],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
    print(f"Written {config['target'].relative_to(ROOT)}")


def main():
    parser = argparse.ArgumentParser(description="Build the ACP questionnaire PDFs.")
    parser.add_argument("--lang", choices=sorted(LANGUAGES), help="build only this language")
    args = parser.parse_args()
    browser = find_browser()
    for lang in [args.lang] if args.lang else LANGUAGES:
        build(lang, browser)


if __name__ == "__main__":
    main()
