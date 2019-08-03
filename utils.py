#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import openpyxl
import xlrd
import time
import os
import datetime
import requests
from lxml import html
from urllib.parse import urljoin
import os
import math

from datetime import date, timedelta, datetime
from dateutil import relativedelta
import re
from string import ascii_uppercase, ascii_lowercase
import itertools

