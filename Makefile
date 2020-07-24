# ??
.PHONY: pip-install setup deploy

REQUIREMENTS="requirements/requirements-python3.7.txt"

pip-install:
	@echo "Install required Python packages "
	pip3 install -r $(REQUIREMENTS)

setup:
	@echo "Create dist folder"
	python3 src/setup.py sdist bdist_wheel

deploy:
	@echo "Deploy Python package to Python Package Index (PyPI)"
	 python3 -m twine upload --skip-existing \
 	  	-u $(USERNAME) -p $(PASSWORD) --repository testpypi dist/*

all: pip-install setup deploy
