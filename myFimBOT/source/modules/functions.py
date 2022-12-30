import cv2
import numpy as np
import os
import modules.speech as speech
import time
import datetime
from json import loads
from requests import get
from pyowm.owm import OWM
from modules.keys import keys
import webbrowser


engine = speech.Speech()

def go_to_page(url):
  webbrowser.open(url)

def show_Insurance():
  engine.text_to_speech("1. Visit the Insurance page")
  go_to_page("url")
def show_Insurance():
  engine.text_to_speech("1. Visit the Insurance page")
  go_to_page("url")
def go_to_services():
    engine.text_to_speech("1. Visit the Insurance page")
    go_to_page("url")
def go_user_profile():
    engine.text_to_speech("1. Visit the Insurance page")
    go_to_page("url")
def go_to_fund_transfer():
    engine.text_to_speech("1. Visit the Insurance page")
    go_to_page("url")

 