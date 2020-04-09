from lxml import etree
from lxml import html
import re
import sqlite3
import requests
import datetime

class Current_value():
    def __init__(self,object):
        self.object = object
