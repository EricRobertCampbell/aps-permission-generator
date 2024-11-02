#!/usr/bin/env python3

import json
import re

def generate_latex_file(data):
    template = ""
    with open("template.tex", "r") as file:
        template = file.read()
    for entry in data:
        presenter = entry['presenter']
        date = entry['dateOfPresentation']
        title = entry['title']
    # Generate a sanitized filename
        filename = f"permission_{re.sub(r'_+', '_', re.sub(r'[^a-zA-Z]', '_', presenter.lower()))}.tex"
        content = template.replace(r"\newcommand{\presenterName}{}", f"\\newcommand{{\\presenterName}}{{{presenter}}}")
        content = content.replace(r"\newcommand{\presentationDate}{}", f"\\newcommand{{\\presentationDate}}{{{date}}}")
        content = content.replace(r"\newcommand{\presentationTitle}{}", f"\\newcommand{{\\presentationTitle}}{{{title}}}")

        with open(filename, "w") as file:
            file.write(content)

if __name__ == "__main__":
    with open("data.json", "r") as file:
        data = json.load(file)
    generate_latex_file(data)

