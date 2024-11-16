from playwright.sync_api import Page, expect

def test_formulario_que_el_telefono_tenga_letras_y_numeros(page: Page):
    print("Given user visit homepage")
    page.goto("https://bdeo.io/")

    #print("When click cookies")
    #page.get_by_role("button", name="Aceptar cookies").click()

    print("When click pedir demo")
    page.get_by_label("Pedir demo").click()

    print("When user insert letter and number in telephone")
    page.get_by_label("Teléfono*").clear()
    page.get_by_label("Teléfono*").fill("+34 hh44gg33gg4")

    print("Then user see message El numero de telefono solo puede contener numeros")
    expect(page.get_by_text("El número de teléfono solo puede contener números")).to_be_visible()

    