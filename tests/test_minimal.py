
from libtabular import fromcsvwithheader
from libtabular import fromxlswithheader


def test_minimal_csv():
    testcsvpath = 'samples/minimal.csv'
    table = fromcsvwithheader(testcsvpath)

    # check metadata
    assert "key1" in table.metadata
    assert "value1" == table.metadata["key1"]

    # check data
    data_dicts = list(table.dicts())
    assert len(data_dicts) == 4

    # spot check second row:
    expected = {
        'section_id': '002',
        'slug': 'dataformat',
        'title': 'CSV files with metadata',
        'description': 'Description of the CSV-with-metadata-header data format',
        'url': 'https://github.com/rocdata/libtabular/blob/main/docs/dataformat.md'
    }
    assert data_dicts[1] == expected



def test_minimal_xls():
    testxlspath = 'samples/minimal.xls'
    table = fromxlswithheader(testxlspath, "Sheet1")

    # check metadata
    assert "key1" in table.metadata
    assert "value1" == table.metadata["key1"]

    # check data
    data_dicts = list(table.dicts())
    assert len(data_dicts) == 4

    # spot check second row:
    expected = {
        'section_id': '002',
        'slug': 'dataformat',
        'title': 'CSV files with metadata',
        'description': 'Description of the CSV-with-metadata-header data format',
        'url': 'https://github.com/rocdata/libtabular/blob/main/docs/dataformat.md'
    }
    assert data_dicts[1] == expected