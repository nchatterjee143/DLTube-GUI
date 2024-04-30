.PHONY: all check clean

# Detect operating system
ifeq ($(OS),Windows_NT)
    PYTHON_CMD := python
    RM_CMD := del /q /f
else
    PYTHON_CMD := python3
    RM_CMD := rm -rf
endif

all: check build clean

check:
	@echo "Checking for Python..."
	@if $(PYTHON_CMD) --version >/dev/null 2>&1; then \
		echo "Python is installed"; \
	else \
		echo "Python is not installed"; \
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
	$(RM_CMD) build dist DLTube.spec
