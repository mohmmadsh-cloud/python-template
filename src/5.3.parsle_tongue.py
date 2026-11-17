"""Extract hidden messages from a binary file."""

MIN_MESSAGE_LENGTH = 5


def parsle_tongue(file_path):
    """Yield hidden messages containing lowercase letters followed by '!'."""
    with open(file_path, "rb") as binary_file:
        letters = bytearray()

        while (character := binary_file.read(1)):
            if b"a" <= character <= b"z":
                letters.extend(character)
            else:
                if character == b"!" and len(letters) >= MIN_MESSAGE_LENGTH:
                    yield letters.decode("ascii") + "!"
                letters.clear()


def main():
    """Print the hidden messages or report a file access error."""
    try:
        for message in parsle_tongue("resources/logo.jpg"):
            print(message)
    except OSError as error:
        print(f"Could not read the file: {error}")


if __name__ == "__main__":
    main()