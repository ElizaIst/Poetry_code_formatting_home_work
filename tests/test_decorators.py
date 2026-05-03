from pathlib import Path

from typing import Any
import pytest
from src.decorators import log

@log()
def add(x: int, y: int) -> int:
    return x + y
@log()
def divide(x: int, y: int) -> float:
    return x / y

def test_log_console_success(capsys: Any) -> None:
    """Тест успешного выполнения с выводом в консоль."""
    add(1, 2)
    captured = capsys.readouterr()
    assert "add ok" in captured.out

def test_log_console_error(capsys: Any) -> None:
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError" in captured.out

def test_log_file_success(tmp_path: Path) -> None:
    """Тест записи лога в файл."""
    temp_file = tmp_path / "test.log"

    @log(filename=str(temp_file))
    def mult(x: int, y: int) -> int:
        return x * y

    mult(3, 4)
    with open(str(temp_file), "r") as f:
        content = f.read()
    assert "mult ok" in content