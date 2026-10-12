# Prerequisite: pip install pypdf
# Run: python split_pdf.py input.pdf

import sys
from pathlib import Path
from pypdf import PdfReader, PdfWriter

src = Path(sys.argv[1])
reader = PdfReader(src)

for i, page in enumerate(reader.pages, start=1):
    writer = PdfWriter()
    writer.add_page(page)
    out = src.with_name(f"{src.stem}_page{i}.pdf")
    with open(out, "wb") as f:
        writer.write(f)
    print(f"Wrote {out}")
