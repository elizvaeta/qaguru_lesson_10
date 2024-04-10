import allure
from selene import browser, by, be
from selene.support.shared.jquery_style import s


def test_github_issue():
    with allure.step('Открытие браузера'):
        browser.open('https://github.com')

    with allure.step('Поиск репозитория'):
        s('.header-search-button').click()
        s('#query-builder-test').send_keys('eroshenkoam/allure-example')
        s('#query-builder-test').submit()

    with allure.step('Открытие репозитория'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открытие вкладки Issues'):
        s('#issues-tab').click()

    with allure.step('Проверка наличия названия 76'):
        s(by.partial_text('#76')).should(be.visible)
