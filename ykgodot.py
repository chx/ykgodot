#!/bin/python

from time import time,sleep
from subprocess import call,DEVNULL
from urllib.parse import urlparse
from pyperclip import paste
import tldextract
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
      domain = tldextract.extract(urlparse(current_value).netloc).domain
      # Wait a few seconds for the Yubikey
      timeout = time() + 10
      while time() < timeout:
        if 0 == call(["gpg", "--card-status"], stdout=DEVNULL, stderr=DEVNULL):
          if 0 == call(["pass", "-c", domain], stdout=DEVNULL, stderr=DEVNULL):
            mynotify('Password copied')
          break
        sleep(0.02)
    except:
      pass
    sleep(0.2)
