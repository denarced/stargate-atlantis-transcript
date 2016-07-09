#!/bin/bash

rm -fr re-encoded/ text/
#mkdir re-encoded/ text/
./reenc.bash
./extract.py
./fixes.bash
