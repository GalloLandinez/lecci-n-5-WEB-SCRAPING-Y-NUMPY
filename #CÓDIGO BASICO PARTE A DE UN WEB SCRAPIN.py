#CÓDIGO BASICO PARTE A DE UN WEB SCRAPING:

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup as bs
import pandas as pd
#configurar WBDRIVER para usarlo con CHROME
#www=webdriver.Chrome("DIR DE chromedriver.exe")
# Configurar el servicio de ChromeDriver
service = Service(r"C:\Users\HP-10\Downloads\chromedriver.exe")
# Inicializar el controlador de Chrome
driver = webdriver.Chrome(service=service)
m2=[]
# Ahora puedes usar 'driver' para navegar
driver.get("https://www.metrocuadrado.com/inmuebles/venta/")

#CÓDIGO BASICO PARTE B DE UN WEB SCRAPING:
#este código reconoce la estructura html de la página
#y guarda el contenido de la página en una variable
html_page= driver.page_source
#esta variable guarda toda la pagina en formato Beautifulsoup
ddd=bs(html_page, "html.parser")
for i in ddd.find_all("div",attrs={"class":"property-card__detail"}):
    m2.append(i.find("div",attrs={"class":"property-card__detail-price"}))
www=pd.DataFrame(m2)
print(www)