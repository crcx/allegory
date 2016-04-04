#!/usr/bin/env python3
# coding: utf-8
# This is a small script to download / update the Parable sources

import requests
import os.path
import sys

urls = [
        'https://raw.githubusercontent.com/crcx/parable/master/source/py/parable.py',
        'https://raw.githubusercontent.com/crcx/parable/master/source/py/stdlib.p',
        'https://raw.githubusercontent.com/crcx/parable/master/source/py/gen-snapshot.py',
       ]

print('Downloading')
for url in urls:
    sys.stdout.write('  ' + os.path.basename(url) + '\t\t')
    r =  requests.get(url)
    with open(os.path.basename(url), 'w') as f:
        f.write(r.text)
    print(str(len(r.content)) + ' bytes')
print('Finished')
