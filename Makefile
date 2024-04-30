.PHONY: all check_python clean

all: check_python build clean

check_python:
	@echo "Checking for Python..."
	@if python3 --version >/dev/null 2>&1; then \
		echo "Python 3 is installed"; \
	else \
		echo "Python 3 is not installed"; \
		echo "Please download and install Python from https://www.python.org/downloads/"; \
	exit 1; \
	fi

build:
	@echo "Installing dependencies..."
	pip install pyinstaller yt_dlp
	@echo "Building DLTube..."
	pyinstaller --onefile --windowed --hidden-import=yt_dlp DLTube.py
	@echo "Running DLTube..."
	./dist/DLTube

clean:
	@echo "Cleaning up..."
	rm -rf build dist DLTube.spec
