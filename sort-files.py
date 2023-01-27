import os

extensions = {('xlsx', 'csv'): 'excels',  ('pdf', 'doc', 'docx',
                                           'txt'): 'documents', ('jpg', 'jpeg', 'png', 'svg'):  'imagenes', ('rar', 'zip'): 'comprimidos', ('py'): 'python-scripts', ('cpp'): 'C scripts', ('pka'): 'redes'}

destiny = 'C:\\Users\\axell\\Desktop\\Ordenado2'

lista = list()


def deal_with_path(path: str, file_name: str, destiny: str):
    extension = file_name.split('.')[-1]

    for exts, new_directory in extensions.items():
        if extension in exts:
            new_path_file = os.path.join(destiny, new_directory)
            if not os.path.exists(new_path_file):
                os.mkdir(new_path_file)
            path_file = os.path.join(path, file_name)
            new_file = os.path.join(new_path_file, file_name)
            try:
                os.rename(path_file, new_file)
                print(f"Renombrando {path_file} como {new_file}")

            except:
                print("Excepción con el archivo", file_name)
            finally:
                break


def sort_directory(source_path: str, destiny_path: str):
    """This function sorts any directory throught creating diferents directorys to separates many extensions"""
    file_list = os.listdir(source_path)

    for file_name in file_list:
        if os.path.isdir(os.path.join(source_path, file_name)):
            new_source_path = os.path.join(source_path, file_name)
            sort_directory(new_source_path, destiny_path)
        else:
            deal_with_path(source_path, file_name, destiny_path)


if __name__ == "__main__":
    sort_directory('C:\\Users\\axell\\Desktop\\Test', destiny)
