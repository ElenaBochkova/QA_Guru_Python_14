from selene import browser, be, have


def test_google_search_positive(manage_browser):
    browser.open("")
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_search_negative(manage_browser):
    browser.open("")
    query = 'qwqwqwqw567qwqwqwqwqwqw'
    browser.element('[name="q"]').clear().type(query).press_enter()
    browser.element('[class="card-section"]').should(have.text(f"По запросу {query} ничего не найдено."))