import argparse


def cli_arg_parser():
    parser = argparse.ArgumentParser(description="Generate diff")

    # Positional arguments
    parser.add_argument("first_file")
    parser.add_argument("second_file")

    # Optional arguments
    parser.add_argument("-f", "--format",
                        help="set format of output",
                        default="stylish")

    args = parser.parse_args()
    filepath1, filepath2 = args.first_file, args.second_file
    output_format = args.format

    return filepath1, filepath2, output_format
