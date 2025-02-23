# TODO

- read in xml
- retrieve all data from the URLs
- analyse the htmls for the following:
  - H-Structure correct? H1->H2->H3
  - alt tag containing content?
  - Page title present?
  - lang is set to de?
  -

beeclear/
│
├── beeclear/
│ ├── **init**.py # Initializes the package
│ ├── cli.py # Typer app and CLI commands
│ ├── crawler.py # Crawling logic
│ ├── analyzer.py # WCAG analysis functions
│ ├── utils.py # Helper utilities
│
├── tests/ # Unit tests
│ ├── test_crawler.py
│ ├── test_analyzer.py
│ ├── test_utils.py
│
├── pyproject.toml # Poetry project config
└── README.md # Project documentation
