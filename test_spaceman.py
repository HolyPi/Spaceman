from spaceman import *

def test_is_guess_in_word():
    guess = "bunny"
    secret_word = "bunny"
    assert is_guess_in_word(guess, secret_word) == True


def test_get_guessed_word():
    secret_word = "bird"
    letters_guessed = ["b", "i", "r", "d"]
    assert get_guessed_word(secret_word, letters_guessed) == secret_word


def test_is_word_guessed():
    secret_word = "thumbsup"
    letters_guessed = ["n", "e", "c", "k"]
    assert is_word_guessed(secret_word, letters_guessed) == False
