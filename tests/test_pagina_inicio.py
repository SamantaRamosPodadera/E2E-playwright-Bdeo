from playwright.sync_api import Page, expect

def test_pagina_inicio(page: Page):
    print("Given user visit homepage")
    page.goto("https://bdeo.io/en/")