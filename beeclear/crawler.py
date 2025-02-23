# crawler.py
import os
import requests
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from beeclear.utils import create_output_dir


def crawl_sitemap(xml_file: str):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    output_dir = create_output_dir()

    namespaces = {
        "": "http://www.sitemaps.org/schemas/sitemap/0.9",
        "image": "http://www.google.com/schemas/sitemap-image/1.1",
    }

    for url in root.findall(".//url", namespaces):
        loc = url.find(".//loc", namespaces)
        if loc is not None:
            response = requests.get(loc.text)
            if response.status_code == 200:
                # do something with returned html
                filename = os.path.join(output_dir, f"{Path(loc.text).name}.html")
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(response.text)
