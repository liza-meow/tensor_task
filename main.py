
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://sbis.ru/'

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def go_to_link(self, link):
        return self.driver.get(link)

class SbisElementsLocators:
    LOCATOR_CONTACTS_LINK = (By.LINK_TEXT, 'Контакты')
    LOCATOR_TENSOR_BANNER = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[1]/div/div/div[2]/div/a')
    LOCATOR_REGION = (By.CLASS_NAME, 'sbis_ru-Region-Chooser__text')
    LOCATOR_PARTNERS = (By.CLASS_NAME, 'controls-ListViewV__itemsContainer')
    LOCATOR_CHOICE_REGION = (By.CLASS_NAME, 'sbis_ru-Region-Panel__list')
    LOCATOR_KAMCHATKA = (By.XPATH, '//*[.="41 Камчатский край"]')
    LOCATOR_DOWNLOAD_SBIS_PAGE = (By.XPATH, '//a[.="Скачать СБИС"]')
    LOCATOR_TAB_SBIS_PLUGIN = (By.CLASS_NAME, 'controls-tabButton__overlay')
    LOCATOR_DOWNLOAD_LINK = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/a')

class SbisActionHelper(BasePage):

    def check_region(self):
        return True if SbisElementsLocators.LOCATOR_REGION else False

    def check_partners(self):
        return True if SbisElementsLocators.LOCATOR_PARTNERS else False


    def swap_region(self):
        self.find_element(SbisElementsLocators.LOCATOR_KAMCHATKA).click()

    def check_swap_region(self):
        counter = [True if 'Камчат' in self.driver.title else False,
                   True if '41-kamchatskij-kraj' in self.driver.current_url else False,
                   True if 'Камчат' in self.find_element(SbisElementsLocators.LOCATOR_REGION).text else False,
                   True if 'Камчат' in self.find_element(SbisElementsLocators.LOCATOR_PARTNERS).text else False
                   ]

        return True if counter.count(True) == len(counter) else False



def test_second_case(browser):
    sbis_main_page = SbisActionHelper(browser)
    sbis_main_page.go_to_site()
    time.sleep(3)
    sbis_main_page.find_element(SbisElementsLocators.LOCATOR_CONTACTS_LINK).click()
    time.sleep(3)



    sbis_main_page.find_element(SbisElementsLocators.LOCATOR_REGION).click()
    time.sleep(3)
    sbis_main_page.swap_region()
    time.sleep(3)





"""browser = webdriver.Chrome()
browser.get('https://sbis.ru/contacts/76-yaroslavskaya-oblast?tab=clients')
a = browser.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
if a.text == 'Ярославская обл.':
    print('Область определяется правильно')
else: print('Область определяется неправильно')


browser.quit()
browser = webdriver.Chrome()
browser.get('https://sbis.ru/contacts/76-yaroslavskaya-oblast?tab=clients')
sleep(2)
browser.find_element(By.XPATH, '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a/img').click()
sleep(2)
a = browser.find_element(By.XPATH, "//*[contains(text(), 'Сила в людях')]").text
#POWER_IN_PEOPLE = ()
#browser.find_element(By.LINK_TEXT, ("Подробнее")).click()
sleep(5)
print(a)
#assert "Сила в людях" in browser.page_source"""



