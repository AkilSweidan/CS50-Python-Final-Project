import pytest
from project import format_price, convert_usd_to_xau, build_table

def test_format_price():
    assert format_price(1234.5) == "1,234.50"
    assert format_price(0) == "0.00"
    assert format_price(1000000.789) == "1,000,000.79"

def test_convert_usd_to_xau():
    assert pytest.approx(convert_usd_to_xau(1000, 2000), rel=1e-6) == 0.5
    with pytest.raises(ValueError):
        convert_usd_to_xau(100, 0)

def test_build_table():
    rows = [[1, "BTC", 50000], [2, "ETH", 3000]]
    headers = ["Rank", "Name", "Price"]
    table_str = build_table(rows, headers)
    assert "BTC" in table_str
    assert "ETH" in table_str
    assert "Rank" in table_str