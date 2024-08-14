from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote as url_quote

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Chrome Automation App!"

@app.route('/automate', methods=['POST'])
def automate():
    query = request.json.get('query')
    if not query:
        return jsonify({'error': 'Query parameter is required.'}), 400
    try:
        result = automate_chrome_search(query)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def automate_chrome_search(query):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # ChromeDriverのパスを指定
    service = ChromeService(executable_path='/tmp/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        driver.get('https://www.google.com')
        search_box = driver.find_element('name', 'q')
        search_box.send_keys(query + Keys.RETURN)
        
        driver.implicitly_wait(5)
        first_result = driver.find_element('css selector', 'h3').text
    finally:
        driver.quit()
    
    return first_result

if __name__ == '__main__':
    app.run(port=5000)