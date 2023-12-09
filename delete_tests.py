from pathlib import Path
import glob
import shutil

for function in glob.glob("functions/*/*/*"):
    path_obj = Path(function)
    if "test_" in path_obj.stem:
        # delete folder and all contents in one function call
        shutil.rmtree(path_obj)