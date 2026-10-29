from .message_decorator import MessageDecorator
from .message import Message

class TimestampDecorator(MessageDecorator):
    def __init__(self, message: Message, timestamp: str):
        super().__init__(message)
        self.timestamp = timestamp

    def render(self) -> str:
        return f"[{self.timestamp}] {super().render()}"
