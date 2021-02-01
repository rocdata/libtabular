Design
======

The high-level plan for `libtabular` is to implement reader and writer wrappers
around the `petl` library that transparently take care of mapping CSV header
metadata to the `metadata` property on the resulting `Table` subclass.

At least two possible implementations exist for the parse-and-skip-headers logic.


### Two-stage reading logic implementation

1. Inspection stage:
   - 1.1. Open and read sample of first :30 rows from file.
   - 1.2. Parse sample to detect metadata rows and infer header row.
   - 1.3. Close
2. Read stage:
   - 2.1. Re-open file setting appropriate header from 1.2
   - 2.2. Consume the first `num_metadata_rows` rows and parse metadata key-value pairs.
     Add key-value info (dict) to the `Table` object under the `metadata` property (monkey patching)
   - 2.3. Skip and header row
   - 2.4. Return to user the rest of iterator for further processing.


### One-step, in-memory reading logic

1. Loading pre-processors step:
   - 1.1. Open source for reading headers=None
   - 1.2. Read file as tuples
   - 1.3. Inspection sub-step:
     - Parse sample of first :30 rows from file to detect metadata rows and infer header row.
   - 1.4. Copy all data rows (rows starting at index `num_metadata_rows+1`) to a MemorySource buffer
   - 1.5. Create CSVView from the in-memory buffer, with `headers` obtained from step 1.3
   - 1.6. Return user the MemorySource-backed CSVView for further processing.
