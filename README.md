# libtabular
A general purpose library for reading and writing tabular data (CSV, TSV, gsheets, ods, xlsx).


## Pitch
Imagine a `csv.DictReader`-like API you can use to "open" and "read" any source
of tabular data (CSV, TSV, gsheets, ods, xlsx) without having to worry about a
million libraries and authentication APIs.

## Tabular data with metadata headers
The main "new feature" that `libtabular` provides is a way to parse "metadata headers"
in tabular data (e.g. CSV) automatically. These "CSV metadata headers" are directly
analogous to the YAML headers that sometimes appear in Markdown files used in
static site generators.


## Example

    TODO


Using `libtabular` you would easily "extract" the data and metadata from this source
file using a few commands:

```python
from libtabular import loadpath

dataset = loadpath('samples/minimal.csv')
dataset.get_metadata()
DICT

dataset.get_data()
ROWS OF DICTS

dataset.get_keys()
LIST

```

## Why is this needed?

Recent work on a repository of curriculum documents, see [rocdata.global](https://rocdata.global),
requires an easy-to-use process for import and export of curriculum data like:
 - Curriculum standards documents (excel sheets that specify what students should be learning)
 - Content collections data (excel sheets that consists of links to useful learning resources)
 - Content correlations data (excel sheets that contain "links" between curriculum standards
   and relevant learning resources)

The spreadsheet/CSV format is a natural choice for teachers and administrators,
who have experience working with this file type, so it is worth developing tools
that facilitate reading and writing tabular data:

 - Curriculum bodies and ministries of education can publish curriculum standards
   documents information in machine-readable formats (instead of publishing PDFs, publish spreadsheets).
 - Teachers can download standards data in easy-to-use spreadsheet formats
   (use standards for your grade level to plan your lessons).
 - Curriculum experts and teachers can download blank templates with appropriate
   headers to fill in when need to specify standards documents or content correlations.

