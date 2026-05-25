from logging import getLogger
from time import sleep
from config import CONF, url
from models.user_actions import UserActionsRepeater

logger = getLogger(__name__)
bot = UserActionsRepeater(url, CONF)


def start_one(*args):
    """Вход; категория; раздел; Объявление №; вниз; вниз; -> раздел; вниз; выход"""
    res = False
    cat, razdel, idx = args
    bot.load_page()
    res = bot.get_current_user_agent()
    bot.click_link(cat)
    bot.click_link(razdel)
    rdr_url = bot.save_current_url()
    bot.control_link_div('ob_item', idx, 1)# выбрано объявление № idx
    bot.scroll_to(30)
    bot.scroll_to(200)
    bot.redirect(rdr_url)
    sleep(10)
    bot.scroll_to(150)
    bot.exit_driver()
    return res

def start_two(*args):
    """Вход; категория; категория; категория; раздел; вниз; -> главная; выход"""
    res = False
    cat, cat_sec, cat_th = args
    bot.load_page()
    rdr_url = bot.save_current_url()
    res = bot.get_current_user_agent()
    bot.click_link(cat)
    bot.click_link(cat_sec)
    bot.click_link(cat_th)
    bot.control_link_div('blok_top', 0, 0)# выбрано верхнее объявление
    bot.scroll_to_footer_smoothly()
    bot.redirect(rdr_url)
    sleep(10)
    bot.exit_driver()
    return res

def start_three(*args):
    """Вход; категория; раздел; раздел; вниз; вверх; выход"""
    res = False
    cat, razdel, razdel_sec, idx = args
    bot.load_page()
    res = bot.get_current_user_agent()
    bot.click_link(cat)
    bot.click_link(razdel)
    bot.click_link(razdel_sec)
    bot.control_link_div('ob_item', idx, 1)# выбрано верхнее объявление
    bot.scroll_to_footer_smoothly()
    bot.scroll_to(3)
    sleep(3)
    bot.exit_driver()
    return res

def start_four(idx):
    """Вход; лента №;вниз; вверх; выход"""
    res = False
    bot.load_page()
    res = bot.get_current_user_agent()
    bot.control_link_div('lenta_id', idx, 0)# выбрано верхнее объявление
    bot.scroll_to_footer_smoothly()
    bot.scroll_to(3)
    sleep(3)
    bot.exit_driver()
    return res

def start_five(*args):
    """Вход; категория; раздел; вниз; ссылка Футер; вниз; выход"""
    res = False
    cat, razdel, f_link = args
    bot.load_page()
    res = bot.get_current_user_agent()
    bot.click_link(cat)
    bot.click_link(razdel)
    bot.scroll_to_footer_smoothly()
    bot.click_link(f_link)
    bot.scroll_to(50)
    sleep(3)
    bot.scroll_to(200)
    bot.exit_driver()
    return res

def newuser():
    bot.load_page()
    sleep(10)
    res = bot.get_current_user_agent()
    bot.scroll_to_footer_smoothly()
    bot.find_and_move_to('top-btn-block')
    sleep(3)
    bot.scroll_to(3)
    bot.exit_driver()