def truncate_slug(slug: str, max_len: int) -> str:
    if max_len <= 0:
        return ""

    if len(slug) < max_len:
        return slug

    hyphen = slug.rfind("-", 0, max_len + 1)
    if hyphen != -1:
        return slug[:hyphen]

    return slug[:max_len]
