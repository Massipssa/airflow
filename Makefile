
# pip command
pip-install:
	@echo "Install required Python packages "
	pip3 install -r requirements/requirements-python3.7.txt

setup:
	@echo "Create dist folder"
	python3 src/setup.py sdist bdist_wheel

deploy:
	@echo "Deploy Python package to Python Package Index (PyPI)"
	 python3 -m twine upload -u $(USERNAME) -p $(PASSWORD) --repository testpypi dist/*

# Docker
#push-image:
#	docker
