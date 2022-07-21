### Hexlet tests and linter status:
[![Actions Status](https://github.com/VasiliyBogdanov/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/VasiliyBogdanov/python-project-lvl2/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/6ff1868af3e92f0dd252/maintainability)](https://codeclimate.com/github/VasiliyBogdanov/python-project-lvl2/maintainability)
[![flake8](https://github.com/VasiliyBogdanov/python-project-lvl2/actions/workflows/flake8.yml/badge.svg)](https://github.com/VasiliyBogdanov/python-project-lvl2/actions/workflows/flake8.yml)
[![Test Coverage](https://api.codeclimate.com/v1/badges/6ff1868af3e92f0dd252/test_coverage)](https://codeclimate.com/github/VasiliyBogdanov/python-project-lvl2/test_coverage)
### Description:
This is the 2nd project in Hexlet's 'Python developer' course, 'gendiff', library and CLI for comparing two json or yaml files.
Have three output formats, works with nested structures.
### Requirements: 
- Python ^3.8;
- poetry;
### Installation:
```
pip install git+https://github.com/VasiliyBogdanov/python-project-lvl2.git
```
or:
- Clone this repo;
- If you have 'make' utility:
```
make install
make build
make publish
make package-install
```
- If you don't:
    - get one 🧐  
or:
```
poetry install
poetry build
poetry publish --dry-run
python3 -m pip install --user dist/*.whl
```
### Usage:
CLI
```
gendiff filepath1 filepath2 --format
```
Function
```
some_var = generate_diff(filepath_a, filepath_b, format_='stylish')
```
'format' argument can be 'stylish', 'plain' or 'json'
## Demo:
### Plain JSON
[![asciicast](https://asciinema.org/a/0lnFLtjxwiUARhaZerb0zFOdV.svg)](https://asciinema.org/a/0lnFLtjxwiUARhaZerb0zFOdV)
### Plain YAML
[![asciicast](https://asciinema.org/a/l3th2SqDS1cvC164cStZhKem4.svg)](https://asciinema.org/a/l3th2SqDS1cvC164cStZhKem4)
### Nested JSON "Stylish" format
[![asciicast](https://asciinema.org/a/gAcNJPgXBchj9EYqBEcVX2CQp.svg)](https://asciinema.org/a/gAcNJPgXBchj9EYqBEcVX2CQp)
### Nested JSON "Plain" format
[![asciicast](https://asciinema.org/a/fDs1z48oD6YperOtJrUDPI8ut.svg)](https://asciinema.org/a/fDs1z48oD6YperOtJrUDPI8ut)
### Nested JSON "JSON" format
[![asciicast](https://asciinema.org/a/sIH1aEfRI0jOpeJZAgIdIsI2R.svg)](https://asciinema.org/a/sIH1aEfRI0jOpeJZAgIdIsI2R)
