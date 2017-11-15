import os


# coz we need to create a directory for every site we scan
def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


print('1___creating directories ...')
