import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from logic_utils import check_guess
from app import parse_guess

# FIX: added underscore for message since check_guess returns multiple outputs
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

# FIX: Added tests to check if the hint matches the logic

def test_too_high_message_correct():
    # When guess is too high, message should say "Go LOWER!" not "Go HIGHER!"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_too_low_message_correct():
    # When guess is too low, message should say "Go HIGHER!" not "Go LOWER!"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

def test_winning_message():
    # When guess equals secret, should return correct message
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_check_guess_handles_string_input():
    # check_guess should convert string inputs to integers
    outcome, message = check_guess("50", "50")
    assert outcome == "Win"
    assert message == "🎉 Correct!"

# FIX: Added tests for input range validation

def test_parse_guess_valid_in_range():
    # Test that valid guesses between 1-100 are accepted
    ok, guess_int, err = parse_guess("50")
    assert ok is True
    assert guess_int == 50
    assert err is None


def test_parse_guess_lower_boundary():
    # Test that guess at lower boundary (1) is accepted
    ok, guess_int, err = parse_guess("1")
    assert ok is True
    assert guess_int == 1
    assert err is None


def test_parse_guess_upper_boundary():
    # Test that guess at upper boundary (100) is accepted
    ok, guess_int, err = parse_guess("100")
    assert ok is True
    assert guess_int == 100
    assert err is None


def test_parse_guess_below_range():
    # Test that guess below 1 is rejected
    ok, guess_int, err = parse_guess("0")
    assert ok is False
    assert guess_int is None
    assert err == "Guess must be between 1 and 100."


def test_parse_guess_negative():
    # Test that negative guess is rejected
    ok, guess_int, err = parse_guess("-5")
    assert ok is False
    assert guess_int is None
    assert err == "Guess must be between 1 and 100."


def test_parse_guess_above_range():
    # Test that guess above 100 is rejected
    ok, guess_int, err = parse_guess("101")
    assert ok is False
    assert guess_int is None
    assert err == "Guess must be between 1 and 100."


def test_parse_guess_large_number():
    # Test that very large guess is rejected
    ok, guess_int, err = parse_guess("999")
    assert ok is False
    assert guess_int is None
    assert err == "Guess must be between 1 and 100."


def test_parse_guess_decimal_in_range():
    # Test that decimal input is converted and validated
    ok, guess_int, err = parse_guess("50.7")
    assert ok is True
    assert guess_int == 50
    assert err is None


def test_parse_guess_decimal_out_of_range():
    # Test that decimal input above 100 is rejected
    ok, guess_int, err = parse_guess("100.5")
    assert ok is False
    assert guess_int is None
    assert err == "Guess must be between 1 and 100."
