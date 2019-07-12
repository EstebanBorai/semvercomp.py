# semvercomp
🐍 Semantic Version Comparison for Python

## Development
### Requirements
- [pyenv](https://github.com/pyenv/pyenv)
- [pipenv](https://pipenv.readthedocs.io/en/latest/)
- [Visual Studio Code](https://code.visualstudio.com/) **Recommended**

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
