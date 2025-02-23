# cli.py
import typer
from beeclear.crawler import crawl_sitemap
from pathlib import Path

app = typer.Typer()


@app.command()
def main(xml_file: Path = typer.Argument(..., help="Path to the XML file")):
    """Crawl sitemap and save HTML pages."""
    crawl_sitemap(xml_file)


if __name__ == "__main__":
    app(prog_name="beeclear")
