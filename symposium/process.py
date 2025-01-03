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
        filename = presenter.lower()
        filename = re.sub(r'[^a-zA-Z]', '_', filename)
        filename = re.sub(r'_+', '_', filename)
        filename = re.sub(r'(^_+)|(_+$)', '', filename)
        filename = f"permission_{filename}.tex"
        content = template.replace(r"\newcommand{\presenterName}{}", f"\\newcommand{{\\presenterName}}{{{presenter}}}")
        content = content.replace(r"\newcommand{\presentationDate}{}", f"\\newcommand{{\\presentationDate}}{{{date}}}")
        content = content.replace(r"\newcommand{\presentationTitle}{}", f"\\newcommand{{\\presentationTitle}}{{{title}}}")

        with open(filename, "w") as file:
            print('Writing to file:', filename)
            file.write(content)

if __name__ == "__main__":
    with open("data.json", "r") as file:
        data = json.load(file)
    generate_latex_file(data)

