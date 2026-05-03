import datetime
from functools import wraps
from typing import Any, Callable, Optional

def log(filename: Optional[str] = None) -> Callable:
    """Декоратор, который логирует вызов функции, ее результат или ошибку."""
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                # ВАЖНО: сначала выполняем функцию
                result = func(*args, **kwargs)
                log_message = f"{now} {func.__name__} ok\n"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_message)
                else:
                    print(log_message.strip())
                return result
            except Exception as e:
                # Этот блок у тебя уже почти готов на image_e282df.jpg
                log_message = (
                    f"{now} {func.__name__} error: {type(e).__name__}. "
                    f"Inputs: {args}, {kwargs}\n"
                )
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_message)
                else:
                    print(log_message.strip())
                raise e
        return inner
    return wrapper