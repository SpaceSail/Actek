from pathlib import Path
import pandas as pd

names = []
xls_books = []


def check_path(file: str):
    """Function for checking does the path/files exists"""
    data = Path(f"{file}")
    if not data.exists():
        print('check address again')
    else:
        counter = 0
        for path in data.glob('*.xlsx'):
            counter += 1
            name = str(path)
            _names = name.replace(file + '/', '').split('.')
            names.append(_names[0])
            xls_books.append(path)
        print(f'{counter} files are detected', names)
    return


def write_to_excel():
    """Function for concatenating to single sheet"""
    frames = ([pd.read_excel(name, header=2).drop('Unnamed: 0', axis=1) for name
               in xls_books])

    out = pd.concat(frames, ignore_index=True)
    out.to_excel('out.xlsx', index=False)
    frames[0].to_excel('out_1.xlsx', sheet_name=names[0], index=False)
    with pd.ExcelWriter('out_1.xlsx',engine='openpyxl', mode='a') as writer:
        for i, df in enumerate(frames[1:]):
            df.to_excel(writer, sheet_name=f'{dict(enumerate(names[1:]))[i]}',
                        index=False)

def separate_sheets():
    """Function for concatenating to a multiple sheets"""
    frames = ([pd.read_excel(name, header=2).drop('Unnamed: 0', axis=1) for name
               in xls_books])

    frames[0].to_excel('out_1.xlsx', sheet_name=names[0], index=False)
    with pd.ExcelWriter('out_1.xlsx',engine='openpyxl', mode='a') as writer:
        for i, df in enumerate(frames[1:]):
            df.to_excel(writer, sheet_name=f'{dict(enumerate(names[1:]))[i]}',
                        index=False)