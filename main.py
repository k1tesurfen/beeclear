from pathlib import Path
import typer
import xml.etree.ElementTree as ET

app = typer.Typer()


def analyse(xml_file: Path):
    """Reads an XML sitemap and prints only the <loc> URLs."""
    if not xml_file.exists():
        typer.echo(f"Error: File '{xml_file}' not found!", err=True)
        raise typer.Exit(code=1)

    if xml_file.suffix.lower() != ".xml":
        typer.echo("Error: Only XML files are supported!", err=True)
        raise typer.Exit(code=1)

    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        namespace = {"sitemap": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        loc_elements = root.findall(".//sitemap:loc", namespaces=namespace)

        if not loc_elements:
            typer.echo("No <loc> elements found in the XML.")
            return

        typer.echo("🔗 Sitemap URLs:")
        for loc in loc_elements:
            # do stuff
            typer.echo(loc.text)

    except ET.ParseError as e:
        typer.echo(f"❌ XML Parsing Error: {e}", err=True)
        raise typer.Exit(code=1)


@app.command()
def main(xml_file: Path = typer.Argument(..., help="Path to the XML file")):
    """CLI tool for reading and parsing an XML file."""
    analyse(xml_file)


if __name__ == "__main__":
    app(prog_name="beeclear")
