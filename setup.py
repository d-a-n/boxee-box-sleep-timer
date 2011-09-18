"""
Usage:
	rm -R dist/ build/
    /usr/local/bin/python setup.py py2app --optimize 2 -S
"""

from setuptools import setup

APP = ['Main.py']
DATA_FILES = []
OPTIONS = {
	'argv_emulation': False,
	'iconfile':'app_icon.icns',
	'packages':['wx'],
	'site_packages':True,
	'plist': dict(
		CFBundleName = "Boxee Sleep Timer",
		CFBundleShortVersionString = "0.1.0",
		CFBundleGetInfoString = "Boxee Sleep Timer 0.1.0",
		CFBundleExecutable = "BoxeeSleepTimer",
		CFBundleIdentifier = "to.db.boxee-sleep-timer"
	),
	
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
