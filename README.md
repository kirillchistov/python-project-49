## Brain games: simple command line games for math geeks

### Description
Hexlet Python Developer training project. 
5 simple CLI math games to massage your brain muscle!

### Hexlet tests and linter status:
[![Actions Status](https://github.com/kirillchistov/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/kirillchistov/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/d922981a966fe718675c/maintainability)](https://codeclimate.com/github/kirillchistov/python-project-49/maintainability)

### Games demonstration:
#### Even or Odd
[![asciicast](https://asciinema.org/a/IFei1plp3YOf1V7D1XAhq2Ztm.svg)](https://asciinema.org/a/IFei1plp3YOf1V7D1XAhq2Ztm)

#### Calculator
[![asciicast](https://asciinema.org/a/tlFjvkcB4DDTVMcy0EO3satOU.svg)](https://asciinema.org/a/tlFjvkcB4DDTVMcy0EO3satOU)

#### GCD
[![asciicast](https://asciinema.org/a/CncHybP2ROvOMYz316ztqrnTo.svg)](https://asciinema.org/a/CncHybP2ROvOMYz316ztqrnTo)

#### Progression
[![asciicast](https://asciinema.org/a/ISpMbFYNaprK6sw0QqO4WRYxS.svg)](https://asciinema.org/a/ISpMbFYNaprK6sw0QqO4WRYxS)

#### Prime
[![asciicast](https://asciinema.org/a/4MakelJDELwQWNESNtDj7NHFt.svg)](https://asciinema.org/a/4MakelJDELwQWNESNtDj7NHFt)


### Requirements:
python = "^3.9+", poetry = "^1.4.2", prompt = "^0.4.1"
```sh
sudo apt install python3
sudo apt -y install python3-pip
python3 -m pip install --upgrade --user pip
pipx install poetry
pip install prompt 
```

### Clone project:
```sh
git clone git@github.com:kirillchistov/python-project-49.git
```

### Install:
```sh
cd python-project-49
make install build package-install
```

### Launch games:
```sh
 make brain-even
```
```sh
brain-calc 
```
```sh
brain-gcd 
```
```sh
brain-progression 
```
```sh
brain-prime
```