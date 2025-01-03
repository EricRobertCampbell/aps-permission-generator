LATEXMK = latexmk
LATEXMKFLAGS = -pdf # -quiet

# Define a pattern rule for generating PDFs from .tex files
%.pdf: %.tex
	$(LATEXMK) $(LATEXMKFLAGS) $<

# Run process.py first to generate .tex files and then make PDFs
.PHONY: all process clean depclean

all: process $(shell ls permission_*.tex 2>/dev/null | sed 's/\.tex$$/.pdf/')

# Generate .tex files from data.json
process:
	python3 process.py

# Clean up intermediate files
clean:
	$(LATEXMK) -c

# Clean up all generated files
depclean: clean
	rm -f *.pdf permission_*.tex

