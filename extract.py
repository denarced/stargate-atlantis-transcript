#!/usr/bin/env python3

import glob
import os

import html2text


def extractNearby(cont):
    begin = "<!-- BEGIN TRANSCRIPT BOX -->"
    end = "<!-- END TRANSCRIPT BOX -->"
    alpha = cont.find(begin) + len(begin)
    omega = cont.find(end)
    return cont[alpha:omega].strip()


def longestLine(s):
    suspiciousLength = 200
    longest = ''
    for each in s.split('\n'):
        stripped = each.strip()
        if len(stripped) > len(longest):
            longest = stripped
        elif suspiciousLength < len(stripped):
            print("Suspiciously long line:", stripped)
    return longest


def extractTranscript(filen):
    with open(filen) as f:
        cont = f.read()
    nearby = extractNearby(cont)
    return longestLine(nearby)


def createDirectory(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)

if __name__ == '__main__':
    counter = 0
    files = sorted(glob.glob('re-encoded/*.shtml'))
    targetDir = 'text/'
    createDirectory(targetDir)
    for eachFile in files:
        filename = os.path.basename(eachFile)
        episode = os.path.splitext(filename)[0]
        dest = os.path.join(targetDir, episode + '.md')
        transcript = extractTranscript(eachFile)
        markdown = html2text.html2text(transcript)
        print(eachFile)
        with open(dest, 'w') as f:
            f.write(markdown)
