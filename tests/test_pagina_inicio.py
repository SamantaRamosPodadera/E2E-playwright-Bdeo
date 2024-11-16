from playwright.sync_api import Page, expect

def test_pagina_inicio(page: Page):
    print("Given user visit homepage")
    page.goto("https://bdeo.io/en/")
    
    print("Given user change language to spanish")
    page.locator("#slb-44991").hover()
    page.locator("#navbar").get_by_text("Español").click()

  # print("When user click cookies")
  #  page.get_by_role("button", name="Aceptar cookies").click()


    print("When user see title ispeccion y evaulacion de daños")
    expect(page.get_by_role("heading", name="Inspección y evaluación de daños")).to_be_visible()

    print("When user click empieza hoy")
    page.locator("section").filter(has_text="Inspección y evaluación de daños").get_by_role("link").click()

    print("Then user see formulario demo")
    expect(page.get_by_role("heading", name="Pide tu demo y descubre las")).to_be_visible()

    
