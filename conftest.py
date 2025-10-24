import pytest
from selene import browser
from selenium import webdriver
from utils import attach


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    # Настройки Selene
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    # Используем ChromeOptions как в современных версиях
    options = webdriver.ChromeOptions()

    # Устанавливаем capabilities
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "128.0")
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": True
    })

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
    browser.quit()
