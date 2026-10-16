"""Generate the resume PDF from the HTML source."""

from pathlib import Path

from weasyprint import HTML


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "resume.html"
OUTPUT = HERE / "Zhang_Yuanmin_Resume.pdf"


def main() -> None:
    HTML(filename=str(SOURCE), base_url=str(HERE)).write_pdf(str(OUTPUT))
    print(OUTPUT)


if __name__ == "__main__":
    main()
