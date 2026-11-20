# PyPI Upload Guide for scriber-core

This repository is now ready for publication on PyPI. Follow these steps to upload your package.

## Prerequisites

- Python 3.10+ with `uv` package manager
- A PyPI account (create at https://pypi.org/account/register/)
- A PyPI API token (generate at https://pypi.org/manage/account/token/)

## Step 1: Build the Package

```bash
uv pip install build
python -m build
```

This creates two files in the `dist/` directory:
- `scriber_core-1.0.0.tar.gz` (source distribution)
- `scriber_core-1.0.0-py3-none-any.whl` (wheel)

## Step 2: Configure PyPI Credentials

The `.pypirc` file has been created for you. Add your API token:

```ini
[pypi]
username = __token__
password = pypi-YOUR_API_TOKEN_HERE
```

**Note:** `.pypirc` is in `.gitignore` to prevent credential leaks.

## Step 3: Test Upload (Optional)

Upload to TestPyPI first to verify everything works:

```bash
uv pip install twine
twine upload --repository testpypi dist/*
```

Check at https://test.pypi.org/project/scriber-core/

## Step 4: Upload to PyPI

```bash
twine upload dist/*
```

Check at https://pypi.org/project/scriber-core/

## Step 5: Verify Installation

```bash
pip install scriber-core
eigenscribe --version
```

## Updating the Version

Before each release:

1. Update `version` in `pyproject.toml`
2. Update `__version__` in `src/frontend/__init__.py`
3. Update `CLI_VERSION` in `src/cli/main.py`
4. Update `CHANGELOG.md`
5. Build and upload

## Notes

- The package name on PyPI will be `scriber-core`
- The import names are `frontend` and `cli`
- The CLI command is `eigenscribe`
