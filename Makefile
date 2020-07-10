
# pip command
pip-install:
	@echo "Install required Python packages "
	pip3 install -r requirements/requirements-python3.7.txt

upgrade-setuptools:
	@echo "Upgrade setuptools and wheel"
	pip3 install --upgrade setuptools wheel

setup:
	@echo "Create dist folder"
	python3 src/setup.py sdist bdist_wheel

# Docker
#push-image:
#	docker