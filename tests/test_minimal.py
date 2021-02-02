
from libtabular import fromcsvwithheader


def test_minimal_csv():
    testcsvpath = 'samples/minimal.csv'
    table = fromcsvwithheader(testcsvpath)

    # check metadata
    assert "key1" in table.metadata
    assert "value1" == table.metadata["key1"]

    # check data
    data_dicts = list(table.dicts())
    assert len(data_dicts) == 3

    # spot check first row:
    expected = {
        'section_id': '002',
        'slug': 'dataformat',
        'title': 'CSV files with metadata',
        'description': 'Description of the CSV-with-metadata-header data format',
        'url': 'https://github.com/rocdata/libtabular/blob/main/docs/dataformat.md'
    }
    assert data_dicts[0] == expected

