#!/bin/python

import time
from subprocess import check_call,DEVNULL
from urllib.parse import urlparse
import pyperclip
# Remember to run tldextract --update as root.
import tldextract
from retrying import retry

try:
  from pync import Notifier
  def notify(text):
    Notifier.notify(text, title='YK Godot')
except ImportError:
  try:
    from gi.repository import Notify
    def notify(text):
      app='YK Godot'
      Notify.init(app)
      notification = Notify.Notification.new(app, text, 'dialog-information')
      notification.show()
  except ImportError:
    def notify(text):
      pass

@retry(stop_max_delay=10000,wait_fixed=20)
def generate_password(domain):
  check_call(["gpg", "--card-status"], stdout=DEVNULL, stderr=DEVNULL)
  check_call(["pass", "-c", domain], stdout=DEVNULL, stderr=DEVNULL)

old_value = pyperclip.paste()
while True:
  current_value = pyperclip.paste()
  if current_value != old_value:
    old_value = current_value
    domain = tldextract.extract(urlparse(current_value).netloc).domain
    if domain:
      generate_password(domain)
      notify('Password copied')
  time.sleep(0.2)
