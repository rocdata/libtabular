CSV-with-headers data format
============================

Regular CSV whose first few rows are interpreted as key-value pairs.
The `libtabular` data loader automatically detects which rows are "metadata",
which row specifies the data headers, and which rows are contain the data values.

