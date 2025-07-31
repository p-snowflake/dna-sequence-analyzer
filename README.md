# 🧬 DNA Sequence Analyzer

A simple bioinformatics tool built using Streamlit to analyze DNA sequences from FASTA files or plain text input. This beginner-friendly project performs basic sequence analysis and displays simple visualizations.

## Features

* Nucleotide count (A, T, G, C)
* Base composition percentages
* GC content and AT content
* GC/AT content ratio
* Reverse complement of the sequence
* Pie chart and bar chart visualizations

## Input Options

* Upload a DNA sequence file in `.fasta` or `.fa` format
* Or manually enter a DNA sequence in the text box

## Technologies Used

* Python
* Streamlit
* Matplotlib

## Notes

* Only DNA sequences are supported. RNA or protein sequences are not handled.
* Maximum file size for upload is 200MB (Streamlit's default limit).

## How to Run

1. Clone the repository:
   `git clone https://github.com/p-snowflake/dna-sequence-analyzer.git`
   `cd dna-sequence-analyzer`

2. Install the required packages:
   `pip install streamlit matplotlib`

3. Run the app:
   `streamlit run atgc.py`
   If that doesn't work, try:
   `python -m streamlit run atgc.py`
