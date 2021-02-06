import pytest


@pytest.fixture
def sampledata2():
    """
    A small data sample with non-ascii characters and other "tricky" stuff.
    """
    metadata = {
        "key3": "value3",
        "key4 (space)": "value4 (with brackets)",
        "ключ5": "данни5",
    }
    header = ["f1", "f2 with spaces", "фийлд3 (non-ascii)", "field4, with comma"]
    data = [
        ('1', '2', '3', '4'),
        ('вальо', 'Smith, John', '1', '1.1'),
        ('other punct ;"*_f#[]%@!~`', 'val (val)', '', 'zzzzz')
    ]

    return dict(
        metadata=metadata,
        header=header,
        data=data,
    )