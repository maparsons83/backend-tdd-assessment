import sys
import argparse


def echo_upper(text):
    return text.upper()


def echo_lower(text):
    return text.lower()


def echo_title(text):
    return text.title()


def parse_args(args):
    parser = argparse.ArgumentParser(
        description='Perform transformation on input text.')
    parser.add_argument('-u', '--upper',
                        help='convert text to uppercase', action='store_true')
    parser.add_argument('-l', '--lower',
                        help='convert text to lowercase', action='store_true')
    parser.add_argument('-t', '--title',
                        help='convert text to titlecase', action='store_true')
    parser.add_argument('text', help='text to be manipulated')

    return parser.parse_args(args)


def main():
    text = parse_args(sys.argv[1:])
    upper = text.upper
    lower = text.lower
    title = text.title

    if upper:
        print(echo_upper(text))
    if lower:
        print(echo_lower(text))
    if title:
        print(echo_title(text))


if __name__ == "__main__":
    main()
