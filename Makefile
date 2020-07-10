
# pip command
pip-install:
	pip install -r requirements/requirements-python3.7.txt

upgrade-setuptools:
	# pip3 install --user --upgrade setuptools wheel
	pip install --upgrade setuptools wheel

# Docker
push-image:
	docker