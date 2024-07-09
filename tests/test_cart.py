from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import re
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pytest
from pages.anasayfa import Anasayfa
from pages.restoranpage import Restaurant
from pages.cartpage import Cart
from constants import globalconstants as c

# @pytest.mark.usefixtures("setup")
class TestCart:
    def setup_method(self):   #her test başlangıcında çalışacak fonk.
        self.driver = webdriver.Chrome()
        self.driver.get(c.BASE_URL)
        self.driver.maximize_window()

    def teardown_method(self):  # her testin btiminde çalışacak fonk
        self.driver.quit()
    # bu satır gbt den
    @pytest.mark.parametrize("product_index", [0, 1, 2])
    def test_add_to_cart(self,product_index):
        anasayfa = Anasayfa(self.driver)
        restaurant = Restaurant(self.driver)
        try:
            anasayfa.adres_arama_cubuguna_adres_gir()
        except:
            pass

        anasayfa.anasayfada_restoran_arat(restoranAdi="sarmaşık kebap")
        anasayfa.restoran_sec_sarmasik_cart_sayfasi_icin()
        sleep(1)
        # menu_webelement = restaurant.menu_sayfasinin_yazisini_ver()
        # assert menu_webelement.is_displayed()

        urunler_liste = restaurant.varsayilan_urunler_liste_ver()
        sepete_eklenen_urun_adi = urunler_liste[product_index].text
        urunler_liste[product_index].click()

        product_price = restaurant.sepete_eklenen_urun_fiyatini_integera_cevir()
        
        cart = Cart(self.driver)
        cart.sepete_ekle_butonuna_tikla()
       

        anasayfa.sepet_iconuna_tikla()
        sepetteki_urun = cart.sepetteki_urun_elementini_ver()
        sepetteki_urun_adi = sepetteki_urun.text


        sepetteki_urun_fiyati_int = cart.sepetteki_urun_fiyatini_integera_cevir_ver()

        assert sepete_eklenen_urun_adi == sepetteki_urun_adi
        assert product_price == sepetteki_urun_fiyati_int
    def test_remove_from_cart(self):
        anasayfa = Anasayfa(self.driver)
        try:
            anasayfa.adres_arama_cubuguna_adres_gir()
        except:
            pass

        anasayfa.anasayfada_restoran_arat(restoranAdi="sarmaşık kebap")
        anasayfa.restoran_sec_sarmasik_cart_sayfasi_icin()

        urunler_liste = WebDriverWait(self.driver,15).until(EC.visibility_of_all_elements_located((By.XPATH,"//div[@class='subtitle-2 name']")))
        urunler_liste[2].click()

        cart = Cart(self.driver)
        cart.sepete_ekle_butonuna_tikla()
       
       
        anasayfa.sepet_iconuna_tikla()
        cart.sepetten_urunu_tamamen_sil()
    
        urunler_liste = cart.urunun_sepette_gorunurlugunu_bool_dondur((By.XPATH,"(//div[@class='subtitle-2 name'])[3]"))
        assert urunler_liste

    def test_change_quantity(self):
        anasayfa = Anasayfa(self.driver)
        restaurant = Restaurant(self.driver)
        try:
            anasayfa.adres_arama_cubuguna_adres_gir()
        except:
            pass

        anasayfa.anasayfada_restoran_arat(restoranAdi="sarmaşık kebap")
        anasayfa.restoran_sec_sarmasik_cart_sayfasi_icin()
        urunler_liste = restaurant.varsayilan_urunler_liste_ver()
        
        restaurant.listede_ikinci_siradaki_urune_tikla()

        cart = Cart(self.driver)
        cart.sepete_ekle_butonuna_tikla()
        
        anasayfa.sepet_iconuna_tikla()

        sepetteki_urun_miktari= cart.sepetteki_urun_miktarini_ver()
        arttirma_yapmadan_onceki_adet = sepetteki_urun_miktari.text

        cart.sepetteki_urun_miktarini_arttir()

        arttirma_yaptiktan_sonraki_adet = cart.sepetteki_urun_miktarini_ver().text
        assert arttirma_yaptiktan_sonraki_adet > arttirma_yapmadan_onceki_adet

        cart.sepetteki_urun_miktarini_azalt()
        assert int(arttirma_yaptiktan_sonraki_adet) == int(arttirma_yaptiktan_sonraki_adet)

        

       


