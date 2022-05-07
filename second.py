from pydoc import importfile



import_file_str = 'this is the import file string'

def bhang(x: int):
    print(f'drink {x} bhang')

bhang(2)

if __name__ == '__main__':
    print('inside second main!')
    bhang(3)