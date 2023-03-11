import os


def get_files(base_path: str, files_paths=[]) -> list[str]:
    paths = os.listdir(base_path)

    for path in paths:
        new_path = os.path.join(base_path, path)
        if os.path.isdir(new_path):
            get_files(new_path, files_paths)
        elif os.path.isfile(new_path):
            files_paths.append(new_path)
    return files_paths
