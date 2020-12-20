
from testy import (
    assertEqual,
    cli,
)

from __init__ import (
    EOF,
    REPLACE,
    InvalidUTF8Encoding,
    UTF8Decoder,
)

###############################################################################
# Tests
###############################################################################

def test_stress_test():
    # Test processing the UTF-8 decoder capability and stress test from:
    # https://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-test.txt
    input_fh = open('test_data/UTF-8-test.txt', 'rb')
    expected_fh = open('test_data/UTF-8-test.txt.expected', 'r',
                       encoding='utf-8')
    decoder = UTF8Decoder(input_fh, errors=REPLACE)
    for c in decoder:
        if c == EOF:
            break
        assertEqual(c, expected_fh.read(1))

def test_i_can_eat_glass():
    # Test processing the "I CAN EAT GLASS" section at:
    # http://kermitproject.org/utf8.html#glass
    original_fh = open('test_data/i_can_eat_glass.txt', 'r', encoding='utf-8')
    decoder_fh = open('test_data/i_can_eat_glass.txt', 'rb')
    decoder = UTF8Decoder(decoder_fh, errors=REPLACE)
    for c in decoder:
        if c == EOF:
            break
        assertEqual(c, original_fh.read(1))

###############################################################################

if __name__ == '__main__':
    cli(globals())
