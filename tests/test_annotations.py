import allure
from allure_commons.types import Severity
from selene import browser, by, be
from selene.support.shared.jquery_style import s


@allure.tag('qaguru')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'elizvaeta')
@allure.feature('Поиск issue')
@allure.story('Неавторизованный пользователь может искать issue')
@allure.link('https://github.com', name='Testing')
def test_github_issue():
    browser.open('https://github.com')

    s('.header-search-button').click()
    s('#query-builder-test').send_keys('eroshenkoam/allure-example')
    s('#query-builder-test').submit()

    s(by.link_text('eroshenkoam/allure-example')).click()

    s('#issues-tab').click()

    s(by.partial_text('#76')).should(be.visible)
