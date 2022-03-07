#!/usr/bin/env python3
from gendiff.parsers.cli_parser import cli_arg_parser
from gendiff.generate_diff import generate_diff


def main():
    filepath1, filepath2, output_format = cli_arg_parser()
    print(generate_diff(filepath1, filepath2, output_format))


if __name__ == '__main__':
    main()
