"""Decode a message stored in black-pixel positions."""

from PIL import Image

BLACK = (1, 1, 1)


def remember_remember(file_path):
    """
    Decode characters from black-pixel row positions, left to right.

    :param file_path: Path to the encoded image.
    :return: Decoded message.
    :raises ValueError: If a column has no black pixel.
    """
    characters = []

    with Image.open(file_path) as source_image:
        with source_image.convert("RGB") as image:
            width, height = image.size

            for column in range(width):
                for row in range(height):
                    if image.getpixel((column, row)) == BLACK:
                        characters.append(chr(row))
                        break
                else:
                    raise ValueError(
                        f"No black pixel found in column {column}."
                    )

    return "".join(characters)


def main():
    """Print the decoded message or a helpful error."""
    try:
        print(remember_remember("resources/code.png"))
    except (OSError, ValueError) as error:
        print(f"Could not decode the image: {error}")


if __name__ == "__main__":
    main()
