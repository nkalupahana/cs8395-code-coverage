#!/bin/bash
cd functions/one
pytest --cov=. --junitxml=output.xml
coverage json
cd ../two
pytest --cov=. --junitxml=output.xml
coverage json
cd ../../
python3 parse_coverage.py