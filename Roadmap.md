# Roadmap — Text 2 CSV Converter

This document outlines plans for the utility's development, improvements to its architecture, and the addition of new features.

---

## 🟢 v0.1.0-alpha (Текущий статус) — Базовый каркас
- [x] Initializing the CLI interface based on `Typer`.
- [x] Omnivorous string parsing (automatic handling of multiple spaces and tabs).
- [x] Building the installer using `Inno Setup`.

---

## 🟡 v0.2.0-alpha — Инженерная надежность и UX
*Main focus: protecting against invalid data and improving readability in the terminal.*

### 🛠 UX improvements
- [x] Pre-normalization of numerical data: automatic correction of the format `3,14 -> 3.14` using regular expressions (Lookbehind/Lookahead).
- [ ] **Smart `--preview`:** displays the first 5 rows of normalized data as a formatted `Rich.table` directly in the console.
- [ ] Encoding option to support legacy encodings (cp1251) with informative UnicodeDecodeError handling.

### 📐 Quality assurance and automation (Infrastructure)
- [ ] Module coverage with unit tests based on `pytest` (testing the normalization of ordinary numbers and exponential forms, and the preservation of text strings).
- [ ] Build automation via .bat file.

