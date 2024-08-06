import pytest
from fuel import convert, gauge

def test_convert():
    assert convert('1/2') == 50
    assert convert('3/4') == 75
    assert convert('99/100') == 99

    with pytest.raises(ValueError):
        assert convert('4/3')
        assert convert('abc/def')

    with pytest.raises(ZeroDivisionError):
        assert convert('1/0')

def test_gauge():
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'
    assert gauge(50) == '50%'
