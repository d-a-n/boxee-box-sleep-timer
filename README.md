# Boxee Sleep Timer

<img src="https://github.com/d-a-n/boxee-box-sleep-timer/raw/master/assets/screenshot.png"/>

This little cross-platform Python app will shutdown your Boxee App/Boxee Box at a given time. Just select a device, set the time and hit activate.

Please feel free to contact me / open a ticket if you have any feature request or find bugs.


## Features

* automatic device discovery
* cross-platform (Windows, OS X, Linux)
* supporting the Boxee desktop App and the Boxee Box


## TODO

* replace HTTP API with the new JSON_RPC (http://developer.boxee.tv/JSON_RPC & https://github.com/Boxee/Boxee-Tools/blob/master/python/boxeeboxclient.py)
* code cleanup
* app settings
* device history with on/offline status
* multiple timers (daily, once, weekdays)
* a nice UI (native OS X client)
* native Android / iOS Apps


## Setup

1. Run the app via python. You will need Python >= 2.6 and wxPython installed.

```bash
$ python Main.py
```

2. Create your own stand alone app with py2app/py2exe

```bash
$ rm -R dist/ build/
$ python setup.py py2app --optimize 2 -S
```

3. Download a prebuilt package.
  * Windows: tbd
  * OS X: tbd


