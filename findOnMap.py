#!/usr/local/bin/python3
import webbrowser, sys, pyperclip

# Check if command line arguments were passed
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
   address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)