# semvercomp
🐍 Semantic Version Comparison for Python

## Development
### Requirements
- [pyenv](https://github.com/pyenv/pyenv)
- [pipenv](https://pipenv.readthedocs.io/en/latest/)
- [Visual Studio Code](https://code.visualstudio.com/) **Recomended**

### Testing
- Running unit tests
```bash
# from repository root directory
python -m unittest tests/<test_file>.py 
```
[More details](https://docs.python.org/3/library/unittest.html#command-line-interface)

- Coverage Report
```bash
# from repository root directory
coverage run semvercomp/<source_file_to_gather_coverage>.py

# report coverage using the CLI
coverage report -m

# report coverage creating HTML file
coverage html
```
[More details](https://coverage.readthedocs.io/en/v4.5.x/cmd.html#)
