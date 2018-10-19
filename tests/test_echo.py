import unittest
import argparse
import subprocess

from echo import *


class echo_tests(unittest.TestCase):

    def test_help(self):
        """ Running the program without arguments should show usage. """
        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        print('stdout type is', type(stdout))
        s = stdout.decode('utf-8')
        print('s type is', type(s), len(s))
        print('The s string is', s)
        usage = open("./USAGE", "r").read()
        print('usage type is', type(usage), len(usage))
        self.assertEqual(s, usage)

    def test_echo_upper(self):
        """ Running should uppercase a string """
        parser1 = parse_args(['-u', 'corgi'])
        parser2 = parse_args(['--upper', 'corgi'])
        self.assertTrue(parser1.upper)
        self.assertTrue(parser2.upper)
        self.assertEqual(echo_upper("hello"), "HELLO")

    def test_echo_lower(self):
        """ Running should lowercase a string """
        parser1 = parse_args(['-l', 'corgi'])
        parser2 = parse_args(['--lower', 'corgi'])
        self.assertTrue(parser1.lower)
        self.assertTrue(parser2.lower)
        self.assertEqual(echo_lower("Hello"), "hello")

    def test_echo_title(self):
        """ Running should capitalize the first letter
        of every word in a string """
        parser1 = parse_args(['-t', 'corgi'])
        parser2 = parse_args(['--title', 'corgi'])
        self.assertTrue(parser1.title)
        self.assertTrue(parser2.title)
        self.assertEqual(echo_title("hello"), "Hello")
