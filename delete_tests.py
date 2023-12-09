from pathlib import Path
import glob

for function in glob.glob("functions/*/*/*/*.py"):
    print(function)
    path_obj = Path(function)
    filename = path_obj.stem
    test_path = path_obj.parent / f"test_{filename}.py"

    if test_path.exists():
        test_path.unlink()