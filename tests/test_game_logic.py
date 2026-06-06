import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from logic_utils import check_guess

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
