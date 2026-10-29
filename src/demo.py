from messages.plain_message import PlainMessage
from messages.urgent_decorator import UrgentDecorator
from messages.timestamp_decorator import TimestampDecorator


message = PlainMessage("Deploy complete")

# First combination: Timestamp outside, Urgent inside
decorated = TimestampDecorator(
    UrgentDecorator(message),
    "2026-10-29 15:00",
)

print("Original:", message.render())
print("Decorated:", decorated.render())

# Second combination: Reverse the order
reversed_order = UrgentDecorator(
    TimestampDecorator(message, "2026-10-29 15:00")
)

print("Reversed:", reversed_order.render())
