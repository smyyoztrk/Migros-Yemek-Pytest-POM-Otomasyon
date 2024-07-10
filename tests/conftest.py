from selenium import webdriver
import pytest
from constants import globalconstants as c
from pages.anasayfa import Anasayfa

# @pytest.fixture(scope="class") # class başında bir kere çalışır tüm testler koşar kapanır.
@pytest.fixture() # her test için çalışır
def setup(request):
    driver=webdriver.Chrome()
    driver.get(c.BASE_URL)
    driver.maximize_window()
    request.cls.driver = driver # bu fixture kullanan class lar driver çağırdığında driver = webdriver.Chrome() u ver dedik.  
    anasayfa = Anasayfa(driver)
    try:
        anasayfa.adres_arama_cubuguna_adres_gir()
    except:
        pass
    anasayfa.anasayfada_restoran_arat(restoranAdi="sarmaşık kebap")
    anasayfa.restoran_sec_sarmasik_cart_sayfasi_icin()
    yield
    driver.quit()



