import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import lxml.html as html
from webdriver_manager.chrome import ChromeDriverManager

url='https://www.latamairlines.com/co/es/ofertas-vuelos?dataFlight=%7B%22tripTypeSelected%22%3A%7B%22label%22%3A%22Ida%20y%20Vuelta%22%2C%22value%22%3A%22RT%22%7D%2C%22cabinSelected%22%3A%7B%22label%22%3A%22Economy%22%2C%22value%22%3A%22Economy%22%7D%2C%22passengerSelected%22%3A%7B%22adultQuantity%22%3A1%2C%22childrenQuantity%22%3A0%2C%22infantQuantity%22%3A0%7D%2C%22originSelected%22%3A%7B%22id%22%3A%22BOG_CO_AIRPORT%22%2C%22name%22%3A%22El%20Dorado%20Intl.%22%2C%22city%22%3A%22Bogot%C3%A1%22%2C%22country%22%3A%22Colombia%22%2C%22iata%22%3A%22BOG%22%2C%22latitude%22%3A4.70159%2C%22longitude%22%3A-74.1469%2C%22timezone%22%3A-5%2C%22tz%22%3A%22America%2FBogota%22%2C%22type%22%3A%22AIRPORT%22%2C%22countryAlpha2%22%3A%22CO%22%2C%22airportIataCode%22%3A%22BOG%22%7D%2C%22destinationSelected%22%3A%7B%22id%22%3A%22SCL_CL_AIRPORT%22%2C%22name%22%3A%22A.%20Merino%20Benitez%20Intl.%22%2C%22city%22%3A%22Santiago%20de%20Chile%22%2C%22country%22%3A%22Chile%22%2C%22iata%22%3A%22SCL%22%2C%22latitude%22%3A-33.393001556396484%2C%22longitude%22%3A-70.78579711914062%2C%22timezone%22%3A-4%2C%22tz%22%3A%22America%2FSantiago%22%2C%22type%22%3A%22AIRPORT%22%2C%22countryAlpha2%22%3A%22CL%22%2C%22airportIataCode%22%3A%22SCL%22%7D%2C%22dateGoSelected%22%3A%222021-02-01T17%3A00%3A00.000Z%22%2C%22dateReturnSelected%22%3A%222021-02-28T17%3A00%3A00.000Z%22%2C%22redemption%22%3Afalse%7D&sort=RECOMMENDED'
r=requests.get(url)
print(r.status_code)
s=BeautifulSoup(r.text,'html.parser')

options=webdriver.ChromeOptions()
options.add_argument('--incognito')
driver= webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.get(url)

#driver.close()