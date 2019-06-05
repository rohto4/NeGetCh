import os
from os.path import expanduser
import pathlib

if __name__ == '__main__':
#     directory = expanduser("~")
    _PROJECT_ROOT = pathlib.Path('../../').resolve()
    print(_PROJECT_ROOT)
    _THUMBNAIL_DIR = pathlib.Path(str(_PROJECT_ROOT) + '/core/imgs/thumbnail/').resolve()
    print(_THUMBNAIL_DIR)
    dir = os.path.dirname(__file__)
    print(dir)
    base = os.path.basename(__file__)
    print(base)
    testdir = pathlib.Path('../../')
    print(testdir)
    print(testdir.resolve())
    