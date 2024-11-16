from playwright.sync_api import Page, expect
import re

def test_visitar_aseguradora_de_motor_gestion_poliza(page: Page):
    print("Given user visit homepage")
    page.goto("https://bdeo.io/en/")
    
    print("Given user change language to spanish")
    page.locator("#slb-44991").hover()
    page.locator("#navbar").get_by_text("Español").click()

   # print("When user accept cookies")
   # page.get_by_role("button", name="Aceptar cookies").click()

    print("When user click aseguradora de motor")
    page.locator("#slb-21290").click()

    print("When user click suscropcion de poliza ")
    page.locator("a").filter(has_text=re.compile(r"^Suscripción de Pólizas$")).click()

    print("Then user see title suscripcion de poliza")
    expect(page.get_by_text("La suscripción de pólizas más rápida del mercado", exact=True)).to_be_visible()


def test_visitar_aseguradora_de_motor_gestion_siniestro(page: Page):
    print("Given user visit homepage")
    page.goto("https://bdeo.io/en/")
    
    print("Given user change language to spanish")
    page.locator("#slb-44991").hover()
    page.locator("#navbar").get_by_text("Español").click()

   # print("When user accept cookies")
   # page.get_by_role("button", name="Aceptar cookies").click()

    print("When user click aseguradora de motor")
    page.locator("#slb-21290").click()

    
    print("When user click gestion de siniestros")
    page.locator("a").filter(has_text=re.compile(r"^Gestión de Siniestros$")).click()

    print("Then user see title gestion de siniestros")
    expect(page.get_by_text("La resolución de siniestros más ágil en la industria.", exact=True)).to_be_visible()
