pyinstaller main.py -F -n sound_dataset_tools2


pip install nuitka
pip install ordered-set
pip install zstandard


nuitka --standalone main.py --enable-plugin=pyside6 --onefile --output-dir=out