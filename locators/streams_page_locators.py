from selenium.webdriver.common.by import By

class StreamsPageLocators:
    RECORDING_TO_STREAM = By.XPATH, "//button[contains(@class, 'create-btn__btn__text')]"  # Кнопка "Запись на поток"
    SEARCH_USERS = By.XPATH, "//button[contains(@class, 'q-btn__content text-center col items-center q-anchor--skip justify-center row')]/button[text()='Поиск']" # Кнопка поиска
    CHECKBOX_USERS = By.XPATH, "//button[contains(@class, 'q-checkbox__svg fit absolute-full')]"  #Чекбокс выбора пользователя
    NEXT = By.XPATH, "//button[contains(@class, 'q-btn__content text-center col items-center q-anchor--skip justify-center row')]/button[text()='Далее']" # Кнопка далее
