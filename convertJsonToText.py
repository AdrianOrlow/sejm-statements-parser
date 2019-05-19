import json
import time
import sys
import re
import pathlib


def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()


with open('data.json') as f:
    jsonData = json.load(f)

decoded = ""
for index, jsonDataElement in enumerate(jsonData):
    progress(index, len(jsonData), 'converting')
    decoded += (jsonDataElement + "\n\n")

target = open('data.txt', 'wb')
target.write(decoded.encode(encoding='UTF-8'))
target.close()
