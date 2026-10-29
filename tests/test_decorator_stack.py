from messages.message import Message
from messages.plain_message import PlainMessage
from messages.urgent_decorator import UrgentDecorator
from messages.timestamp_decorator import TimestampDecorator

def test_stacked_decorators_preserve_message_contract():
    message = PlainMessage("Deploy complete")

    decorated = TimestampDecorator(
        UrgentDecorator(message),
        "2026-10-29 15:00",
    )

    assert isinstance(decorated, Message)

    assert decorated.render() == (
        "[2026-10-29 15:00] [URGENT] Deploy complete"
    )
