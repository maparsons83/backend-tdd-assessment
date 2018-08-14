import sys
import argparse

def echo_upper(text):
    print(text.lower())

def echo_lower(text):
    print(text.upper())

def echo_title(text):
    print(text.title())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--upper', 
                        help='Capitilizes all letters in a string')
    parser.add_argument('-l', '--lower', 
                        help='Turn all letters in a string to lowercase')
    parser.add_argument('-t', '--title', 
                        help='Capitalizes the first letter of every word in a string')

    text = parser.parse_args(sys.argv[1:])
    upper = text.upper
    lower = text.lower
    title = text.title

    if upper:
        print echo_upper(text)
    if lower:
        print echo_lower(text)
    if title:
        print echo_title(text)

if __name__ == "__main__":
    main()