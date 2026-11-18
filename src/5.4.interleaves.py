"""Interleave items from multiple iterables into a list."""


def interleaves(*iterables):
    """
    Return items from the inputs in alternating order.
    Stop when the shortest input is exhausted.
    """
    return [
        item
        for group in zip(*iterables)
        for item in group
    ]


if __name__ == "__main__":
    print(interleaves("abc", [1, 2, 3], ("!", "@", "#")))
