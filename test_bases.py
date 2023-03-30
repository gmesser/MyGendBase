import pytest
from bases import parse_bases, print_bases

def test_parse_bases():
    assert parse_bases('1010', 2) == 10
    assert parse_bases('255', 10) == 255
    assert parse_bases('FF', 16) == 255
    assert parse_bases('10000', 2) == 16
    assert parse_bases('7F', 16) == 127

def test_print_bases(capsys):
    print_bases(10)
    captured = capsys.readouterr()
    assert captured.out == '10 (0b1010, 0xA)\n'

    print_bases(255)
    captured = capsys.readouterr()
    assert captured.out == '255 (0b11111111, 0xFF)\n'

    print_bases(16)
    captured = capsys.readouterr()
    assert captured.out == '16 (0b10000, 0x10)\n'

