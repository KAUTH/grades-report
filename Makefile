# Link for reference: https://makefiletutorial.com/

init:
	pip install pipenv --upgrade
	pipenv install --dev

all-tests:
	tox -r
	coverage xml -i
	coverage html -i

py36-tests:
	tox -re py36,pep8
	coverage xml -i
	coverage html -i

py37-tests:
	tox -re py37,pep8

py38-tests:
	tox -re py38,pep8

# https://packaging.python.org/guides/using-testpypi/
publish-test:
	pip install 'twine>=1.5.0'
	python setup.py sdist bdist_wheel
	twine upload --repository testpypi dist/*
	rm -fr build dist .egg requests.egg-info

publish:
	pip install 'twine>=1.5.0'
	python setup.py sdist bdist_wheel
	twine upload dist/*
	rm -fr build dist .egg requests.egg-info