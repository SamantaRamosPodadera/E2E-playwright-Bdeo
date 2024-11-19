from playwright.sync_api import Page, expect
import re

def test_visitar_enlaces_menu(page: Page):
    print("Given user visit homepage")
    page.goto("https://bdeo.io/en/")
    page.get_by_text("Auto Insurers").hover()
    page.locator("a").filter(has_text="Vehicle Underwriting").click()
    expect(page.get_by_text("Fastest underwriting in the market", exact=True)).to_be_visible()
    page.get_by_text("Auto Insurers").hover()
    page.locator("a").filter(has_text=re.compile(r"^Claims Management$")).click()
    expect(page.get_by_text("The fastest claims resolution in the industry", exact=True)).to_be_visible()
    page.locator("a").filter(has_text="Property Insurers").click()
    expect(page.get_by_text("Cash settlement in just a few clics", exact=True)).to_be_visible()
    page.locator("a").filter(has_text="Fleet Management").click()
    expect(page.get_by_text("Keep track of the status of your vehicle fleet at any time", exact=True)).to_be_visible()
    page.locator("a").filter(has_text="Company").click()
    expect(page.get_by_role("heading", name="About us")).to_be_visible()

    
