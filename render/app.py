from flask import Flask, request, jsonify, render_template
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote as url_quote
import logging

app = Flask(__name__)

# ログの設定
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/automate', methods=['POST'])
def automate():
    query = request.json.get('query')
    if not query:
        return jsonify({'error': 'Query parameter is required.'}), 400
    try:
        result = automate_chrome_search(query)
        return jsonify({'result': result})
    except Exception as e:
        app.logger.error(f"Error occurred: {str(e)}")
        return jsonify({'error': str(e)}), 500

def automate_chrome_search(query):
    driver = None  # 初期化
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        chrome_options.binary_location = "/tmp/google-chrome"
        service = ChromeService(executable_path='/tmp/chromedriver')

        app.logger.info(f"Starting Chrome with binary: {chrome_options.binary_location} and driver: {service.path}")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        app.logger.info("ChromeDriver started successfully")
        
        driver.get('https://www.google.com')
        app.logger.info("Google page loaded successfully")
        search_box = driver.find_element('name', 'q')
        search_box.send_keys(query + Keys.RETURN)
        
        driver.implicitly_wait(5)
        first_result = driver.find_element('css selector', 'h3').text
        app.logger.info(f"First result: {first_result}")
    except Exception as e:
        app.logger.error(f"Error in automate_chrome_search: {str(e)}")
        raise e
    finally:
        if driver:
            driver.quit()
    
    return first_result

if __name__ == '__main__':
    app.run(debug=True)
