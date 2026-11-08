import re


def slugify(text: str) -> str:
    """Convert text to a lowercase ASCII slug separated by hyphens."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
