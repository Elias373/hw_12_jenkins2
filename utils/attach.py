import allure
from allure_commons.types import AttachmentType


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_logs(browser):
    # Логи браузера больше не доступны в новых версиях Selenium/Chrome
    log_info = """
    Browser console logs are no longer available in Selenium 4+ with Chrome.
    This is a known limitation due to changes in Chrome DevTools Protocol.

    Alternatives:
    - Use browser developer tools manually
    - Implement custom JavaScript logging
    - Use performance logs instead
    """

    allure.attach(
        log_info,
        name='browser_logs_info',
        attachment_type=allure.attachment_type.TEXT,
    )




def add_html(browser):
    html = browser.driver.page_source
    allure.attach(body=html, name='page_source', attachment_type=AttachmentType.HTML)


def add_video(browser):
    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')