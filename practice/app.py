from selenium import webdriver

# ChromeDriverを使用してブラウザを起動
driver = webdriver.Chrome()

# 例としてGoogleのページを開く
driver.get("https://www.google.com")

# ブラウザを閉じる
driver.quit()