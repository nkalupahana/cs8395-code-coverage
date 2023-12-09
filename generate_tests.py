from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from pathlib import Path
from tqdm import tqdm

import argparse
import glob
import itertools
import json
import os.path
import sys

from llm_test_helpers import get_llm, get_args
args = get_args(sys.argv)
llm = get_llm(args.model)

# Test generation prompt
raw_prompt = json.loads(open("config.json").read())["prompt"]
prompt = PromptTemplate.from_template(raw_prompt)

for function in tqdm(glob.glob("functions/*/*/*/*.py")):
    if "test_" in function:
        continue

    path_obj = Path(function)
    test_folder = path_obj.parent.parent / f"test_{path_obj.parent.stem}"
    if not test_folder.exists():
        test_folder.mkdir(parents=True, exist_ok=True)

    test_path = test_folder / f"test_{path_obj.stem}.py"
    if test_path.exists():
        print(f"Skipping {function}, test already exists.")
        continue

    test_init_path = test_folder / "__init__.py"
    if not test_init_path.exists():
        test_init_path.touch()

    init_path = path_obj.parent / "__init__.py"
    if not init_path.exists():
        init_path.touch()

    # Get code and create prompt
    with open(function) as f:
        code = f.read()
    code_prompt = prompt.format(code=code)
    
    # Generate tests and clean up output
    output = llm.predict(code_prompt)
    output = output.replace("```python", "").replace("```py", "").replace("```", "").strip()
    output = f"from ..{path_obj.parent.stem}.{path_obj.stem} import {path_obj.stem}\n\n" + output

    # Write out final code
    with open(test_path, "w") as f:
        f.write(output)