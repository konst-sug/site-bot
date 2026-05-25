from selenium.webdriver.common.action_chains import ActionChains
import random

def human_click(element, driver):
    """
    Выполняет "нечеткий" клик по элементу.
    :param element: Веб-элемент (кнопка, ссылка)
    :param driver: Объект вебдрайвера
    """
    # Получаем координаты и размер элемента
    rect = element.rect 
    
    # Вычисляем границы, внутри которых можно кликать
    # Добавим небольшой отступ (10% от размера), чтобы не кликать по самым краям
    x_min = rect['x'] + (rect['width'] * 0.1)
    x_max = rect['x'] + (rect['width'] * 0.9)
    
    y_min = rect['y'] + (rect['height'] * 0.1)
    y_max = rect['y'] + (rect['height'] * 0.9)

    # Генерируем случайные координаты внутри этих границ
    random_x = random.uniform(x_min, x_max)
    random_y = random.uniform(y_min, y_max)

    actions = ActionChains(driver)
    
    actions.move_by_offset(random_x, random_y)
    
    actions.click()
    
    actions.perform()