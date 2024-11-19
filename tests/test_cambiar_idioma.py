from playwright.sync_api import Page, expect

def test_cambiar_idioma (page: Page):
    print("Given user visit demo homepage")
    page.goto("https://bdeo.io/en/")