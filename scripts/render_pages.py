"""Render Class 9-10 Physics Chapter 2 (PDF pages 37-66) to PNG images.

Usage (from the project root):
    python -m scripts.render_pages
"""
from pathlib import Path

from app.utils import pdf_to_images

BOOKS_DIR = Path(__file__).resolve().parent.parent / "books"


def main():
    paths = pdf_to_images(
        pdf_path=BOOKS_DIR / "2026_Class 9-10_Physics_Bangla_version.pdf",
        destination=BOOKS_DIR / "page_images" / "class-9-10" / "physics" / "chapter-2",
        start=37,
        end=66,
    )
    print(f"Done: {len(paths)} images → {paths[0].parent}")


if __name__ == "__main__":
    main()
