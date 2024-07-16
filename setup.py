try:
    import pygame
except ImportError as e:
    print(">>>>>>>>>> You don't have \"pygame\" installed\nrun \"pip install pygame\"")
else:
    print("You have \"pygame\" installed!")
try:
    import json
except ImportError as e:
    print(">>>>>>>>>> You don't have \"json\" installed\nrun \"pip install json\"")
else:
    print("You have \"json\" installed!")
try:
    import os
except ImportError as e:
    print(">>>>>>>>>> You don't have \"os\" installed\nrun \"pip install os\"")
else:
    print("You have \"os\" installed!")
try:
    from watchdog.observers import Observer
except ImportError as e:
    print(">>>>>>>>>> You don't have \"watchdog.observers\" installed\nrun \"pip install watchdog\"")
else:
    print("You have \"watchdog.observers\" installed!")
try:
    from watchdog.events import FileSystemEventHandler
except ImportError as e:
    print(">>>>>>>>>> You don't have \"watchdog.events\" installed\nrun \"pip install watchdog\"")
else:
    print("You have \"watchdog.events\" installed!")
try:
    import time
except ImportError as e:
    print(">>>>>>>>>> You don't have \"time\" installed\nrun \"pip install time\"")
else:
    print("You have \"time\" installed!")
k=input("press close to exit\n")