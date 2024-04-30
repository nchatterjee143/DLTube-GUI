make:
	pyinstaller --onefile --windowed --hidden-import=yt_dlp DLTube.py
	./dist/DLTube
	rm -rf build dist DLTube.spec