"""Group items according to the result of a function."""


def group_by(function, iterable):
    """ Group items using the supplied function to calculate their keys."""
    groups = {}

    for item in iterable:
        key = function(item)
        groups.setdefault(key, []).append(item)

    return groups


if __name__ == "__main__":
    print(group_by(len, ["hi", "bye", "yo", "try"]))
