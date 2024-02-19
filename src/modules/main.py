import pathlib

from modules import *


def main():
    try:
        file = str(input('Define path to .xlsx: '))
        check_path(file)
        write_to_excel()
        separate_sheets()
    except Exception as e:
        print(e)
    finally:
        print(f'files placed here: {pathlib.Path.cwd()}')


if __name__ == "__main__":
    main()

