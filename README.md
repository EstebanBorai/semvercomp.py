# semvercomp
🐍 Semantic Version Comparison for Python

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
