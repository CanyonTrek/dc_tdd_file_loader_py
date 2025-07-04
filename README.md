# TDD File Loader (Python Version)

This project is a Python adaptation of a Java-based TDD walkthrough. It shows how to progressively build a file loading utility using Test-Driven Development (TDD), with Git tags marking key milestones in the development process.

## Project Structure

```
tdd_file_loader/
├── app/
│   └── file_loader.py          # File loading logic
├── tests/
│   └── test_file_loader.py     # Unit tests
└── main.py                     # Entry point for testing the module
```

## Git Tags and Milestones

| Tag | Description |
|-----|-------------|
| `start_here` | Project scaffold with folders and empty files |
| `v1.0-code_in_main-read_text_file` | File reading logic added directly in `main.py` |
| `v1.2-file_loading_in_its_own_class` | Created `FileLoader` class in its own module |
| `v1.3-moved_file_loading_into_function` | Refactored file loading logic into a function |
| `v1.4` (same as `main`) | Final clean version with full test coverage |

## Differences from the Java Project

- Removed Java-specific structures like interfaces and packages
- Uses Python’s `unittest` and `unittest.mock` instead of JUnit/Mockito
- Relies on duck typing instead of interface implementation
- Uses simple modules and folder-based structure
- Code is simplified using Python idioms like `with open(...)` and list comprehensions

## Running the Application

```bash
python main.py
```

## Running the Tests

```bash
python -m unittest discover -s tests
```

## Summary

Each Git tag marks a meaningful step in the TDD process, evolving from a simple script to a modular and testable file loader.

