import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Pure-python command-line calculator.')
    parser.add_argument('expression', type=str, help='expression string to evaluate')
    args = parser.parse_args()
    return args.expression
