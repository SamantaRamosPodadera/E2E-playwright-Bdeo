from playwright.sync_api import Page, expect

def test_pagina_inicio(page: Page):
    print("Given user visit homepage")
    page.goto("https://bdeo.io/en/")
    expect(page.get_by_text("Damage detection and")).to_be_visible()
    expect(page.locator("section").filter(has_text="Damage detection and").get_by_role("link")).to_be_visible()
    expect(page.get_by_label("Ask for a demo")).to_be_visible()