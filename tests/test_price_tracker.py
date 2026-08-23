import pytest

from price_tracker import parse_price, should_alert


def test_price_is_read_from_selected_element():
    html = '<p class="cost">Now £1,249.50</p>'
    assert parse_price(html, ".cost") == 1249.50


def test_missing_selector_has_clear_error():
    with pytest.raises(ValueError, match="No element"):
        parse_price("<p>£10</p>", ".missing")


def test_text_without_price_is_rejected():
    with pytest.raises(ValueError, match="contain a price"):
        parse_price('<p class="cost">Unavailable</p>', ".cost")


def test_target_includes_equal_price():
    assert should_alert(50, 50)
    assert not should_alert(51, 50)
