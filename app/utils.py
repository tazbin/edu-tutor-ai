"""Render PDF pages to high-quality PNG images for OCR."""
from pathlib import Path

import pymupdf


def pdf_to_images(
    pdf_path: str | Path,
    destination: str | Path,
    start: int = 1,
    end: int | None = None,
    dpi: int = 200,
    name_format: str = "page_{page:03d}.png",
    overwrite: bool = False,
) -> list[Path]:
    """Render pages ``start``..``end`` (1-based, inclusive) of a PDF to PNG images.

    ``name_format`` is formatted with the PDF page number, e.g. ``"page_{page:03d}.png"``
    gives ``page_001.png``. ``end`` defaults to the last page. Existing images are skipped
    unless ``overwrite`` is True. Returns the paths of all images in the range.
    """
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=True)

    paths = []
    with pymupdf.open(pdf_path) as doc:
        end = end or doc.page_count
        if not 1 <= start <= end <= doc.page_count:
            raise ValueError(
                f"invalid page range {start}-{end} (PDF has {doc.page_count} pages)"
            )

        for page_no in range(start, end + 1):
            out = destination / name_format.format(page=page_no)
            if overwrite or not out.exists():
                doc[page_no - 1].get_pixmap(dpi=dpi).save(out)
            paths.append(out)

    return paths
