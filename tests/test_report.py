import os
from src.report import ReportGenerator

def test_generate_markdown(tmp_path):
    title = "Sample Report"
    content = "This is **markdown** content."
    output_dir = tmp_path / "reports"
    gen = ReportGenerator(output_dir=str(output_dir))

    md_path = gen.generate_markdown(title, content, filename="test_md")
    # File should exist
    assert os.path.exists(md_path)
    # Contents should start with the title
    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()
    assert text.startswith(f"# {title}")
    assert content in text

def test_generate_pdf(tmp_path):
    title = "PDF Report"
    content = "Line 1\nLine 2\nLine 3"
    output_dir = tmp_path / "reports_pdf"
    gen = ReportGenerator(output_dir=str(output_dir))

    pdf_path = gen.generate_pdf(title, content, filename="test_pdf")
    # File should exist and be non-empty
    assert os.path.exists(pdf_path)
    assert os.path.getsize(pdf_path) > 0

git add tests/test_report.py
git commit -m "Add pytest suite for ReportGenerator"
