#!/bin/bash

# Google Chromeのインストール
echo "Installing Google Chrome..."
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt-get update
dpkg -x google-chrome-stable_current_amd64.deb /tmp/google-chrome

# List the contents of the directory to check the installation
echo "Contents of /tmp/google-chrome/opt/google/chrome/:"
ls -l /tmp/google-chrome/opt/google/chrome/

# インストールが成功したかを確認
if [ -f "/tmp/google-chrome/opt/google/chrome/google-chrome" ]; then
  echo "Google Chrome installed successfully at /tmp/google-chrome/opt/google/chrome/google-chrome"
else
  echo "Error: Google Chrome installation failed or the binary is not in the expected location."
fi

# ChromeDriverのインストール
echo "Installing ChromeDriver..."
wget -N https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip -P /tmp/
unzip /tmp/chromedriver_linux64.zip -d /tmp/
chmod +x /tmp/chromedriver

# クリーンアップ
rm google-chrome-stable_current_amd64.deb
rm /tmp/chromedriver_linux64.zip
