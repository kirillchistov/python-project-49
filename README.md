### Hexlet tests and linter status:
[![Actions Status](https://github.com/kirillchistov/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/kirillchistov/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/d922981a966fe718675c/maintainability)](https://codeclimate.com/github/kirillchistov/python-project-49/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/d922981a966fe718675c/test_coverage)](https://codeclimate.com/github/kirillchistov/python-project-49/test_coverage)
[![asciicast](https://asciinema.org/a/IFei1plp3YOf1V7D1XAhq2Ztm.svg)](https://asciinema.org/a/IFei1plp3YOf1V7D1XAhq2Ztm)

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

## Step 4: Code quality
DOD: Integrade code quality tracking services and linter
1. Register with CodeQuality (Quality branch)
2. Connect the repo and add [![Maintainability](https://api.codeclimate.com/v1/badges/d922981a966fe718675c/maintainability)](https://codeclimate.com/github/kirillchistov/python-project-49/maintainability) badge
3. Add flake8 dependency (poetry add --group dev flake8)
4. Add setup.cfg from the [hexlet boilerplate](https://github.com/hexlet-boilerplates/python-package/blob/main/setup.cfg) and check if 'poetry run flake8 brain_games' works
5. Add Make lint command to launch poetry run flake8 brain_games and correct all linter errors

## TODO Step 5: "Even check"
DOD: the program will prompt the user to answer 'yes' to even, 'no' to odd numbers, print results
1. Add brain_games/scripts/brain_even.py with the game logic
2. Don't touch the previously added brain_games/cli.py, brain_games/scripts/brain_games.py.
3. Update [tool.poetry.scripts] in pyproject.toml with brain_games.py script
4. Build and debug publish to make sure that brain-even command launches the game
5. Record, publish and link the asciinema of package installation, game launch, user winning and losing episodes in README.md: [![asciicast](https://asciinema.org/a/IFei1plp3YOf1V7D1XAhq2Ztm.svg)](https://asciinema.org/a/IFei1plp3YOf1V7D1XAhq2Ztm)

## Step 6: "Calculator game"