import subprocess

from random import choice
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Настройка Selenium (укажите путь к своему chromedriver)
service = Service('drivers/chromedriver')
chrome_options = Options()
result = subprocess.run(['drivers/chromedriver', '--version'], 
                        capture_output=True, text=True)

print('Версия ChromeDriver:', result.stdout.strip())

chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-popup-blocking')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--disable-infobars')   # Убираем всплывающее окно автоматизации
chrome_options.add_argument('--disable-browser-side-navigation')  
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--log-level=0')
chrome_options.add_argument('--zoom=0.8')
chrome_options.add_argument('--remote-debugging-port=9222') 

chrome_options.add_argument('--start-maximized')

test_url = ''
url = 'https://doska-kubani.ru/'

CONF = {
    'page_timeout': 20,
    'sleep_time': 3,
    'max_sleep_time': 10,
    'norm_sleep_time': 5
}

user_agents = [
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0',
'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 OPR/129.0.0.0',

### Мобильные устройства (Android, iPhone)
'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (iPhone; CPU iPhone OS 26_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/23E261 Safari/604.1',

### Примеры из актуальных баз (2026 год)
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
'TuneIn Radio/41.6.1; iPhone18,2; iOS/26.5',
###Chrome:
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
###Edge:
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537',
#Firefox:
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:146.0) Gecko/20100101 Firefox/146.0',
#Opera:
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 OPR/129.0.0.0',
#Яндекс.Браузер:
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 YaBrowser/25.4.0.0 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 YaBrowser/25.4.0.0 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 YaBrowser/25.5.0.0 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 YaBrowser/25.3.0.0 Safari/537.36'
]

INTERVAL = 1
chrome_options.add_argument(f'user-agent={choice(user_agents)}')
