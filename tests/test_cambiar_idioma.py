from playwright.sync_api import Page, expect

def test_cambiar_idioma (page: Page):
    print("Given user visit homepage")
    page.goto("https://bdeo.io/en/")
    print("When change to Spanish language")
    page.locator("#slb-44991").hover()
    
    page.locator("#navbar").get_by_text("Español").click()
    print("Then should see elements in Spanish")
    expect(page.get_by_label("Ask for a demo")).to_contain_text("Pedir demo")
    expect(page.get_by_role("main")).to_contain_text("Empieza hoy")
    expect(page.locator("h1")).to_contain_text("Inspección y evaluación de daños en segundos.")
    expect(page.locator("#slb-34237")).to_contain_text("Aseguradoras de Motor")
