import os
import shutil

def copier(src, dest):
    exists = os.path.exists(dest)
    if exists:
        shutil.rmtree(dest)
    os.mkdir(dest)
    files = os.listdir(src)
    for file in files:
        if os.path.isdir(os.path.join(src, file)):
            copier(os.path.join(src, file), os.path.join(dest, file))
        else:
            shutil.copy(os.path.join(src, file), os.path.join(dest, file))
    return
