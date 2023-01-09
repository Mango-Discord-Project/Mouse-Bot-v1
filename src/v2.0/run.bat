@echo off

:main
pdm run py -3.11 ./src/v2.0/main.py
goto main