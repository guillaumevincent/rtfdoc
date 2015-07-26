import sys

from rtfdoc import cmdline


def main(argv=sys.argv):
    sys.exit(build_main(argv))


def build_main(argv):
    if sys.version_info[:3] < (2, 6, 0) or (3, 0, 0) <= sys.version_info[:3] < (3, 3, 0):
        sys.stderr.write('Error: rftdoc requires at least Python 2.6 to run.\n')
        return 1
    return cmdline.main(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
