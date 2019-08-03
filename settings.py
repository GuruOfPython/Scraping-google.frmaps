#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Chrome Options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHROME_OPTIONS = Options()
# CHROME_OPTIONS.add_argument("--headless")
# CHROME_OPTIONS.add_argument('--disable-gpu')  # Last I checked this was necessary.
CHROME_OPTIONS.add_argument('--disable-notifications')
# prefs = {"profile.managed_default_content_settings.images": 2, 'disk-cache-size': 4096}
# CHROME_OPTIONS.add_experimental_option('prefs', prefs)
CHROME_OPTIONS.add_argument('--ignore-certificate-errors')
CHROME_OPTIONS.add_argument("--test-type")
CHROME_OPTIONS.add_argument('--profile-directory=Default')
CHROME_OPTIONS.add_argument('--disable-infobars')
CHROME_OPTIONS.add_argument('--disable-extensions')
CHROME_OPTIONS.add_argument("--disable-cloud-import")
CHROME_OPTIONS.add_argument("--disable-popup-blocking")
CHROME_OPTIONS.add_argument("--disable-session-crashed-bubble")
# CHROME_OPTIONS.add_argument("--log-level=3")
# CHROME_OPTIONS.add_argument('--incognito')
CHROME_OPTIONS.add_argument('--disable-plugins-discovery')
CHROME_OPTIONS.add_argument('--start-maximized')
CHROME_OPTIONS.add_argument('--no-default-browser-check')
CHROME_OPTIONS.add_argument('--no-first-run')
CHROME_OPTIONS.add_argument('--no-default-browser-check')
CHROME_OPTIONS.add_argument('--ignore-gpu-blacklist')
CHROME_OPTIONS.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')

import os
import csv

