import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_presence_cart_button(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
    button_text = button.text
    assert button_text == "Añadir al carrito"