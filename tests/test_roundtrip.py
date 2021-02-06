import difflib
import os

import petl

from libtabular import fromcsvwithheader
from libtabular import tocsvwithheader

from libtabular import fromxlswithheader
from libtabular import toxlswithheader



# CSV
################################################################################

def test_csv_load_and_write(tmpdir):
    """
    Roundtrip test load a CSV then write out the same data to disk and check the
    output CSV file is the same as the original.
    """
    # load original
    testcsvpath = 'samples/minimal.csv'
    table = fromcsvwithheader(testcsvpath)

    # write copy
    tempfile = os.path.join(tmpdir, 'minimal_out.csv')
    tocsvwithheader(table, tempfile, metadata=table.metadata)

    # diff CSV file contents (ignoring line ending differences)
    expected_lines = open(testcsvpath).readlines()
    observed_lines = open(tempfile).readlines()
    diff_lines = []
    for line in difflib.unified_diff(expected_lines, observed_lines,
        fromfile='expected', tofile='observed', lineterm='', n=0):
        diff_lines.append(line)
    assert diff_lines == [], "found unexpected line differences: " + diff_lines

    # DEBUG: print both files
    # print(open(testcsvpath).read())
    # print('---')
    # print(open(tempfile).read())



def test_csv_write_and_load(tmpdir, sampledata2):
    """
    Roundtrip test write CSV with metadata to disk then load CSV and check the
    data and metadata is the same as the original.
    """
    # original
    metadata = sampledata2["metadata"]
    header = sampledata2["header"]
    data = sampledata2["data"]

    # write to disk
    tempfile = os.path.join(tmpdir, 'roundtrip_test.csv')
    table = [header] + data
    tocsvwithheader(table, tempfile, metadata=metadata)

    # load from disk
    table = fromcsvwithheader(tempfile)

    # checks
    assert table.metadata == metadata, 'different metadata'
    assert table.header == tuple(header), 'different header'
    assert len(list(table.dicts())) == 3, 'wrong number of data rows'
    for exp_row, obs_row in zip(data, petl.data(table)):
        assert exp_row == obs_row, 'different data row encountered'



# XLS
################################################################################

def test_xls_write_and_load(tmpdir, sampledata2):
    """
    Roundtrip test write CSV with metadata to disk then load CSV and check the
    data and metadata is the same as the original.
    """
    # original
    metadata = sampledata2["metadata"]
    header = sampledata2["header"]
    data = sampledata2["data"]

    # write to disk
    tempfile = os.path.join(tmpdir, 'roundtrip_test.xls')
    table = [header] + data
    toxlswithheader(table, tempfile, 'Sheet 1', metadata=metadata)

    # load from disk
    table = fromxlswithheader(tempfile, 'Sheet 1')

    # checks
    assert table.metadata == metadata, 'different metadata'
    assert table.header == tuple(header), 'different header'
    assert len(list(table.dicts())) == 3, 'wrong number of data rows'
    for exp_row, obs_row in zip(data, petl.data(table)):
        assert exp_row == obs_row, 'different data row encountered'
