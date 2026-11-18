"""Map cleaned, lowercase words to their lengths."""


def long_cat_is_long(text):
    """Return the length of each unique word in the text."""
    cleaned_words = (
        "".join(character for character in word if character.isalpha())
        for word in text.lower().split()
    )

    return {word: len(word) for word in cleaned_words if word}


if __name__ == "__main__":
    print(long_cat_is_long("A very, very long cat!"))
