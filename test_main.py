import time

import pytest
from g_utilities import Utilll
from whatsapp.pages import HomePage, ChatPage


@pytest.fixture(scope="session")
def set_up():
    global driver, home_page, chat_page
    driver = Utilll.get_driver("android")
    home_page = HomePage.HomePage(driver)
    chat_page = ChatPage.ChatPage(driver)
    yield
    time.sleep(2)
    driver.quit()


def test_verify_search_btn(set_up):
    print(home_page.search_btn().get_attribute("clickable"))
    assert home_page.search_btn().get_attribute("clickable") == False


def test_click_search(set_up):
    data = home_page.search_click().is_enabled()
    # pytest.home_page.search("tinku")
    assert data == True


def test_enter_reciever(set_up):
    element = home_page.search("banglore")
    assert element.text == "banglore"


def test_verify_results(set_up):
    result_element = home_page.result()
    assert len(result_element) == 1, "target should be 1"  # assert the total no. of result
    assert result_element[0].is_displayed()
    assert result_element[0].text == "Hackathon Banglore"


def test_verify_cick(set_up):
    home_page.click_result(0).click()
    assert chat_page.chat_name().text == "Hackathon banglore"


def test_send_msg(set_up):
    chat_page.enter_msg("hello")
    chat_page.click_send()
    # driver.quit()

# set_up()
# send_message("banglore")
