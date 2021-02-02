CSV-with-headers data format
============================

Regular CSV whose first few rows are interpreted as key-value pairs.
The `libtabular` data loader automatically detects which rows are "metadata",
which row specifies the data headers, and which rows are contain the data values.



Conventions:
- metadata rows must start with `#` character (so we can easily identify them)
- data rows must not start with `#` (i.e. cannot use #-based depth indicator as
  used [hackathon samples](https://docs.google.com/spreadsheets/d/1-ei7BBMOx0udbXxyLJjMPYLW0EJWg9wFUyV9ODa8m5o/edit#gid=1031912854&range=A32:D44).


The `#` prefix for non-data rows allows for basic compatibility with CSV parsers
of other programming languages and libraries:
- Use `pandas.read_csv("input.csv", comment="#")` to skip lines that start with `#`
- In Ruby, skip comments using `CSV.foreach("input.csv", skip_lines: /^#/, headers: true)...`
