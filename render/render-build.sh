#!/usr/bin/env bash

# Google Chromeのインストール
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt-get update
sudo apt-get install -y ./google-chrome-stable_current_amd64.deb

# ChromeDriverのインストール
wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
unzip chromedriver_linux64.zip -d /tmp/
chmod +x /tmp/chromedriver

# Chromeバイナリを移動
mv /usr/bin/google-chrome /tmp/google-chrome

# Clean up
rm google-chrome-stable_current_amd64.deb
rm chromedriver_linux64.zip