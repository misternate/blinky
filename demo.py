import link_conditioner
import sys


def main():
    if len(sys.argv) == 2:
        link_conditioner.LinkConditioner(sys.argv[1])
    elif len(sys.argv) == 3:
            link_conditioner.LinkConditioner(sys.argv[1], sys.argv[2])
    else:
        print('Please provide a network profile and duration (optional).')


if __name__ == '__main__':
    main()
