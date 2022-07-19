clean:
	find . -type d -name __pycache__ -exec rm -r {} \+
	find . -type d -name .pytest_cache -exec rm -r {} \+

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements_dev.txt

lint:
	make clean
	flake8 .

test:
	make clean
	python manage.py test
