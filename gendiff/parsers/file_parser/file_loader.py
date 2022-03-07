import os


def read_file(filepath):
    with open(filepath) as f:
        data = f.read()
        _, extension = os.path.splitext(f.name)
        return data, normalize_extension(extension)


def normalize_extension(file_extension: str):
    normalized_extension = file_extension.lower()
    return normalized_extension
