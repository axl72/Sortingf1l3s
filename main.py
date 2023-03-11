import argparse
from core.sortfiles import sort_directory

parser = argparse.ArgumentParser()
parser.add_argument("basepath")
parser.add_argument("-d", "--destinypath", default="./sorted directory")

if __name__ == "__main__":
    argumentos = parser.parse_args()
    base_path = argumentos.basepath
    destinitypath = argumentos.destinypath
    sort_directory(base_path, destinitypath)
