from playwright.sync_api import Page, expect

def test_formulario_validacion (page: Page):
    print("Given user visit demo homepage")
    page.goto("https://bdeo.io/en/demo/")
    page.get_by_role("button", name="REQUEST MY DEMO").click()
    expect(page.locator("fieldset").filter(has_text="First Name*Please complete").locator("label").nth(1)).to_be_visible()
    expect(page.locator("fieldset").filter(has_text="Working email*Please complete").locator("label").nth(1)).to_be_visible()
    expect(page.locator("fieldset").filter(has_text="Phone Number**Afghanistan").locator("label").nth(1)).to_be_visible()


    