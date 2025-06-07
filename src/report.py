import os
from datetime import datetime
from fpdf import FPDF

class ReportGenerator:
    """
    Generate Markdown and PDF reports summarizing analysis.
    """

    def __init__(self, output_dir: str = "reports"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_markdown(
        self,
        title: str,
        content: str,
        filename: str = None
    ) -> str:
        """
        Create a Markdown report.
        :param title: Report title.
        :param content: Markdown-formatted body.
        :param filename: Optional filename (without extension).
        :return: Full path to the .md file.
        """
        if filename is None:
            timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
            filename = f"{title.replace(' ', '_')}_{timestamp}"
        path = os.path.join(self.output_dir, f"{filename}.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n")
            f.write(content)
        return path

    def generate_pdf(
        self,
        title: str,
        content: str,
        filename: str = None
    ) -> str:
        """
        Create a simple PDF report.
        :param title: Report title.
        :param content: Plain-text or Markdown body.
        :param filename: Optional filename (without extension).
        :return: Full path to the .pdf file.
        """
        if filename is None:
            timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
            filename = f"{title.replace(' ', '_')}_{timestamp}"
        pdf_path = os.path.join(self.output_dir, f"{filename}.pdf")

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, title, ln=True)
        pdf.ln(5)

        pdf.set_font("Arial", size=12)
        for line in content.split("\n"):
            pdf.multi_cell(0, 8, line)

        pdf.output(pdf_path)
        return pdf_path

git add src/report.py
git commit -m "Add report generation module for Markdown and PDF outputs"
