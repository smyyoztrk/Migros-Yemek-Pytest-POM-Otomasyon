from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re
from pages.pagebase import Pagebase


class Restaurant(Pagebase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    MENU_YAZISI = (By.XPATH,"//div[@id='mat-tab-label-0-0']")
    CATEGORİLER = (By.CSS_SELECTOR,"div[class='header-wrapper'] div[class*='-star-inserted']")
    MENU_LISTESINDEKI_ICECEKLER = (By.CSS_SELECTOR,"div[class='header-wrapper'] div[class*='-star-inserted']:nth-child(6)")
    MENU_DETAY_SAYFASINDAKI_ICECEK_YAZISI = (By.XPATH,"//h3[@id='menu-header-İçecekler']")
    RESTORAN_ICINDEKI_ARAMA_CUBUGU = (By.XPATH,"//input[@class='ng-untouched ng-pristine ng-valid']")
    RESTORAN_ICINDEKI_URUN_ARATMADA_LISTELENEN_URUNLER = (By.XPATH,"//div[@class='subtitle-2 name']")
    LISTELENEN_URUNLERIN_FIYATLARI = (By.XPATH,"//div[@class='price-wrapper']/h3")
    RESTORAN_SECINCE_LISTELENEN_URUNLER = (By.XPATH,"//div[@class='subtitle-2 name']")
    SEPETE_EKLENEN_URUN = (By.XPATH,"//div[@class='total-price']/h3")


    def menu_sayfasinin_yazisini_ver(self):
        return self.wait_element_visibility_of(30,Restaurant.MENU_YAZISI)
    
    def categori_liste_ver(self):
        categoriler_webelement = self.wait_element_visibility_of_all(45,Restaurant.CATEGORİLER)
        categoriler_liste = []
        for i in categoriler_webelement:
            categoriler_liste.append(i.text)
        return categoriler_liste
    
    def menu_listesindeki_icecekler_elementine_tikla(self):
        icecekler_webelement = self.wait_element_visibility_of(30,Restaurant.MENU_LISTESINDEKI_ICECEKLER)
        icecekler_webelement.click()

    def menu_detay_sayfasindaki_icecek_yazisini_ver(self):
        return self.wait_element_visibility_of(30,Restaurant.MENU_DETAY_SAYFASINDAKI_ICECEK_YAZISI)
    def restoran_arama_cubugunda_urun_arat(self):
        arama_cubugu_webelement = self.wait_element_visibility_of(30,Restaurant.RESTORAN_ICINDEKI_ARAMA_CUBUGU)
        actions = ActionChains(self.driver)
        actions.move_to_element(arama_cubugu_webelement)
        arama_cubugu_webelement.send_keys("et burger")
        arama_cubugu_webelement.send_keys(Keys.ENTER)
    def urun_aratinca_listenen_urunleri_ver(self):
        return self.wait_element_visibility_of_all(30,Restaurant.RESTORAN_ICINDEKI_URUN_ARATMADA_LISTELENEN_URUNLER)
    def listelenen_urunlerin_fiyatlarini_liste_ver(self):
        return self.wait_element_visibility_of_all(30,Restaurant.LISTELENEN_URUNLERIN_FIYATLARI)


    def varsayilan_urunler_liste_ver(self):
        return self.wait_element_visibility_of_all(30,Restaurant.RESTORAN_SECINCE_LISTELENEN_URUNLER)

    def sepete_eklenen_urun_fiyatini_integera_cevir(self):
        sepete_eklenen_urun_fiyati_webelement = self.wait_element_visibility_of(15,Restaurant.SEPETE_EKLENEN_URUN)

        sepete_eklenen_urun_fiyati_webelement_text = sepete_eklenen_urun_fiyati_webelement.text
        return int(re.search(r'\d+',sepete_eklenen_urun_fiyati_webelement_text).group())
    def sepete_eklenecek_urunu_ver(self):
        return self.wait_element_visibility_of_all(30,Restaurant.RESTORAN_SECINCE_LISTELENEN_URUNLER)
    def listede_ikinci_siradaki_urune_tikla(self):
        urunler_liste = self.varsayilan_urunler_liste_ver()
        urunler_liste[2].click()

    