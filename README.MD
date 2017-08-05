# GetTodaysPath

This script which gathers GPS coordinates of the places visited the current day, based on a Google account paired with a mobile device that is carried during the itinaries.
It actually is a part of a larger project which aims to to monitor the weekly path ofan individual and compares the visited places with another set from a database.

### Prerequisites

This script has been made following the Python 3 standards rules and checked with PyChecker.
In order to work properly it requires some libraries that can ban installed with pip3.
Libraries calls are listed below:
```
import datetime, time, os, sys, subprocess
from lxml import etree
from xml.dom.minidom import parseString
from threading import Thread
```
It is also needed to have the surf browser:
```
apt install surf
```


### Installing

```
git clone *this_git*
cd getTodaysPath
python3 getTodaysPath.py
```
The printed data are just prints called at the end of the different steps of the script.
Feel free to remove those prints to lighten the shell. Moreover there might be commented lines which display more information, check the code.

### How it works

This script is based on the KML file which can be obtained from the maps application of GOogle.
IMPORTANT: In order to run the script properly, the surfbrowser is needed AND it needs to be able to access to a Google account cookie. In fact, the script opens a specific URL from Google using Surf and initiates a download of a KML file which contains information about thecurrent day path.

It consits in 4 subprograms ran one after the other:
```
 Erasing existing KML file in the working directory
 Downloading the good KML file from Google
 Reading the content of the KML FILE and extracting information
 Saving information into /history/*current-date*.coords
```
This script has been created to be executed daily, very early if possible, and thus is a part of a larger project.

## Deployment

Coming soon

## Authors

* **Thomas Di Giusto** - *Initial work* 
* **See Links in code** - *Inspiration*


