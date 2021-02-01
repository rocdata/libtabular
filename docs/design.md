Design
======

The high-level plan for `libtabular` is to implement reader and writer wrappers
around the `petl` library that transparently take care of mapping CSV header
metadata to the `metadata` property on the resulting `Table` subclass.

Pre-processing logic
--------------------

We use the following implementation for the parse-and-skip-headers logic:

- 1. Open source for reading headers=None
- 2. Read file as tuples (assume not big-data and fits into memory)
- 3. Parse the header to detect metadata rows, find header row, and rest of data
- 4. Copy all data rows to a `petl.MemorySource` buffer
- 5. Create a new CSVView from the in-memory buffer, with `header` from step 3
- 6. Return to user the `MemorySource`-backed CSVView for further processing
