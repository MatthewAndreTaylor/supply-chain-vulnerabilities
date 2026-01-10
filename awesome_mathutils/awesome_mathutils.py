
def is_arithmetic_progression(seq):
    """
    Returns True if seq is an arithmetic progression, otherwise False.
    """
    return len(seq) < 2 or all(
        seq[i] - seq[i - 1] == seq[1] - seq[0]
        for i in range(2, len(seq))
    )

def has_arithmetic_progression(seq):
    """
    Returns True if seq contains an arithmetic progression, otherwise False.
    """
    return is_arithmetic_progression(sorted(seq))