"""Calculate the cost of ingredients needed for a recipe."""

GRAMS_PER_PRICE_UNIT = 100


def piece_of_cake(prices, optionals=None, **quantities):
    """Calculate ingredient costs using prices per 100 grams."""
    if optionals is None:
        optionals = []

    return sum(
        price * quantities[ingredient] / GRAMS_PER_PRICE_UNIT
        for ingredient, price in prices.items()
        if ingredient not in optionals
    )


if __name__ == "__main__":
    print(piece_of_cake(
        {"chocolate": 18, "milk": 8},
        chocolate=200,
        milk=100,
    ))

    print(piece_of_cake(
        {"chocolate": 18, "milk": 8},
        optionals=["milk"],
        chocolate=300,
    ))

    print(piece_of_cake({}))
