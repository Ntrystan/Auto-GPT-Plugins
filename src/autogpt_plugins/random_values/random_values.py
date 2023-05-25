"""Random Values classes for Autogpt."""

import json
import random
import string
import uuid

import lorem

"""Random Number function for Autogpt."""


def _random_number(min=0, max=65535, count=1) -> str:
    """Return a random integer between min and max
    Args:
        min (int): The lowest number in the range
        max (int): The highest number in the range
        count (int): The number of random numbers to return
    Returns:
        str: a json array with 1 to "count" random numbers in the format
        ["<random_number>"]
    """

    # Type-check the arguments
    if not isinstance(min, int):
        try:
            min = int(min)
        except ValueError:
            raise ValueError("min must be an integer")
    if not isinstance(max, int):
        try:
            max = int(max)
        except ValueError:
            raise ValueError("max must be an integer")
    if not isinstance(count, int):
        try:
            count = int(count)
        except ValueError:
            raise ValueError("count must be an integer")

    # Make values sane
    if not (0 <= min <= 65535):
        raise ValueError("min must be between 0 and 65535")
    if not (0 <= max <= 65535):
        raise ValueError("max must be between 0 and 65535")
    if not (1 <= count <= 65535):
        raise ValueError("count must be between 1 and 65535")

    random_numbers = [random.randint(min, max) for _ in range(count)]
    return json.dumps(random_numbers)


"""Random UUID function for Autogpt."""


def _make_uuids(count=1) -> str:
    """Return a UUID
    Args:
        count (int): The number of UUIDs to return
    Returns:
        str: a json array with 1 to "count" UUIDs
        ["<UUID>"]
    """

    # Type-check the arguments
    if not isinstance(count, int):
        try:
            count = int(count)
        except ValueError:
            raise ValueError("count must be an integer")

    # Make values sane
    if not (1 <= count <= 65535):
        raise ValueError("count must be between 1 and 65535")

    uuids = [str(uuid.uuid4()) for _ in range(count)]
    return json.dumps(uuids)


"""Random String function for Autogpt."""


def _generate_string(length=10, count=1) -> str:
    """Return a random string
    Args:
        length (int): The length of the string
        count (int): The number of strings to return
    Returns:
        str: a json array with 1 to "count" strings of "length" length
        ["<string>"]
    """

    # Type-check the arguments
    if not isinstance(length, int):
        try:
            length = int(length)
        except ValueError:
            raise ValueError("length must be an integer")
    if not isinstance(count, int):
        try:
            count = int(count)
        except ValueError:
            raise ValueError("count must be an integer")

    # Make values sane
    if not (2 <= length <= 65535):
        raise ValueError("length must be between 2 and 65535")
    if not (1 <= count <= 65535):
        raise ValueError("count must be between 1 and 65535")

    strings = [
        "".join(random.choice(string.ascii_letters) for _ in range(length))
        for _ in range(count)
    ]
    return json.dumps(strings)


"""Random Password function for Autogpt."""


def _generate_password(length=16, count=1) -> str:
    """Return a random password of letters, numbers, and punctuation
    Args:
        length (int): The length of the password
        count (int): The number of passwords to return
    Returns:
        str: a json array with 1 to "count" passwords of "length" length
        ["<password>"]
    """

    # Type-check the arguments
    if not isinstance(length, int):
        try:
            length = int(length)
        except ValueError:
            raise ValueError("length must be an integer")
    if not isinstance(count, int):
        try:
            count = int(count)
        except ValueError:
            raise ValueError("count must be an integer")

    # Make values sane
    if not (6 <= length <= 65535):
        raise ValueError("length must be between 6 and 65535")
    if not (1 <= count <= 65535):
        raise ValueError("count must be between 1 and 65535")

    passwords = [
        "".join(
            random.choice(
                string.ascii_letters + string.digits + string.punctuation
            )
            for _ in range(length)
        )
        for _ in range(count)
    ]
    return json.dumps(passwords)


"""Random Lorem Ipsum function for Autogpt."""


def _generate_placeholder_text(sentences=1) -> str:
    """Return a random sentence of lorem ipsum text
    Args:
        sentences (int): The number of strings to return
    Returns:
        str: a json array with 1 to "sentences" strings of lorem ipsum
        ["<string>"]
    """

    # Type-check the arguments
    if not isinstance(sentences, int):
        try:
            sentences = int(sentences)
        except ValueError:
            raise ValueError("sentences must be an integer")

    # Make values sane
    if not (1 <= sentences <= 65535):
        raise ValueError("sentences must be between 1 and 65535")

    strings = [lorem.get_sentence() for _ in range(sentences)]
    return json.dumps(strings)
