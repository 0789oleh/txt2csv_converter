# Text 2 CSV Converter (v0.1.0-alpha) 🚀

[![GitHub release](https://img.shields.io/github/v/release/0789oleh/txt2csv_converter?include_prereleases)](https://github.com/0789oleh/txt2csv_converter/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A lightweight and fast Python CLI utility for converting text data (logs, scientific output, TSV files) to CSV format. Ideal for preparing data for analysis in Excel, Pandas, or Origin.

## ✨ Features
* **Smart parsing:** Automatically handles any number of spaces or tabs between columns (ideal for scientific data).
* **Modern CLI:** Built on `Typer` with beautiful output via `Rich`.
* **Validation:** Checks file existence and permissions on the fly.
* **Standalone EXE:** Does not require Python to be installed on the system.

## 📥 Installation

### Windows (Installer)
Download `text2csv_setup_v0.1.0-alpha.exe` from the releases page and follow the installer's instructions.

### Portable
Just download `txt2csv_converter.exe` and run it in terminal.

> **Note:** To easily run the application from any folder, add the path to the installed application to the `PATH` environment variable.

## 🚀 Usage

```bash
# View help
text2csv_converter --help

# Simple conversion
text2csv_converter data.txt result.csv

# Conversion with quote
text2csv_converter data.txt result.csv --quote "'"```