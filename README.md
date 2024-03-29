# semvercomp
🐍 Semantic Version Comparison for Python

Implementation of a `Version` object with comparison capabilities and tag validation following [semver](https://semver.org/) conventions.

## Installation
```bash
pip install semvercomp
```

## Usage
- [Classes](https://github.com/estebanborai/semvercomp#classes)
	- [Version](https://github.com/estebanborai/semvercomp#versionmajor0--int-minor0--int-patch0--int-pre_release--str-patch--str-has_vfalse--str)
- [Comparison of Version Objects](https://github.com/estebanborai/semvercomp#comparison-of-version-objects)
	- [Equal](https://github.com/estebanborai/semvercomp#equal)
	- [Greater](https://github.com/estebanborai/semvercomp#greater)
	- [Lower](https://github.com/estebanborai/semvercomp#lower)
- [Validation](https://github.com/estebanborai/semvercomp#validation)
	- [validate_version](https://github.com/estebanborai/semvercomp#validate_versionversion-str-parts-dict-is_ok-bool)
- [Utils](https://github.com/estebanborai/semvercomp#utils)
	- [to_version_list](https://github.com/estebanborai/semvercomp#to_version_listcoll-iterable-version)

### Classes
#### `Version(major=0 : int, minor=0 : int, patch=0 : int, pre_release="" : str, patch="" : str, has_v=False : str)`

Class `Version` represents a version tag following *semver* conventions.
A version tag is structured the following way:
```
X.Y.Z-pre+build
```

Value | Name | Description
------------ | ------------- | -------------
`X` | `Major` | Version when you make incompatible API changes
`Y` | `Minor` | Version when you add functionality in a backwards-compatible manner
`Z` | `Patch` | Version when you make backwards-compatible bug fixes
`pre` | `Pre Release` | Version *pre-release* tag
`build` | `Build` | Version *build* tag

Source: [Semantic Versioning 2.0.0](https://semver.org/)

- Public Properties

Key | Value | Type
------------ | ------------- | -------------
`has_v` | `bool` | Flag for preceding `v` or `V` in version tag
`major` | `int` | Major member
`minor` | `int` | Minor member
`patch` | `int` | Patch member
`pre_release` | `str` | Pre Release member
`build` | `str` | Build member

- Instance of Version

```python
from semvercomp.Version import Version

ver = Version(1, 0, 0, 'beta', '20191224')
print(str(ver))
# 1.0.0-beta+20191224
```

- Creating a Version object from a version string:

```python
from semvercomp.Version import Version

str_v = Version()
str_v.parse_version_number('v1.0.0-beta')
# str_v.major == 1
# str_v.minor == 0
# str_v.patch == 0
# str_v.has_v == True
# str_v.pre_release == 'beta'
```

### Comparison of Version Objects
`Version` class implements `__gt__`, `__lt__` and `__eq__` built-in methods to implement comparison.
#### Equal
```python
from semvercomp.Version import Version

a = Version(1, 0, 0)
b = Version(1, 0, 0)
print(a == b) # True
```

#### Greater
```python
from semvercomp.Version import Version

a = Version(1, 1, 0)
b = Version(1, 0, 0)
print(a > b) # True
```

#### Lower
```python
from semvercomp.Version import Version

a = Version(0, 1, 0)
b = Version(1, 0, 0)
print(a < b) # True
```

### Validation
It is possible to validate and gather the different members of a version tag using `validate version` from `semvercomp.validators`.

#### `validate_version(version: str): (parts: dict(), is_ok: bool)`
Will return a tuple where, the first element is a dictionary with the properties of the given version tag destructured.

The second element in the tuple is a boolean flag that stands as the validation result.

```python
from semvercomp.validators import validate_version

ver_str = 'v1.0.22'
(parts, is_ok) = validate_version(ver_str)
print(parts) # {'has_v': True, 'major': 1, 'minor': 0, 'patch': 22, 'pre_release': None, 'build': None}
print(is_ok) # True
```

### Utils
#### `to_version_list(coll: iterable): Version[]`
Create an array of Version objects from an iterable of version tags as strings.

```python
from semvercomp.utils import to_version_list

all = [
	'1.0.0-beta',
	'0.1.0+1234',
	'33.22.3'
]

versions = to_version_list(all)
```

## Development
### Requirements
- [pyenv](https://github.com/pyenv/pyenv)
- [pipenv](https://pipenv.readthedocs.io/en/latest/)
- [Visual Studio Code](https://code.visualstudio.com/) **Recommended**

### Debugging
- Debugging tests
Tests for this package are written with `pytest`.
The following json, is an example of the `.vscode/settings.json`:
```json
{
	"python.pythonPath": /* Your Python Binary Address*/,
	"python.testing.pytestArgs": [
		"tests"
	],
	"python.testing.unittestEnabled": false,
	"python.testing.nosetestsEnabled": false,
	"python.testing.pytestEnabled": true
}
```

### Testing
- Running unit tests
```bash
# from repository root directory
pytest
```

- Running test coverage
```bash
# from repository root directory
pytest --cov=semvercomp tests/

# or with html report
pytest --cov-report html --cov=semvercomp tests/
```
