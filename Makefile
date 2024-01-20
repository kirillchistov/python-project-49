install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime

lint:
	poetry run flake8 brain_games

selfcheck:
	poetry check

check: selfcheck lint

build: check
	   poetry build

package-install:
	python3 -m pip install --user dist/*.whl

publish:
	poetry publish --dry-run

.PHONY: install lint selfcheck check build