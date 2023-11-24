import allure
from Pages.stream_page import StreamPage
from locators.streams_page_locators import StreamsPageLocators

class TestStream:

    @allure.title('Запись пользователя на поток')
    def test_user_record(self, driver):
        stream = StreamPage(driver)
        stream.click_rec_to_stream_button()
        stream.click_find_button()
        stream.click_checkbox_button()
        stream.click_next_button()