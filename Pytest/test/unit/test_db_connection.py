from unittest.mock import patch

from Pytest.src.db_connection import save_user


def test_db_connection():
    with patch("Pytest.src.db_connection.sqlite3.connect") as mock_connect:
        mock_cursor = mock_connect.return_value.cursor.return_value

        save_user(name="John", age=30)

    mock_connect.assert_called_once_with("sqlite:///test.db")
    mock_cursor.execute.assert_called_once_with(
        "INSERT INTO users (name, age) VALUES (?, ?)", ("John", 30)
    )
