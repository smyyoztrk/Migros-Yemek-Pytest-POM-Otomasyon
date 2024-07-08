from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import json
from pages.pagebase import Pagebase

class Anasayfa(Pagebase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        
    ADRES_GIRME_CUBUGU = (By.XPATH,"(//input[@type='text'])[2]")
    ACILIR_LISTEDE_CIKAN_ADRES = (By.XPATH,"(//li[@class='mat-caption-normal'])[1]")
    ISARETLEDIGIM_KONUM_ILE_GUNCELLE_BUTONU = (By.XPATH,"(//span[@class='mdc-button__label'])[2]")
    ADRESIM_DOGRU_BUTONU = (By.XPATH,"(//span[@class='mdc-button__label'])[1]")
    RESTAURANT_66 = (By.XPATH,"//a[@href='/yemek/66-burger-sancaktepe-meclis-mah-st-1dfa4']")
    RESTORAN_SARMASIK = (By.XPATH,"//a[@href='/yemek/sarmasik-kebap-doner-et-lokantasi-sancaktepe-sarigazi-mah-st-1bb70']")
    SEPET_IKONU = (By.XPATH,"//div[@id='homepage-cart-button']")
    UYE_OLMADAN_DEVAM_ET_BUTONU = (By.XPATH,"(//span[@class='mdc-button__label'])[3]")
    RESTORAN_ARAMA_MOTORU = (By.XPATH,"//input[@id='product-search-combobox--trigger']") 
    TUMUNU_KABULET_BUTONU = (By.XPATH,"//button[@id='accept-all']")

    def adres_arama_cubuguna_adres_gir(self):
        adres_girme_input = self.wait_element_visibility_of(30,Anasayfa.ADRES_GIRME_CUBUGU)
        
        adres_girme_input.send_keys("sancaktepe refah cad")
        adres_girme_input.send_keys(Keys.ENTER)
        adres =self.wait_element_visibility_of(15,Anasayfa.ACILIR_LISTEDE_CIKAN_ADRES).click()
        
        isareledigim_konum_ile_guncelle_butonu = WebDriverWait(self.driver,15).until(EC.element_to_be_clickable(Anasayfa.ISARETLEDIGIM_KONUM_ILE_GUNCELLE_BUTONU))
        
        isareledigim_konum_ile_guncelle_butonu.click()
        adresim_dogru_buton = self.wait_element_of_be_clikcable(30,Anasayfa.ADRESIM_DOGRU_BUTONU)
        adresim_dogru_buton.click()
        tumunu_kabulet_buton = self.wait_element_of_be_clikcable(20,Anasayfa.TUMUNU_KABULET_BUTONU)
        tumunu_kabulet_buton.click()
        actions = ActionChains(self.driver)
        actions.move_by_offset(10, 10).click()
        sleep(1)
        actions.move_by_offset(10, 10).click()
        sleep(1)
        actions.move_by_offset(10,10).click().perform()
        sleep(2)
    def uye_olmadan_devamet_butonuna_tikla(self):
        uye_olmadan_devamet_buton = self.wait_element_of_be_clikcable(30,Anasayfa.UYE_OLMADAN_DEVAM_ET_BUTONU)
        uye_olmadan_devamet_buton.click()
    def anasayfada_restoran_arat(self,restoranAdi):
        anasayfa_arama_motoru = self.wait_element_visibility_of(30,Anasayfa.RESTORAN_ARAMA_MOTORU).click()
        sleep(2)
        self.uye_olmadan_devamet_butonuna_tikla()
        sleep(2)
        anasayfa_arama_motoru = self.wait_element_visibility_of(30,Anasayfa.RESTORAN_ARAMA_MOTORU)
        anasayfa_arama_motoru.send_keys(restoranAdi)
        anasayfa_arama_motoru.send_keys(Keys.ENTER)

        
    def restoran_sec_66_restoranı_menu_sayfasi_icin(self):
        restaurant_webelement = self.wait_element_of_presence(30,Anasayfa.RESTAURANT_66)
        actions = ActionChains(self.driver)
        actions.move_to_element(restaurant_webelement)
        actions.click(restaurant_webelement)
        actions.perform()
    def restoran_sec_sarmasik_cart_sayfasi_icin(self):
        restaurant_webelement = self.wait_element_of_presence(30,Anasayfa.RESTORAN_SARMASIK)
        actions = ActionChains(self.driver)
        actions.move_to_element(restaurant_webelement)
        actions.click(restaurant_webelement)
        actions.perform()
    

    def sepet_iconuna_tikla(self):
        sepet = self.wait_element_visibility_of(30,Anasayfa.SEPET_IKONU)
        sepet.click()
        sleep(3)

    


