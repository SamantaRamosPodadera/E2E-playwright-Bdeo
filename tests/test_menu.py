from playwright.sync_api import Page, expect
import re

def test_visitar_enlaces_menu(page: Page):
    print("Given user visit homepage")
    page.goto("https://bdeo.io/en/")
    
