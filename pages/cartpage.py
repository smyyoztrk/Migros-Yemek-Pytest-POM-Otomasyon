from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re
from pages.pagebase import Pagebase

class Cart(Pagebase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    
    SEPETE_EKLE_BUTONU = (By.XPATH,"//span[text()=' Sepete Ekle ']")
    SEPETTEN_SİLME_İKONU = (By.XPATH,"//div[@id='cart-page-item-remove']")
    SEPETTEKI_URUN = (By.XPATH,"//a[@class='subtitle-2 text-color-black text-decoration-ellipsis ng-star-inserted']")
    SEPETTEKI_URUN_FIYATI = (By.XPATH,"//div[@class='product-price desktop-only']//span[@id='new-amount']")
    SEPETTEKI_URUN_MIKTARI = (By.XPATH,"(//span[@class='amount mat-caption'])[2]")
    SEPETTE_ARTI_IKONU = (By.XPATH,"(//button[@class='product-increase'])[2]")
    SEPETTE_EKSI_IKONU = (By.XPATH,"(//button[@class='product-decrease'])[2]")
    
    
    def sepete_ekle_butonuna_tikla(self):
        sepete_ekle_butonu = self.wait_element_visibility_of(30,Cart.SEPETE_EKLE_BUTONU)
        sepete_ekle_butonu.click()
    def sepetten_urunu_tamamen_sil(self):
        delete_icon_from_cart = self.wait_element_visibility_of(30,Cart.SEPETTEN_SİLME_İKONU)
        delete_icon_from_cart.click()
    def urunun_sepette_gorunurlugunu_bool_dondur(self,by_location):
        return self.wait_until_not_visibility_of(30,by_location)
    def sepetteki_urun_elementini_ver(self):
        return self.wait_element_visibility_of(30,Cart.SEPETTEKI_URUN)
    def sepetteki_urun_fiyatini_integera_cevir_ver(self):
        sepetteki_urun_fiyatı = self.wait_element_visibility_of(30,Cart.SEPETTEKI_URUN_FIYATI)
        sepetteki_urun_fiyatı_text = sepetteki_urun_fiyatı.text

        sepetteki_fiyat_part = int(re.search(r'\d+',sepetteki_urun_fiyatı_text).group())
        return sepetteki_fiyat_part
    def sepetteki_urun_miktarini_ver(self):
        return self.wait_element_visibility_of(30,Cart.SEPETTEKI_URUN_MIKTARI)
    def sepetteki_urun_miktarini_arttir(self):
        arttırma_iconu = self.wait_element_visibility_of(30,Cart.SEPETTE_ARTI_IKONU)
        arttırma_iconu.click()
    def sepetteki_urun_miktarini_azalt(self):
        eksiltme_iconu = self.wait_element_visibility_of(30,Cart.SEPETTE_EKSI_IKONU).click()
    



