import allure
import pytest
from locators.main_page_locators import MainPageLocators  # Добавьте этот импорт
from pages.order_page import OrderPage
from pages.main_page import MainPage
from data import TestData


class TestOrderPageOrder:
    @allure.title('Проверка позитивного сценария оформления заказа')
    @allure.description('Сквозное тестирование функциональности оформления заказа из двух точек входа')
    @pytest.mark.parametrize('button,test_data', [
        (MainPageLocators.order_button_in_header, TestData.test_data_user1),
        (MainPageLocators.order_button_in_main, TestData.test_data_user2)
    ])
    def test_order_all_fields_success(self, driver, button, test_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.scroll_to_element(button)
        main_page.wait_visibility_of_element(button)
        main_page.click_on_element(button)
        order_page.data_entry_first_form(test_data)
        order_page.data_entry_second_form(test_data)