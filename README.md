# Message Decorators — Design Pattern Activity

**Team conformed by:** Braulio Milanés Loza and Oswaldo Oseguera Sandoval

## Overview

This project demonstrates the Decorator Design Pattern
using Python and object-oriented programming.

The objective is to add optional responsibilities to
message objects without modifying their original
implementation.

The implementation follows the Decorator pattern
presented in the "Decorator & Observer" class material.

## Design Pattern: Decorator

The Decorator pattern allows new behavior to be added
to objects dynamically by wrapping them with other
objects that implement the same interface.

This project uses the following components:

- Message: Abstract component that defines render().
- PlainMessage: Concrete component that returns text.
- MessageDecorator: Base decorator that wraps Message.
- UrgentDecorator: Adds an urgency label.
- TimestampDecorator: Adds a timestamp to the message.

Each main class is implemented in a separate source file.

## Project Structure

    src/
      messages/
        __init__.py
        message.py
        plain_message.py
        message_decorator.py
        urgent_decorator.py
        timestamp_decorator.py
      demo.py

    tests/
      test_plain_message.py
      test_decorator_stack.py

    README.md
    requirements.txt
    pyproject.toml

## Requirements

- Python 3
- pytest

## Installation

Clone the repository:

    git clone <YOUR_REPOSITORY_URL>

Open the project folder:

    cd decorator-message-activity

Create a virtual environment on Windows:

    py -m venv .venv

Activate the environment:

    .venv\Scripts\Activate.ps1

Install dependencies:

    python -m pip install --upgrade pip
    pip install -r requirements.txt

## Running the Application

Execute the demonstration:

    python src/demo.py

Expected output:

    Original: Deploy complete
    Decorated: [2026-10-29 15:00] [URGENT] Deploy complete
    Reversed: [URGENT] [2026-10-29 15:00] Deploy complete

The timestamp is injected as a fixed string to ensure
deterministic behavior.

## Running Tests

Execute:

    python -m pytest -q

The tests verify:

1. PlainMessage retains its original behavior.
2. Decorators preserve the Message contract.
3. UrgentDecorator and TimestampDecorator work together.
4. The combined output matches the expected result.

## Why Was PlainMessage Not Modified?

PlainMessage already implements the Message contract.

The Decorator pattern adds responsibilities through
composition rather than changing existing classes.

This follows the Open/Closed Principle:
classes should be open for extension but closed
for modification.

## Does Decorator Order Matter?

Yes, decorator order matters because each decorator
transforms the result of the wrapped object.

Example 1:

    TimestampDecorator(
        UrgentDecorator(PlainMessage("Deploy complete")),
        "2026-10-29 15:00"
    )

Output:

    [2026-10-29 15:00] [URGENT] Deploy complete

Example 2:

    UrgentDecorator(
        TimestampDecorator(
            PlainMessage("Deploy complete"),
            "2026-10-29 15:00"
        )
    )

Output:

    [URGENT] [2026-10-29 15:00] Deploy complete

The outer decorator applies its transformation
to the rendered result of the inner decorator.

Therefore, changing the order changes the output.

## Complexity Cost

One complexity cost introduced by the Decorator pattern
is the creation of additional wrapper objects.

As more decorators are stacked, it can become harder
to trace the order of execution and debug behavior.

However, decorators provide flexibility and reduce
the need to create subclasses for every combination
of features.

## Design Decisions

- PlainMessage remains unchanged.
- Message.render() remains the stable contract.
- MessageDecorator inherits from Message.
- Each decorator wraps another Message object.
- Each concrete decorator has one responsibility.
- Decorators can be combined dynamically.
- A fixed timestamp ensures repeatable tests.
- One main class is used per source file.

## Conclusion

The Decorator pattern successfully extends the behavior
of Message objects without modifying PlainMessage.

UrgentDecorator and TimestampDecorator can be stacked
in different orders while preserving the original
Message interface.

This implementation demonstrates composition,
flexibility, and separation of responsibilities.
