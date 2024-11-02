# APS Permission PDF Generator

This project is designed to automatically generate permission PDFs for speakers at the Alberta Palaeontological Society (APS) events. Each PDF will include the APS logo, presenter information, and options for sharing their presentation online.

## Files and Directories

-   **makefile**: Automates the process of generating `.tex` files, compiling them into PDFs, and cleaning up generated files.
-   **process.py**: A Python script that reads `data.json` and generates LaTeX files for each presenter based on their information.
-   **data.json**: A JSON file containing an array of objects with presenter details, including `presenter`, `dateOfPresentation`, and `title`.
-   **.gitignore**: Specifies files and directories that should be ignored by Git.
-   **README.md**: This file, providing an overview of the project.

## Usage

1. **Update `data.json`**: Populate the `data.json` file with presenter information in the specified format.
2. **Run makefile**: Use the following command to generate PDFs:

```bash
make
```

This command will run process.py, create the necessary .tex files, and compile them into PDF documents. 3. Clean Up: To remove generated PDF files and auxiliary files, run:

```bash
make clean
```

To remove all generated files, including .tex files, use:

```bash
make depclean
```

### Requirements

-   LaTeX distribution (e.g., TeX Live, MikTeX)
-   Python 3.x
-   latexmk (for automated LaTeX compilation)

### Acknowledgments

[Alberta Palaeontological Society (APS)](https://albertapaleo.org) for providing the context and need for this tool.
