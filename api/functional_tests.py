from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
browser = webdriver.Chrome()
browser.get('http://localhost:8000')

assert 'Tespress' in browser.title
