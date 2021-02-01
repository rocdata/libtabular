

def parse_metadata_header(table, sample_size=30):
    """
    Given a PETL table-like object opened from any source with header=None,
    parse a sample of the rows to identify:
     - `num_metadata_rows` (int): number of rows containing key-value pairs
     - `metadatata`: contents of header rows as a `dict` where the metadata rows
       are interpreted as: key = first_column.rstrip(":") (str), value = second_column (str).
     - `header` list(str): the contents of the "column headers" row, which separates
       metadata header rows from data rows.

    This information is sufficient for subsequent processing of this data file:
     - use `header` as the column names (possibly post-processed/renamed).
     - when reading data from file, skip the first `num_metadata_rows+1`
       before starting to return data.
    """
    sample = table[0:sample_size]
    rows = list(sample)

    assert rows, 'unexpected empty table given'

    data_width = len(rows[0])
    for row in rows:
        if len(row) != data_width:
            raise ValueError("Unexpected 'ragged' rows table encountered")

    # convert to radded-rows (truncate row to end of non-empty values)
    succinct_rows = []
    for row in rows:
        succinct_row = []
        for colidx in range(0,len(row)):
            if all(col.strip() == "" for col in row[colidx:]):
                succinct_row = row[0:colidx]
                break
        if not succinct_row:
            succinct_row = row
        succinct_rows.append(succinct_row)
        print()

    assert len(succinct_rows[-1]) == data_width, 'Insufficient sample of rows taken'

    # go through rows to parse metadata and find header row
    num_metadata_rows = None
    metadata = {}
    header = None
    for i, succinct_row in enumerate(succinct_rows):
        if len(succinct_row) < data_width:
            key = succinct_row[0].strip(':')
            value = succinct_row[1].strip()
            metadata[key] = value
        else:
            # found the header!
            num_metadata_rows = i
            header = succinct_row
            break

    return (num_metadata_rows, metadata, header)

