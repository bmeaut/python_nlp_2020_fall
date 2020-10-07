import sys


def diff():
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]

    with open(filename1) as f1, open(filename2) as f2:
        z = zip(f1, f2)
        # This would load both files into memory:
        # for line1, line2 in list(zip(f1, f2)):
        for line1, line2 in zip(f1, f2):
            if line1 != line2:
                print(f"{filename1} and {filename2} are different.")
                input("Input somethint to end the program.")
                return
        print(f"{filename1} and {filename2} are the same.")
        input("Input somethint to end the program.")


if __name__ == '__main__':
    diff()
