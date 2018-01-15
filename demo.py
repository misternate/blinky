import link_conditioner
import sys


def main():
    if len(sys.argv) > 1:
        link_conditioner.LinkConditioner(sys.argv[1])
    else:
        print('Please provide a profile (100% Loss, Edge, 3G, etc.)')


if __name__ == '__main__':
    main()
