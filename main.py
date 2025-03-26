import data
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium import webdriver
from data import card_number, card_code
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación.
    """
    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [
                log["message"]
                for log in driver.get_log('performance')
                if log.get("message") and 'api/v1/number?number' in log.get("message")
            ]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd(
                    'Network.getResponseBody',
                    {'requestId': message_data["params"]["requestId"]}
                )
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception(
                "No se encontró el código de confirmación del teléfono.\n"
                "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación."
            )
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_icon = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[1]')
    phone_field = (By.XPATH, '/html/body/div/div/div[1]/div[2]/div[1]/form/div[1]/div[1]/input')
    phone_case = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div')
    button_full = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    close_button_section_close = (By.CLASS_NAME, 'close-button section-close')
    button_confirmation = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
    # payment_method_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]')
    phone_modal_button = (By.CLASS_NAME, 'np-text')
    phone_input = (By.ID, 'phone')
    number = (By.XPATH, '//*[@id="phone"]')
    next_button = (By.XPATH, '//*[text()="Siguiente"]')
    click_code = (By.ID, 'code_input')
    code = (By.ID, 'code')
    select_taxi = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    phone_send_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    payment_method = (By.CLASS_NAME, "pp-button")
    add_card_button = (By.CLASS_NAME, "pp-plus")
    credit_number = (By.CLASS_NAME, 'card-number-input')
    add_credit_card = (By.XPATH, '//*[@id="number"]')
    card_cvv = (By.XPATH, '//div[@class="card-code-input"]/input[@id="code"]')
    agree_card = (By.XPATH, '//*[text()="Agregar"]')
    x_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    cell_next = (By.XPATH, '//*[text()="Confirmar"]')
    driver_message_input = (By.XPATH, '//*[@id="comment"]')
    requests_button = (By.CLASS_NAME, "reqs-head")
    blanket_and_tissues_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')
    ice_cream_button = (By.CLASS_NAME, "counter-plus")
    taxi_search_button = (By.CLASS_NAME, "smart-button-main")
    modal_taxi = (By.CLASS_NAME, "order-details")

    def __init__(self, driver):
        self.get = None
        self.driver = driver
        self.phone_field = (By.XPATH, "//input[@name='phone']")  # Verifica el XPATH

    def set_from(self, from_address):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def get_request_taxi_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.request_taxi_button)
        )

    def set_request_taxi_button(self):
        self.get_request_taxi_button().click()

    def get_comfort_icon(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.comfort_icon)
        )

    def set_comfort_icon(self):
        self.get_comfort_icon().click()

    def get_phone_case(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.phone_case)
        )

    def set_phone_case(self):
        self.get_phone_case().click()

    def get_close_button_section_close(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.close_button_section_close)
        )

    def set_close_button_section_close(self):
        self.get.close_button_section_close().click()

    def click_to_open_phone_modal(self):
        self.get_add_phone_number_button().click()

    def get_add_phone_number_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.phone_modal_button)
        )

    def set_phone_number(self, phone_number):
        self.get_phone_number().send_keys(phone_number)

    def get_phone_number(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.phone_input)
        )

    def write_driver_message(self, message_for_driver):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.driver_message_input)
        ).send_keys(data.message_for_driver)

    def add_blanket_and_tissues(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.blanket_and_tissues_button)
        ).click()

    def add_ice_cream(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.ice_cream_button)
        ).click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.ice_cream_button)
        ).click()

    def get_payment_method_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.payment_method)
        )

    def set_payment_method_button(self):
        self.get_payment_method_button().click()

    def get_add_card_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.add_card_button)
        )

    def set_add_card_button(self):
        self.get_add_card_button().click()

    def get_button_full(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.button_full)
        )

    def set_button_full(self):
        self.get_button_full().click()

    def get_sms_code(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.code)
        )

    def set_sms_code(self):
        code = retrieve_phone_code(self.driver)
        self.get_sms_code().send_keys(code)

    def get_button_confirmation(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.button_confirmation)
        )

    def set_button_confirmation(self):
        self.get_button_confirmation().click()

    def fill_credit_card(self, card_number, card_code):
        self.driver.find_element(*self.add_credit_card).send_keys(card_number)
        cvv_field = self.driver.find_element(*self.card_cvv)
        cvv_field.send_keys(card_code)
        cvv_field.send_keys(Keys.TAB)
        self.driver.find_element(*self.agree_card).click()

    def get_close_modal(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.x_button)
        )

    def set_close_modal(self):
        self.get_close_modal().click()

    def confirm_phone(self):
        self.driver.find_element(*self.cell_next).click()


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_request_taxi(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_request_taxi_button()
        routes_page.set_comfort_icon()

    def test_fill_phone_number(self):
        self.test_request_taxi()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_to_open_phone_modal()
        routes_page.set_phone_number(data.phone_number)
        routes_page.set_button_full()
        routes_page.set_sms_code()
        routes_page.set_button_confirmation()
        assert routes_page.get_add_phone_number_button().text == data.phone_number

    def test_add_payment_method(self):
        self.test_fill_phone_number()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_payment_method_button()
        routes_page.set_add_card_button()
        routes_page.fill_credit_card(card_number, card_code)
        time.sleep(2)
        routes_page.set_close_modal()

    def test_write_driver_message(self):
        self.test_add_payment_method()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.write_driver_message(data.message_for_driver)

    def test_add_blanket_and_tissues(self):
        self.test_write_driver_message()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_blanket_and_tissues()

    def test_add_ice_cream(self):
        self.test_add_payment_method()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_ice_cream()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
