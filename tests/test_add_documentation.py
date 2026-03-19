```python
import pytest
from app.features import add_documentation

def test_add_documentation_returns_correct_value():
    # Arrange
    documentation_text = "This is a test documentation."
    expected_result = "Documentation added: This is a test documentation."

    # Act
    result = add_documentation(documentation_text)

    # Assert
    assert result == expected_result

def test_add_documentation_handles_empty_string():
    # Arrange
    documentation_text = ""
    expected_result = "No documentation added."

    # Act
    result = add_documentation(documentation_text)

    # Assert
    assert result == expected_result

def test_add_documentation_handles_none_input():
    # Arrange
    documentation_text = None
    expected_result = "No documentation added."

    # Act
    result = add_documentation(documentation_text)

    # Assert
    assert result == expected_result

def test_add_documentation_handles_numerical_input():
    # Arrange
    documentation_text = 12345
    expected_result = "Invalid input. Please enter a string."

    # Act
    result = add_documentation(documentation_text)

    # Assert
    assert result == expected_result

def test_add_documentation_handles_special_characters_input():
    # Arrange
    documentation_text = "!@#$%^&*()"
    expected_result = "Documentation added: !@#$%^&*()"

    # Act
    result = add_documentation(documentation_text)

    # Assert
    assert result == expected_result
```