clean:
	-find -name "*.un~" -exec rm {} \;
	-find -name "*.swp" -exec rm {} \;
	-find -name "*.pyc" -exec rm {} \;


test:
	python3 -m pytest tests

run:
	python3 src/async_server.py

