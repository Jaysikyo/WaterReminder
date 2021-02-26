@echo off
color 0b
title WaterReminder - Idle Notifier
cls

cd waterreminder
..\env\Scripts\python.exe ..\waterreminder\main.py
PAUSE