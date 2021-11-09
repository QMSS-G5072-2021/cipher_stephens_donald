from qmsspkg_DS import qmsspkg_DS

import pytest

def test_cipher_single_word():
    result = cipher(text = 'absent', shift = 1, encrypt = True)
    assert(result) == 'bctfou', 'Should be ''bctfou'''

@pytest.mark.parametrize("example, shift, expected", [
    ('absent', 1, 'bctfou'),
    ('a', 1, 'b'),
    ('Absent', 1, 'Bctfou'),
    ('ABSENT', 1, 'BCTFOU'),
    ('absent@', 1, 'bctfou@'),
    ('-absent@', 1, '-bctfou@'),
    ('student was ABSENT', 1, 'tuvefou xbt BCTFOU'),
    ('$', 1, '$')
])
def test_cipher_cases_looping(example, shift, expected):
    result = cipher(text = example, shift = shift, encrypt = True)
    assert result == expected
