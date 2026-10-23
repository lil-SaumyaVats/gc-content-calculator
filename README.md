# GC Content Calculator

A Python tool for validating DNA sequences and calculating their GC content.

This program takes a DNA sequence as input, checks whether it contains valid DNA bases (`A`, `T`, `G`, `C`), and calculates the percentage of guanine (G) and cytosine (C) in the sequence.

## Features

* Converts DNA sequences to uppercase.
* Validates DNA sequences and handles empty input.
* Counts the total number of bases.
* Counts G and C nucleotides separately.
* Calculates GC content as a percentage.
* Displays the result rounded to two decimal places.

## Formula

**GC Content (%) = [(G count + C count) / Total bases] × 100**

## Example

**Input:**

```text
atttgctga
```

**Output:**

```text
Valid DNA sequence
Total bases: 9
G_count: 2
C_count: 1
GC_content: 33.33%
```

## How to Run

1. Make sure Python is installed.
2. Clone or download this repository.
3. Open a terminal in the project folder and run:

```bash
python gc_content_calculator.py
```
