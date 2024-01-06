from enum import Enum
from openai import RateLimitError
from json import JSONDecodeError


class ExceptionType(Enum):
    RATE_LIMIT_ERROR = RateLimitError
    JSON_DECODE_ERROR = JSONDecodeError


class CustomExceptionHandler(Exception):
    def __init__(self, exception_type: Exception, message: str):
        self.exception_type = exception_type
        self.message = message
        super().__init__(self.message)

    def handle(self):
        print(f"Exception Occurred: {self.message}")
        if self.exception_type == ExceptionType.RATE_LIMIT_ERROR:
            self.handle_rate_limit_error()
        elif self.exception_type == ExceptionType.JSON_DECODE_ERROR:
            self.handle_json_decode_error()

    def handle_rate_limit_error(self):
        print(f"Handling {str(ExceptionType.RATE_LIMIT_ERROR)}: {self.message}")

    def handle_json_decode_error(self):
        print(f"Handling {ExceptionType.JSON_DECODE_ERROR}: {self.message}")
