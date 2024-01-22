import os


def get_absolute_path(path):
    *_, extension = os.path.splitext(path)
    path_to, _ = os.path.split(path)
    file_name = os.path.basename(path).split('.')[0]
    
    return path_to, file_name, extension


if __name__ == '__main__':
    path = '/Users/jshuckbot/projects/geekbrains/Ivan511440/Seminar_5/ivan.txt'
    print(get_absolute_path(path))