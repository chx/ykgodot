#!/bin/python

from time import time,sleep
from subprocess import call,DEVNULL
from urllib.parse import urlparse
from pyperclip import paste
try:
  from pync import Notifier
except:
  from gi.repository import Notify

def mynotify(text):
  app='YK Godot'
  try:
    Notifier.notify(text, title=app)
  except:
    Notify.init(app)
    notification = Notify.Notification.new(app, text, 'dialog-information')
    notification.show()

old_value = paste()
while True:
  current_value = paste()
  if current_value != old_value:
    old_value = current_value
    try:
      # Split and remove domain. urlparse will throw an exception if this is
      # not an URL.
      parts = urlparse(current_value).netloc.split('.')[:-1]
      # Remove co and similar.
      id = [x for x in parts if len(x) > 2][-1]
      # Wait a few seconds for the Yubikey
      timeout = time() + 10
      while time() < timeout:
        if 0 == call(["gpg", "--card-status"], stdout=DEVNULL, stderr=DEVNULL):
          if 0 == call(["pass1", "-c", id], stdout=DEVNULL, stderr=DEVNULL):
            mynotify('Password copied')
          break
        sleep(0.02)
    except:
      pass
    sleep(0.2)
