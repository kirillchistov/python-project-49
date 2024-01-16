### Hexlet tests and linter status:
[![Actions Status](https://github.com/kirillchistov/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/kirillchistov/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/d922981a966fe718675c/maintainability)](https://codeclimate.com/github/kirillchistov/python-project-49/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/d922981a966fe718675c/test_coverage)](https://codeclimate.com/github/kirillchistov/python-project-49/test_coverage)
[![asciicast](https://asciinema.org/a/IFei1plp3YOf1V7D1XAhq2Ztm.svg)](https://asciinema.org/a/IFei1plp3YOf1V7D1XAhq2Ztm)

## Step 1: Initialize the package. 
[x] DOD: executable file, printing 'Welcome to the Brain Games!' when launched.
- Pre-requisites: Python3.6+, pip 19+, poetry 1.2.0+
[x] Clone git@github.com:kirillchistov/python-project-49.git
[x] Initialize hexlet-code with poetry
[x] Create /brain-games and /brain-games/scripts
[x] Update /pyproject.toml (tool.poetry and tool.poetry.scripts)
[x] Create /brain-games/__init__.py and /brain-games/scripts/__init__.py
[x] Create /brain-games/scripts/brain_games.py with main function
[x] Poetry install the package and test if it works

## Step 2: Prepare to publish the package
[x] DOD: package will represent executable program accessible via 'brain-games' command
[x] Add shebang to /brain-games/scripts/brain_games.py
[x] Create /Makefile with install, build, publish, package-install commands
[x] Build package and debug publication
[x] Install the package with make package-install and test brain-games in bash
[x] Git push the repository

## Step 3: Work with external library
[x] DOD: Integrate the library to interact with a user (Ask the name and greet).
[x] Add prompt library dependency (poetry add prompt)
[x] Create brain_games/cli.py with welcome_user function and name prompt (import prompt)
[x] Call welcome_user function in brain_games/scripts/brain_games.py
[x] Build package
[x] Debug publication

## Step 4: Code quality
[x] DOD: Integrade code quality tracking services and linter
[x] Register with CodeQuality (Quality branch)
[x] Connect the repo and add [![Maintainability](https://api.codeclimate.com/v1/badges/d922981a966fe718675c/maintainability)](https://codeclimate.com/github/kirillchistov/python-project-49/maintainability) badge
[x] Add flake8 dependency (poetry add --group dev flake8)
[x] Add setup.cfg from the [hexlet boilerplate](https://github.com/hexlet-boilerplates/python-package/blob/main/setup.cfg) and check if 'poetry run flake8 brain_games' works
[x] Add Make lint command to launch poetry run flake8 brain_games and correct all linter errors

## Step 5: "Even check"
[x] DOD: the program will prompt the user to answer 'yes' to even, 'no' to odd numbers, print results
[x] Add brain_games/scripts/brain_even.py with the game logic
[x] Don't touch the previously added brain_games/cli.py, brain_games/scripts/brain_games.py.
[x] Update [tool.poetry.scripts] in pyproject.toml with brain_games.py script
[x] Build and debug publish to make sure that brain-even command launches the game
[x] Record, publish and link the [asciinema](https://asciinema.org/a/IFei1plp3YOf1V7D1XAhq2Ztm) of package installation, game launch, user winning and losing episodes in README.md

## TODO Step 6: "Calculator game"
[] DOD: the program will calculate random math expression and print correct result
[] Add /scripts/brain_calc.py with [game logic](https://ru.hexlet.io/projects/49/members/36039?step=6)
[] Streamline architecture and file structure (/games) so that the logic is centralized and manageable
[] Add [tool.poetry.scripts] section to pyproject.toml
[] Build, debug publish and test the game, add asciinema to README.md
