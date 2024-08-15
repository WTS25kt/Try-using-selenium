#!/bin/bash

# Google Chromeのインストール
echo "Installing Google Chrome..."
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt-get update
apt-get install -y ./google-chrome-stable_current_amd64.deb

# ChromeDriverのインストール
echo "Installing ChromeDriver..."
wget -N https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip -P /tmp/
unzip /tmp/chromedriver_linux64.zip -d /tmp/
chmod +x /tmp/chromedriver

# クリーンアップ
rm google-chrome-stable_current_amd64.deb
rm /tmp/chromedriver_linux64.zip
