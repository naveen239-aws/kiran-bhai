#!/usr/bin/env python3

"""Simple hello world script."""


def write_message(filename: str, message: str) -> None:
    """Write a message to a file specified by *filename*.

    Args:
        filename: Path to the file to write.
        message: The text to write into the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(message)


def main():
    print("Hello, world!")
    print("Hello, world123")
    print("Hello, kiran1234")

    # demonstrate write_message
    write_message("output.txt", "This is a message written by write_message()\n")
    print("Message written to output.txt")




if __name__ == "__main__":
    main()
