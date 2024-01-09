### Hexlet tests and linter status:
[![Actions Status](https://github.com/kirillchistov/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/kirillchistov/python-project-49/actions)

## Step 1: Initialize the package. 
DOD: executable file, printing 'Welcome to the Brain Games!' when launched.
- Pre-requisites: Python3.6+, pip 19+, poetry 1.2.0+
1. Clone git@github.com:kirillchistov/python-project-49.git
2. Initialize hexlet-code with poetry
3. Create /brain-games and /brain-games/scripts
4. Update /pyproject.toml (tool.poetry and tool.poetry.scripts)
5. Create /brain-games/__init__.py and /brain-games/scripts/__init__.py
6. Create /brain-games/scripts/brain_games.py with main function
7. Poetry install the package and test if it works

## Step 2: Prepare to publish the package
DOD: package will represent executable program accessible via 'brain-games' command
1. Add shebang to /brain-games/scripts/brain_games.py
2. Create /Makefile with install, build, publish, package-install commands
3. Build package and debug publication
4. Install the package with make package-install and test brain-games in bash
5. Git push the repository

## Step 3: Work with external library
DOD: Integrate the library to interact with a user (Ask the name and greet).
1. Add prompt library dependency (poetry add prompt)
2. Create brain_games/cli.py with welcome_user function and name prompt (import prompt)
3. Call welcome_user function in brain_games/scripts/brain_games.py
4. Build package
5. Debug publication

## TODO Step 4: Code quality
DOD: Integrade code quality tracking services and linter