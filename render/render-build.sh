#!/usr/bin/env bash

# Google Chromeのインストール
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt-get update

# Chromeを/tmp/google-chromeに展開
mkdir -p /tmp/google-chrome
dpkg -x google-chrome-stable_current_amd64.deb /tmp/google-chrome/

# ChromeDriverのインストール
wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
unzip chromedriver_linux64.zip -d /tmp/
chmod +x /tmp/chromedriver

# Clean up
rm google-chrome-stable_current_amd64.deb
rm chromedriver_linux64.zip
