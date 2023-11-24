import allure
from locators.streams_page_locators import StreamsPageLocators
from Pages.base_page import BasePage


class StreamPage(BasePage):

    @allure.step('Нажать на кнопку "Запись на поток"')
    def click_rec_to_stream_button(self):
        self.driver.find_element(*StreamsPageLocators.RECORDING_TO_STREAM).click()

    @allure.step('Нажать на кнопку "Поиск"')
    def click_find_button(self):
        self.driver.find_element(*StreamsPageLocators.SEARCH_USERS).click()

    @allure.step('Нажать на Чекбокс')
    def click_checkbox_button(self):
        self.click_to_element(*StreamsPageLocators.CHECKBOX_USERS)

    @allure.step('Нажать на кнопку "Далее"')
    def click_next_button(self):
        self.click_to_element(*StreamsPageLocators.NEXT)
