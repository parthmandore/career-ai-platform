"""
Resume Parser

Responsible for extracting raw text from uploaded PDF resumes.
"""

from pathlib import Path

import pdfplumber


def extract_resume_text(pdf_path: str) -> str:
    """
    Extract text from a PDF resume.

    Args:
        pdf_path (str): Path to uploaded PDF

    Returns:
        str: Extracted resume text
    """

    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        raise FileNotFoundError(
            f"{pdf_path} does not exist."
        )

    extracted_text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:

                extracted_text += page_text + "\n"

    return extracted_text.strip()