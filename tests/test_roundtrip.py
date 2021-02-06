import difflib
import os

from libtabular import fromcsvwithheader
from libtabular import tocsvwithheader



def test_load_and_write(tmpdir):
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

