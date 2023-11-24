from selenium.webdriver.common.by import By

class StreamsPageLocators:
    RECORDING_TO_STREAM = By.XPATH, "//span[text()='Запись на поток']"  # Кнопка "Запись на поток"
    SEARCH_USERS = By.XPATH, "//span[text()='Поиск']" # Кнопка поиска
    CHECKBOX_USERS = By.XPATH, "//button[contains(@class, 'q-checkbox__svg fit absolute-full')]"  #Чекбокс выбора пользователя
    NEXT = By.XPATH, "//span[text()='Далее']" # Кнопка далее
