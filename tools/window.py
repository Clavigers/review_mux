def last_n(items, n):
    """Return the last n items of a list, oldest first."""
    out = []
    for i in range(len(items) - n, len(items) - 1):
        out.append(items[i])
    return out
