"""
Common utilities.
"""

import requests
import subprocess

# downloads a file from a url to a specific location
def download(url, filename):
    r = requests.get(url)
    with open(filename, "wb") as f:
        f.write(r.content)