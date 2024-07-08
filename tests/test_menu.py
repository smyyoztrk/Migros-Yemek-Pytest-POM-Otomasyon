from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pages.anasayfa import Anasayfa
from pages.restoranpage import Restaurant
from constants import globalconstants as c
import json
from typing import List, Tuple


@pytest.mark.usefixtures("setup")
class TestMenu:

    
    def readMenuListesiFromJson():

        file = open("data/menu_listesi.json") 
        data = json.load(file)
        parameter = []

        for menu in data['menu_listesi']:
            menu_adi = menu["menu_adi"]
            parameter.append((menu_adi))
        return parameter
    
    @pytest.mark.parametrize("menu_adi",readMenuListesiFromJson())
    def test_view_menu_by_category(self,menu_adi):
        anasayfa = Anasayfa(self.driver)
        

        restaurant = Restaurant(self.driver)
        menu_webelement = restaurant.menu_sayfasinin_yazisini_ver()
        assert menu_webelement.is_displayed()

        categoriler_liste = restaurant.categori_liste_ver()

        assert menu_adi in categoriler_liste
        assert len(categoriler_liste) > 0

        restaurant.menu_listesindeki_icecekler_elementine_tikla()

        icecek_yazisi = restaurant.menu_detay_sayfasindaki_icecek_yazisini_ver()
        assert icecek_yazisi.is_displayed()

   
    def test_search_menu_items(self):
        restaurant = Restaurant(self.driver)
        restaurant.restoran_arama_cubugunda_urun_arat()

        listelenen_urunler = restaurant.urun_aratinca_listenen_urunleri_ver()
        assert all("et döner" in urun.text.lower() for urun in listelenen_urunler)

    def test_item_prices(self):
        anasayfa = Anasayfa(self.driver)
        restaurant = Restaurant(self.driver)
       
        urun_fiyatlari_liste_webelement = restaurant.listelenen_urunlerin_fiyatlarini_liste_ver()
        for i in urun_fiyatlari_liste_webelement:
            assert "TL" in i.text
  

