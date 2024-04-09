import allure
from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github_issue():
    open_page()
    search_repository('eroshenkoam/allure-example')
    open_repository('eroshenkoam/allure-example')
    open_issues_tab()
    should_be_number('#76')


@allure.step('Открытие браузера')
def open_page():
    browser.open('https://github.com')


@allure.step('Поиск репозитория {repository}')
def search_repository(repository):
    s('.header-search-button').click()
    s('#query-builder-test').send_keys(repository)
    s('#query-builder-test').submit()


@allure.step('Открытие репозитория {repository}')
def open_repository(repository):
    s(by.link_text(repository)).click()


@allure.step('Открытие вкладки Issues')
def open_issues_tab():
    s('#issues-tab').click()


@allure.step('Проверка наличия названия {name}')
def should_be_number(name):
    s(by.partial_text(name)).should(be.visible)
