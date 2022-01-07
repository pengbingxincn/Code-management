import glob
import os
from pathlib import Path
IMG_FORMATS = ['bmp', 'jpg', 'jpeg', 'png', 'tif', 'tiff', 'dng', 'webp', 'mpo']
def image_read(path):
    path = path
    f = []  # image files
    for p in path if isinstance(path, list) else [path]:
        p = Path(p)
        if p.is_dir():  # dir
            f += glob.glob(str(p / '**' / '*.*'), recursive=True)
        elif p.is_file():  # file
            with open(p) as t:
                t = t.read().strip().splitlines()
                parent = str(p.parent) + os.sep
                f += [x.replace('./', parent) if x.startswith('./') else x for x in t]  # local to global path
        else:
            print(f' does not exist')
    img_files = sorted(x.replace('/', os.sep) for x in f if x.split('.')[-1].lower() in IMG_FORMATS)
    return img_files

def img2label_paths(img_paths):
    # Define label paths as a function of image paths
    sa, sb = os.sep + 'images' + os.sep, os.sep + 'labels' + os.sep  # /images/, /labels/ substrings
    return [sb.join(x.rsplit(sa, 1)).rsplit('.', 1)[0] + '.txt' for x in img_paths]

if __name__ == '__main__':
    path = ["data/images/ants"]
    # path = "data/classes.csv"
    # for p in path if isinstance(path, list) else [path]:
    #     image_read(path)
    #     print(image_read(path))
    label_files = img2label_paths(image_read(path))  # labels
    print(label_files)

