#Makefile

install:
	poetry install

brain-games:
<<<<<<< HEAD
=======

>>>>>>> refs/remotes/origin/step_4
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
<<<<<<< HEAD
=======

>>>>>>> refs/remotes/origin/step_4
	poetry run flake8 brain_games
