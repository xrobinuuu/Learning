#
import time
import random
from typing import Optional

from lxml import etree
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.automate import Browser
from config.core.decorator import retry


class CrawlIphone(Browser):

    def __init__(
            self,
            url: str,
            surname: str,
            name: str,
            email: str,
            passwd: str,
            phone_num: str,
            _remote: bool = False,
            _choice_distinct: bool = False,
            loading=True,
            **kwargs
    ):
        if _remote:
            super().__init__(headless=False)
            self.driver = self.remote_chrome()
        else:
            super().__init__(loading=loading, headless=False)
            self.driver = self.chrome()
        if _choice_distinct:
            self.province = kwargs['province']
            self.city = kwargs['city']
            self.distinct = kwargs['distinct']

        self._choice_distinct = _choice_distinct
        self.url = url
        self.surname = surname
        self.phone_num = phone_num
        self.name = name
        self.email = email
        self.passwd = passwd

        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)
        self.refresh = 0
        self.success = 0
        self.signin = False
        self.wait_time = 7

    def run(self) -> Optional:
        self.shop_login()
        if not self.signin:
            self.settle_login()
            self.signin = True

        self.wait.until(EC.visibility_of_element_located((By.XPATH, '(//button[@role="radio"])[2]'))).click()
        if self._choice_distinct:
            self.choice_distinct()
        self.check_product()
        self.choice_pay_method()
        time.sleep(1000)

    def agree_item(self) -> Optional:
        button1 = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@class="form-checkbox-indicator"][1]')))
        button1.click()

        button2 = self.driver.find_element(By.XPATH, '(//span[@class="form-checkbox-indicator"])[2]')
        button2.click()

        agree = self.driver.find_element(by=By.ID, value='consent-overlay-accept-button')
        agree.click()

    def settle_login(self) -> Optional:
        self.agree_item()
        apple_id = self.driver.find_element(by=By.ID, value='signIn.customerLogin.appleId')
        apple_id.send_keys(self.email)
        self.driver.execute_script("arguments[0].value = '';", apple_id)
        apple_id.send_keys(self.email)

        password = self.driver.find_element(by=By.ID, value='signIn.customerLogin.password')
        password.send_keys(self.passwd)

        login = self.driver.find_element(by=By.ID, value='signin-submit-button')
        login.click()

    def choice_distinct(self) -> Optional:

        choice_button = self.driver.find_element(
            by=By.XPATH,
            value='//button[@class="rs-edit-location-button as-buttonlink icon icon-after icon-chevrondown"]')
        choice_button.click()

        province = self.driver.find_element(
            by=By.XPATH,
            value=f'//button[@class="rc-province-selector-option typography-body rc-province-selector-option-state" and text()="{self.province}"]')
        province.click()

        city = self.driver.find_element(
            by=By.XPATH,
            value=f'//button[@class="rc-province-selector-option typography-body rc-province-selector-option-city" and text()="{self.city}"]')
        city.click()

        district = self.driver.find_element(
            by=By.XPATH,
            value=f'//button[@class="rc-province-selector-option typography-body rc-province-selector-option-district" and text()="{self.distinct}"]')
        district.click()

    def check_product(self) -> Optional:
        loop = True
        while loop:
            self.driver.refresh()
            self.refresh += 1
            t1 = time.time()
            t2 = time.time()

            if etree.HTML(self.driver.page_source).xpath(".//center/h1[text()='503 Service Temporarily Unavailable']"):
                print("503 Service Temporarily Unavailable")
                self.wait_time = 7
                continue
            else:
                self.wait_time = 7
                self.wait.until(
                    lambda driver: not driver.find_element(
                        By.ID, 'rs-checkout-continue-button-bottom').get_attribute('disabled')
                )
                labels = self.driver.find_elements(by=By.XPATH, value='//li[@class="form-selector"]')
                if len(labels) > 0:
                    self.success += 1
                while t2 - t1 < self.wait_time and loop:
                    for label in labels[:5]:
                        available = label.find_element(
                            by=By.XPATH,
                            value='./label//span[@class="column large-6 small-5 rt-storelocator-store-right"]/span/span[1]'
                        ).text
                        title = label.find_element(by=By.XPATH, value='.//span[@class="form-selector-title"]').text
                        print(title, available)
                        if (available in ['今天 可取货', '明天 可取货']) and (
                                title in ['Apple 深圳万象城', 'Apple 深圳益田假日广场']):
                            commodity = label.find_element(by=By.XPATH, value='./label/span')
                            commodity.click()
                            loop = False
                            print('---------继续填写信息----------')
                            self.wait.until(
                                lambda driver: not driver.find_element(
                                    By.ID,
                                    'rs-checkout-continue-button-bottom'
                                ).get_attribute('disabled')
                            )
                            self.driver.find_element(by=By.ID, value='rs-checkout-continue-button-bottom').click()
                            self.fill_personal_info()
                            break
                    time.sleep(1)
                    t2 = time.time()
                    print('-----------------------------')
            time.sleep(self.wait_time)
            print(f'-----已刷新：{self.refresh}次，刷新成功：{self.success}，刷新失败：{self.refresh - self.success}-----')

    def fill_personal_info(self) -> Optional:
        last_name = self.wait.until(EC.visibility_of_element_located(
            (By.ID, 'checkout.pickupContact.selfPickupContact.selfContact.address.lastName')))
        last_name.send_keys(self.surname)

        first_name = self.driver.find_element(
            by=By.ID,
            value='checkout.pickupContact.selfPickupContact.selfContact.address.firstName'
        )
        first_name.send_keys(self.name)

        email = self.driver.find_element(
            by=By.ID,
            value='checkout.pickupContact.selfPickupContact.selfContact.address.emailAddress'
        )
        email.send_keys(self.email)

        phone = self.driver.find_element(
            by=By.ID,
            value='checkout.pickupContact.selfPickupContact.selfContact.address.fullDaytimePhone'
        )
        phone.send_keys(self.phone_num)

        continue_button = self.driver.find_element(by=By.ID, value='rs-checkout-continue-button-bottom')
        continue_button.click()

    def choice_pay_method(self) -> Optional:
        pay_method = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//div[@id="checkout.billing.billingoptions.installments0001243254-selector"]')))
        pay_method.click()

        payment_installments = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//li[@class="rs-payment-installments-option form-selector"][3]')))
        payment_installments.click()

        checkout_order_button = self.driver.find_element(by=By.ID, value='rs-checkout-continue-button-bottom')
        checkout_order_button.click()

        self.wait.until(EC.text_to_be_present_in_element(
            (By.XPATH, '//button[@id="rs-checkout-continue-button-bottom"]'), "立即下单"))
        button = self.driver.find_element(by=By.XPATH, value='//button[@id="rs-checkout-continue-button-bottom"]')
        button.click()

    def wait_button(self, by, value, text='') -> Optional:
        is_enabled = True
        while is_enabled:
            button = self.driver.find_element(by=by, value=value)
            if button.is_enabled() and (button.text == text if len(text) > 0 else True):
                button.click()
                is_enabled = False

    def shop_login(self) -> Optional:
        self.driver.get(self.url)
        settles = self.driver.find_elements(by=By.ID, value='shoppingCart.actions.navCheckout')
        if not settles:
            login_button = self.driver.find_element(
                by=By.XPATH, value='//div[@class="column rs-bagempty-button"]//a[@class="form-button"]')
            href = login_button.get_attribute('href')
            self.driver.get(href)
            self.agree_item()

            self.driver.switch_to.frame("aid-auth-widget-iFrame")
            email_input = self.driver.find_element(by=By.XPATH, value='//input[@id="account_name_text_field"]')
            email_input.send_keys(self.email)

            login_button = self.driver.find_element(by=By.ID, value='sign-in')
            login_button.click()

            login_button = self.driver.find_element(by=By.ID, value='password_text_field')
            login_button.send_keys(self.passwd)

            login = self.driver.find_element(by=By.ID, value='sign-in')
            login.click()

            self.driver.switch_to.default_content()
            settle = self.wait.until(EC.visibility_of_element_located((By.ID, 'shoppingCart.actions.navCheckout')))
        else:
            settle = settles[0]
        settle.click()


@retry(max_attempts=1000, wait_time=3)
def main():
    url = 'https://www.apple.com.cn/shop/bag'

    crawl = CrawlIphone(
        url=url,
        surname='徐',
        name='榕斌',

        passwd='RongIZai@2',
        email='844091758@qq.com',
        phone_num='17720741109',

        _choice_distinct=False,
        province='广东',
        city='深圳',
        distinct='龙华区',

        _remote=False,
    )
    crawl.run()


if __name__ == '__main__':
    main()
