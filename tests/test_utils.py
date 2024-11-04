import pytest
import bcrypt
from fastapi_admin.utils import generate_random_str, check_password, hash_password

def test_generate_random_str_length():
    length = 10
    result = generate_random_str(length)
    assert len(result) == length

def test_generate_random_str_digits():
    length = 10
    result = generate_random_str(length, is_digit=True)
    assert result.isdigit()

def test_generate_random_str_letters_and_digits():
    length = 10
    result = generate_random_str(length, is_digit=False)
    assert any(c.isalpha() for c in result)
    assert any(c.isdigit() for c in result)

def test_hash_password():
    password = "my_secret_password"
    hashed = hash_password(password)
    assert bcrypt.checkpw(password.encode(), hashed.encode())

def test_check_password_correct():
    password = "my_secret_password"
    hashed = hash_password(password)
    assert check_password(password, hashed)

def test_check_password_incorrect():
    password = "my_secret_password"
    wrong_password = "wrong_password"
    hashed = hash_password(password)
    assert not check_password(wrong_password, hashed)
