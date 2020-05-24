"""Console script for example_package."""
import argparse
import sys

from example_package import example_package as E


def main():
    """Console script for example_package."""
    parser = argparse.ArgumentParser()
    parser.add_argument('nums', nargs='+', type=int)
    args = parser.parse_args()

    for n in args.nums:
        print(E.prime(n), file=sys.stdout)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
