import os
from core.pathdealer import get_files

extensions = {('xlsx', 'csv'): 'excels',  ('pdf', 'doc', 'docx',
                                           'txt'): 'documents', ('jpg', 'jpeg', 'png', 'svg'):  'imagenes', ('rar', 'zip'): 'comprimidos', ('py'): 'python-scripts', ('cpp'): 'C scripts', ('pka'): 'redes'}

destiny = 'C:\\Users\\axell\\Desktop\\Ordenado2'

lista = list()


def deal_with_path(path: str, path_file: str, destiny: str):
    """"This funcdtion deal with a filepath and send it a new directory"""
    """This function should be improved"""
    extension = path_file.split('.')[-1]

    for exts, new_directory in extensions.items():
        if extension in exts:
            nuevo_directorio = os.path.join(destiny, new_directory)
            if not os.path.exists(nuevo_directorio):
                os.mkdir(nuevo_directorio)

            filename = path_file.split("\\")[-1]
            new_file = os.path.join(nuevo_directorio, filename)
            try:
                os.rename(path_file, new_file)
                print(f"Renombrando {path_file} como {new_file}")

            except:
                print("Excepción con el archivo", filename)
            finally:
                break


def sort_directory(base_path, destiny_path="./sorted dir"):
    """This function sorts any directory throught creating diferents directorys to separates many extensions"""
    if not os.path.isdir(destiny_path):
        os.mkdir(destiny_path)
    list_pathfiles = get_files(base_path)
    for filepath in list_pathfiles:
        deal_with_path(base_path, filepath, destiny_path)


if __name__ == "__main__":
    sort_directory('C:\\Users\\axell\\Desktop\\Test', destiny)
