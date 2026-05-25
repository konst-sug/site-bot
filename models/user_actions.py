import logging
import re 

from time import sleep
from random import uniform
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from funcs.utils import human_click

from config import service, chrome_options


class UserActionsRepeater:

    def __init__(self, url: str, conf: dict):
        self._logger = logging.getLogger(self.__class__.__name__)

        self._driver = webdriver.Chrome(service=service, options=chrome_options)
        self._wait = WebDriverWait(self._driver, 10)
        self.url = url

        self.page_timeout = conf.get('page_timeout', 50)
        self.sleep_time = conf.get('sleep_time', 3)
        self.max_sleep_time = conf.get('max_sleep_time', 10)
        self.norm_sleep_time = conf.get('norm_sleep_time', 5)

        self._logger.info('ChromeWebDriver started!')


    def load_page(self):
        res = False
        try:
            self._driver.set_page_load_timeout(self.page_timeout) 
            self._driver.get(self.url)
            sleep(self.sleep_time)
            self.click_link_class_name('cookie_accept')
            res = True
        except Exception as err:
            self._logger.error('load_page error: %s', str(err))
        return res


    def load_page_no_cookie(self):
        res = False
        try:
            self._driver.set_page_load_timeout(self.page_timeout) 
            self._driver.get(self.url)
            sleep(self.sleep_time)
            res = True
        except Exception as err:
            self._logger.error('load_page_no_cookie error: %s', str(err))
        return res


    def click_link(self, link_text: str):
        try:
            ob_button = self._wait.until(EC.element_to_be_clickable((By.LINK_TEXT, link_text)))
            ob_button.click()
            sleep(self.sleep_time)
        except Exception as err:
            self._logger.error('click_link error: %s', str(err))


    def click_link_class_name(self, name: str):
        try:
            ob_button = self._wait.until(EC.element_to_be_clickable((By.CLASS_NAME, name)))
            ob_button.click()
            #human_click(ob_button, self._driver)
            sleep(self.sleep_time)
        except Exception as err:
            self._logger.error('click_link_class_name error: %s', str(err))


    def find_and_move_to(self, class_name: str):
        try:
            elem = self._driver.find_element(By.CLASS_NAME, class_name)
            self._driver.implicitly_wait(10)
            self._driver.execute_script('arguments[0].scrollIntoView();', elem)
            sleep(self.norm_sleep_time)
        except Exception as err:
            self._logger.error('find_and_move_to error: %s', str(err))


    def _move_to(self, elem: str):
        try:
            self._driver.implicitly_wait(10)
            self._driver.execute_script('arguments[0].scrollIntoView();', elem)
            sleep(self.norm_sleep_time)
        except Exception as err:
            self._logger.error('_move_to error: %s', str(err))


    def scroll_to(self, scroll_to: int):
        try:
            script = f'window.scrollTo(0, {str(scroll_to)});'
            self._driver.execute_script(script, '')
            sleep(self.norm_sleep_time)
        except Exception as err:
            self._logger.error('scroll_to error: %s', str(err))


    def auth(self, login: str, passw: str, pattern):
        self.load_page()
        cookies = None
        try:
            self._driver.find_element(By.NAME, 'email').send_keys(login)
            self._driver.find_element(By.NAME, 'pass').send_keys(passw)

            submit_button = self._wait.until(EC.element_to_be_clickable((By.NAME, 'Enter')))
            submit_button.click()
            sleep(self.sleep_time)

            pattern = re.compile(pattern)
            self._wait.until(EC.url_matches(pattern))
            cookies = self._driver.get_cookies()
        except TimeoutException:
            self._logger.error('Redirect to URL failed. Auth failed.')
        except Exception as err:
            self._logger.error('auth error: %s', str(err))
        return cookies
    

    def control_link_div(self, block_name: str, block_num:int, link_num: int):
        '''После выполнения сделать переход назад'''
        try:
            block = self._driver.find_elements(By.CLASS_NAME, block_name)[block_num]
            link = block.find_elements(By.TAG_NAME, 'a')[link_num]
            self._move_to(link)
            sleep(self.sleep_time)
            link.click()
            
        except Exception as err:
            self._logger.error('control_link_div error: %s', str(err))


    def hide_alert(self):
        try:
            submit_button = self._wait.until(EC.element_to_be_clickable((By.ID, 'hide')))
            submit_button.click()
        except Exception as err:
            self._logger.error('hide_alert error: %s', str(err))


    def redirect(self, url: str):
        try:
            self._driver.set_page_load_timeout(self.page_timeout) 
            self._driver.get(url)
            sleep(self.sleep_time)
            res = True
        except Exception as err:
            self._logger.error('redirect error: %s', str(err))
        return res


    def save_current_url(self):
        return self._driver.current_url


    def go_to_page(self, page: int):
        count = 1
        try:
            page_block = self._driver.find_element(By.CLASS_NAME, 'pager')
            if page_block:
                pages = page_block.find_elements(By.TAG_NAME, 'a')
                count = len(pages)
                pages[page].click() if count > page else pages[count].click()
        except Exception as err:
            self._logger.error('go_to_page error: %s', str(err))
        return count


    def scroll_to_footer_smoothly(self, step=300, duration=3):
        try:
            # Получаем высоту страницы и окна
            total_height = self._driver.execute_script("return document.body.scrollHeight")
            current_scroll = 0

            while current_scroll < total_height:
                # Плавно увеличиваем позицию скролла
                delay = 1.3 + uniform(-0.15, 0.15)
                current_scroll += step
                if current_scroll > total_height:
                    current_scroll = total_height
                script = f"window.scrollTo(0, {current_scroll});"
                self._driver.execute_script(script)
                sleep(delay)
        except Exception as err:
            self._logger.error('scroll_to_footer_smoothly error: %s', str(err))


    def get_current_user_agent(self):
        """Возвращает текущий User-Agent, который видит сайт."""
        try:
            # Выполняем JS-код, который возвращает navigator.userAgent
            user_agent = self._driver.execute_script("return navigator.userAgent;")
            self._logger.info("Current User-Agent: %s", user_agent)
            return user_agent
        except Exception as err:
            self._logger.error("Unable to read User-Agent: %s", str(err))
            return None


    def exit_driver(self):
        try:
            self._driver.close()
            self._driver.quit()
        except Exception as err:
            self._logger.error('exit_driver error: %s', str(err))