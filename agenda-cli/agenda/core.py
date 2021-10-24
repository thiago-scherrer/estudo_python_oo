import argparse
import saver

def entrypoint():
    parser = argparse.ArgumentParser(
        prog='agenda', description='Simple agenda tool')
    parser.add_argument('--add', nargs='?', help='Add new contact')
    parser.add_argument('--rm', nargs='?', help='Remove contact')
    args = parser.parse_args()

    saver.Agenda().header_check()

    if args.add:
        print("42")
    elif args.rm:
        print("4242")
    else:
        parser.print_help()


if __name__ == '__main__':
    entrypoint()
