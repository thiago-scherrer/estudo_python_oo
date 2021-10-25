import argparse
import prompter
import saver


def entrypoint():
    parser = argparse.ArgumentParser(
        prog='agenda', description='Simple agenda tool')
    parser.add_argument('--rm', nargs='?', help='Remove contact')
    args = parser.parse_args()

    saver.Agenda().header_check()

    if args.rm:
        print("rm ...")
    else:
        prompter.Input().add_contact()


if __name__ == '__main__':
    entrypoint()
