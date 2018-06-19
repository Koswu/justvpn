init:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock
publish:
	pip install 'twine>=1.5.0'
	python setup.py sdist bdist_wheel
	twine upload dist/*
	rm -fr build dist .egg justvpn.egg-info

