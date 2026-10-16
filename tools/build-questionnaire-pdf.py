"""Build templates/acp-assessment-questionnaire.pdf from assessment/assessment-questionnaire.md.

Usage (from the repository root):

    python3 tools/build-questionnaire-pdf.py

Requires Python 3 and Google Chrome, Chromium or Microsoft Edge. Set the CHROME
environment variable to the browser executable if it is not found automatically.
"""
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "assessment" / "assessment-questionnaire.md"
TARGET = ROOT / "templates" / "acp-assessment-questionnaire.pdf"
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
td:nth-child(1) { width: 4%; font-weight: 600; }
td:nth-child(2) { width: 24%; }
td:nth-child(3) { width: 40%; }
td:nth-child(4) { width: 6%; }
.q td:nth-child(5) { width: 26%; }
code { font-family: Menlo, monospace; font-size: 8pt; }
p { margin: 4px 0; }
h1 + table, h1 + p { page-break-before: avoid; }
"""


def inline(text):
    text = html.escape(text, quote=False).replace("&lt;br&gt;", "<br>")
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    return re.sub(r"`(.+?)`", r"<code>\1</code>", text)


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def convert(md):
    out, lines, i = [], md.splitlines(), 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("# "):
            brk = ' style="page-break-before: always"' if line[2:].startswith(("Domain", "Result Summary")) else ""
            out.append(f"<h1{brk}>{inline(line[2:])}</h1>")
        elif line.strip() == "---":
            out.append("<hr>")
        elif line.startswith("|"):
            head = cells(line)
            i += 2
            cls = ' class="q"' if len(head) == 5 else ""
            rows = [f"<table{cls}><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr>"]
            while i < len(lines) and lines[i].startswith("|"):
                rows.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in cells(lines[i])) + "</tr>")
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
    title = "ACP Assessment Questionnaire"
    return f"<!doctype html><html><head><meta charset='utf-8'><title>{title}</title><style>{CSS}</style></head><body>{''.join(out)}</body></html>"


def find_browser():
    candidates = [os.environ["CHROME"]] if os.environ.get("CHROME") else BROWSERS
    for candidate in candidates:
        path = candidate if os.path.isfile(candidate) else shutil.which(candidate)
        if path:
            return path
    sys.exit("No Chrome, Chromium or Edge executable found. Set the CHROME environment variable.")


def main():
    document = convert(SOURCE.read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / "questionnaire.html"
        page.write_text(document, encoding="utf-8")
        subprocess.run(
            [find_browser(), "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
             f"--print-to-pdf={TARGET}", page.as_uri()],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
    print(f"Written {TARGET.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
