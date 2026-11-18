"""Generate interleaved items from multiple iterables."""


def generator_interleaves(*iterables):
    """
    Yield items from the inputs in alternating order.
    Stop when the shortest input is exhausted.
    """
    for group in zip(*iterables):
        for item in group:
            yield item


if __name__ == "__main__":
    print(list(generator_interleaves(
        "abc", [1, 2, 3], ("!", "@", "#")
    )))
