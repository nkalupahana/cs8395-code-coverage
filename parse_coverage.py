# open coverage file at functions/one/coverage.json

import json
import os
from pathlib import Path
import os
import xml.etree.ElementTree as ET
import statistics

files = {}
coverage_data = {}
with open("functions/one/coverage.json") as f:
    fl = json.load(f)["files"]
    for file in fl:
        files[os.path.join("one", file)] = fl[file]

with open("functions/two/coverage.json") as f:
    fl = json.load(f)["files"]
    for file in fl:
        files[os.path.join("two", file)] = fl[file]

for file in files:
    if "__init__" in file or "test_" in file:
        continue

    path_obj = Path(file)
    if path_obj.parent not in coverage_data:
        coverage_data[path_obj.parent] = (0, 0)

    coverage_data[path_obj.parent] = (
        coverage_data[path_obj.parent][0] + files[file]["summary"]["covered_lines"],
        coverage_data[path_obj.parent][1] + files[file]["summary"]["num_statements"],
    )

all_data = {}

for path in coverage_data:
    all_data[f"cov/{path}"] = coverage_data[path][0] / coverage_data[path][1]

test_success_data = {}
tree = ET.parse("functions/one/output.xml")
for testcase in tree.findall(".//testcase"):
    classname = testcase.attrib["classname"]
    classname = classname.replace("test_", "")
    classname = "one/" + "/".join(classname.split(".")[:2])
    
    if classname not in test_success_data:
        test_success_data[classname] = (0, 0)
    
    test_success_data[classname] = (
        test_success_data[classname][0] + (1 if testcase.find("failure") is None else 0),
        test_success_data[classname][1] + 1
    )

tree = ET.parse("functions/two/output.xml")
for testcase in tree.findall(".//testcase"):
    classname = testcase.attrib["classname"]
    classname = classname.replace("test_", "")
    classname = "two/" + "/".join(classname.split(".")[:2])
    
    if classname not in test_success_data:
        test_success_data[classname] = (0, 0)
    
    test_success_data[classname] = (
        test_success_data[classname][0] + (1 if testcase.find("failure") is None else 0),
        test_success_data[classname][1] + 1
    )

for path in test_success_data:
    all_data[f"success/{path}"] = test_success_data[path][0] / test_success_data[path][1]

all_data["output"] = statistics.mean(all_data.values())
json.dump(all_data, open("output.json", "w"))