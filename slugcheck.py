import re


_SLUG_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*", re.ASCII)


def is_slug(value: str) -> bool:
    """Return whether value is a lowercase ASCII slug with single separators."""
    return isinstance(value, str) and _SLUG_PATTERN.fullmatch(value) is not None
