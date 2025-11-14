.PHONY: help install install-dev test test-cov lint format clean run

help:
	@echo "Available commands:"
	@echo "  make install      - Install production dependencies"
	@echo "  make install-dev  - Install development dependencies"
	@echo "  make test         - Run tests"
	@echo "  make test-cov     - Run tests with coverage report"
	@echo "  make lint         - Run linters (flake8, pylint, mypy)"
	@echo "  make format       - Format code with black"
	@echo "  make clean        - Remove build artifacts and cache"
	@echo "  make run          - Run the scraper with default settings"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

test:
	python3 -m unittest discover -s tests -p "test_*.py" -v

test-cov:
	pytest --cov=src --cov-report=term-missing --cov-report=html

lint:
	flake8 src tests villages_events.py
	pylint src tests villages_events.py
	mypy src villages_events.py

format:
	black src tests villages_events.py

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete

run:
	python3 villages_events.py
