import re
import unicodedata


def slugify(text: str) -> str:
    """Convert text to a lowercase ASCII slug separated by hyphens."""
    text = unicodedata.normalize("NFKD", text)
    text = "".join(char for char in text if not unicodedata.combining(char))
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
