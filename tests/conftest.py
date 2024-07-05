from selenium import webdriver
import pytest
from constants import globalconstants as c

@pytest.fixture(scope="class")
def setup(request):
    driver=webdriver.Chrome()
    driver.get(c.BASE_URL)
    driver.maximize_window()
    request.cls.driver = driver # bu fixture kullanan class lar driver çağırdığında driver = webdriver.Chrome() u ver dedik.  
    yield
    driver.quit()

