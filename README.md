# DLTube-GUI
GUI-based downloader for YouTube videos based on search queries. Supports MP3 (with all relevant metadata) and MP4. Runs locally on your machine, so you don't need to rely on any websites going up or down.

# Requirements
1. Git CLI. For Windows, please download from [here](https://git-scm.com/download/win). For Linux, use `sudo apt-get install git` in a Terminal window. For MacOS, install Homebrew using `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` and then use `brew install git` in a Terminal window.
2. GNU Make. For Windows, please download from [here](https://gnuwin32.sourceforge.net/downlinks/make.php). For Linux, use `sudo apt-get install make` in a Terminal window. For MacOS, install Homebrew using `brew install make` in a Terminal window.
3. Python 3

# Instructions
1. Open a Terminal window (Command Prompt on Windows).
2. `git clone https://github.com/nchatterjee143/DLTube-GUI.git`
3. `cd DLTube-GUI` on Unix-based systems, `dir DLTube-GUI` on Windows
4. `make`

At this point, the application will build itself for your computer's architecture. You will be able to see the progress of your downloads in your Terminal window. The moment you close out of the app the build will self-destruct and you will need to run `make` to use the program again. Remember to `cd` or `dir` into the project directory first if you're not already there.

- **NOTE**: Running `make` uses the `make all` rule from the Makefile. If you would like to skip the additional rules that `make all` uses you may use `make build` instead of `make` or `make all`. This simply builds the application and runs it. It does not make the app self-destruct upon closing. Please note that you must have Python installed on your machine, to which `make check` will be able to check whether or not you do, and if not you will be linked to the relevant link. Also, note that do ***NOT*** use the standalone application version, as currently it is bugged. Please use `./dist/DLTube` in a Terminal window to run the application again.

Your downloads will be located within the project root directory itself, not within the `build` or `dist` folders.
