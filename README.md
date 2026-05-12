# excel-parser-tool

A Python-based utility designed to filter large Excel datasets by keywords across all columns. This tool is built to demonstrate production-ready scripting standards, including logging, error handling, and CLI argument parsing.

## 🚀 Features
- **Global Search:** Scans all columns and rows for specified keywords.
- **CLI-First:** Easily integrable into automated pipelines via command-line arguments.
- **Robust Logging:** Uses the `logging` module to track execution steps and failures.
- **Defensive Programming:** Validates paths and handles missing dependencies gracefully.

## 🛠️ Tech Stack
- **Language:** Python 3.9+
- **Core Library:** [Pandas](https://pandas.pydata.org/)
- **Excel Engine:** [Openpyxl](https://openpyxl.readthedocs.io/)

## 🚀 Quick Start
1. Install dependencies: `pip install -r requirements.txt`
2. Run the tool: `python src/parser.py --input data/sample.xlsx --keywords "Term" --output results.xlsx`