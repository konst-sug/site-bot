from time import sleep
from selenium.common.exceptions import TimeoutException
from user_actions import UserActionsRepeater


class RegSpecificActions(UserActionsRepeater):
    """
    Дочерний класс,для зарегистрированных пользователей.
    """
    def __init__(self, url: str, conf: dict):
        # Вызываем конструктор родителя (UserActionsRepeater)
        # Это инициализирует драйвер, логгер и все настройки из conf.
        super().__init__(url, conf)
        
        self._logger.info("Экземпляр RegSpecificActions успешно создан")


    def login(self, username: str, password: str, pattern):
        """
        Авторизация пользователя.
        """
        self.auth(self.url, username, password, pattern)
        # Здесь будет логика авторизации, использующая self._driver и self._wait
        self._logger.info(f"Попытка входа для пользователя {username}")

