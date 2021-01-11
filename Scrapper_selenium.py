import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import lxml.html as html
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def obtener_info_completa(driver):
    vuelos=driver.find_elements_by_xpath('//li[@class="sc-fHSTwm danPdA"]')
    print(len(vuelos))
    info1=[]
    for v in vuelos:
        #obtener info tiempos generales
        tiempos= obtener_tiempos(v)
        boton=v.find_element_by_xpath('.//div[@class="sc-iuDHTM gHiWYR"]/div/a/span[@aria-hidden="true"]')
        boton.click()
        escalas=obtener_escalas(v)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="MuiDialog-container MuiDialog-scrollPaper"]//button[@class="MuiButtonBase-root MuiIconButton-root sc-dNLxif cnFxBf"]'))).click()
        v.click()
        precios=obtener_precios(v)
        boton=v.find_element_by_xpath('.//button[@class="MuiButtonBase-root MuiButton-root MuiButton-text xp-Button-null MuiButton-textSizeSmall MuiButton-sizeSmall MuiButton-disableElevation"]')
        boton.click()
        info1.append({"tiempo":tiempos,'escalas':escalas,'precios':precios})    
    return info1

def obtener_tiempos(vuelo):
    info_vuelo=[]
    datos=vuelo.find_elements_by_xpath('.//span[@class="sc-lnmtFM ewiHQE"]')
    hora_salida=datos[0].text
    hora_llegada=datos[1].text
    duracion=vuelo.find_element_by_xpath('.//span[@class="sc-FQuPU dkpBdw"]').text
    data_dict={'hora_salida':hora_salida,'hora_llegada':hora_llegada,'duracion':duracion}
    info_vuelo.append(data_dict)
    return info_vuelo

def obtener_escalas(vuelo):
    segmentos= vuelo.find_elements_by_xpath('//div[@aria-hidden="true"]//section[@data-test="section-info-leg"]')
    escalas=len(segmentos)
    return escalas

def obtener_precios(vuelo):
    tarifas= vuelo.find_elements_by_xpath('//ol[@aria-label="Tarifas disponibles."]/div//span[@class="sc-cFlXAS lhMviV"]')
    valores= vuelo.find_elements_by_xpath('//ol[@aria-label="Tarifas disponibles."]/div//span[@class="sc-dRCTWM frWsLu displayAmount"]')
    t=len(tarifas)
    precios=[]
    i=0
    while i< t:
        nombre=tarifas[i].text
        valor= valores[i].text
        dict_tarifas={nombre:{'valor':valor}}
        precios.append(dict_tarifas)
        i=i+1
    return precios


url='https://www.latamairlines.com/co/es/ofertas-vuelos?dataFlight=%7B%22tripTypeSelected%22%3A%7B%22label%22%3A%22Ida%22%2C%22value%22%3A%22OW%22%7D%2C%22cabinSelected%22%3A%7B%22label%22%3A%22Economy%22%2C%22value%22%3A%22Economy%22%7D%2C%22passengerSelected%22%3A%7B%22adultQuantity%22%3A1%2C%22childrenQuantity%22%3A0%2C%22infantQuantity%22%3A0%7D%2C%22originSelected%22%3A%7B%22id%22%3A%22SCL_CL_AIRPORT%22%2C%22name%22%3A%22A.%20Merino%20Benitez%20Intl.%22%2C%22city%22%3A%22Santiago%20de%20Chile%22%2C%22country%22%3A%22Chile%22%2C%22iata%22%3A%22SCL%22%2C%22latitude%22%3A-33.393001556396484%2C%22longitude%22%3A-70.78579711914062%2C%22timezone%22%3A-4%2C%22tz%22%3A%22America%2FSantiago%22%2C%22type%22%3A%22AIRPORT%22%2C%22countryAlpha2%22%3A%22CL%22%2C%22airportIataCode%22%3A%22SCL%22%7D%2C%22destinationSelected%22%3A%7B%22id%22%3A%22MAD_ES_AIRPORT%22%2C%22name%22%3A%22Barajas%20Intl.%22%2C%22city%22%3A%22Madrid%22%2C%22country%22%3A%22Espa%C3%B1a%22%2C%22iata%22%3A%22MAD%22%2C%22latitude%22%3A40.471926%2C%22longitude%22%3A-3.56264%2C%22timezone%22%3A1%2C%22tz%22%3A%22Europe%2FMadrid%22%2C%22type%22%3A%22AIRPORT%22%2C%22countryAlpha2%22%3A%22ES%22%2C%22airportIataCode%22%3A%22MAD%22%7D%2C%22dateGoSelected%22%3A%222021-04-01T16%3A00%3A00.000Z%22%2C%22dateReturnSelected%22%3Anull%2C%22redemption%22%3Afalse%7D&sort=RECOMMENDED'
r=requests.get(url)
print(r.status_code)
s=BeautifulSoup(r.text,'html.parser')
options=webdriver.ChromeOptions()
options.add_argument('--incognito')
driver= webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.get(url)
info=obtener_info_completa(driver)
i=0
for f in info:
    print("vuelo" ,i+1)    
    print(f)
    print("\n")
    i=i+1



    
#boton=driver.find_element_by_xpath('//div[@class="MuiDialog-container MuiDialog-scrollPaper"]//button[@class="MuiButtonBase-root MuiIconButton-root sc-dNLxif cnFxBf"]')
#print("Element is visible? " + str(boton.is_displayed()))
#boton=driver.find_element_by_xpath('//div[@class="MuiDialog-container MuiDialog-scrollPaper"]//button[@class="MuiButtonBase-root MuiIconButton-root sc-dNLxif cnFxBf"]')
#print("Element is visible? " + str(boton.is_displayed()))
#driver.close()
#ActionChains(driver).move_to_element(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "boton_css")))).click().build().perform()
#webdriver.ActionChains(driver).move_to_element(boton).click(boton).perform()
#boton=driver.find_element_by_class_name(u"MuiButtonBase-root MuiIconButton-root sc-dNLxif cnFxBf")
#driver.implicitly_wait(10)


#$x('//ol[@aria-label="Tarifas disponibles."]/div//span[@class="sc-dRCTWM frWsLu displayAmount"]/text()').map(x=>x.wholeText)
