from datetime import datetime
from time import sleep, strftime
from random import randint
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup as bs
import h5py
import numpy as np
import datetime
import os

PATH = "D:\descargas\chromedriver.exe"
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options= options, executable_path = PATH)
sleep(2)
file_path = 'D:\Data quality data wrangling\web_scraping_all.csv'
col_names = ['id', 'web']
url_df = pd.read_csv(file_path, names = col_names, sep = ';')




kayak = url_df['web'].iloc[0]

driver.get(kayak)
sleep(20)

#close the pop up window about privacy
pop_window = '//div[@class="dDYU-close dDYU-mod-variant-default dDYU-mod-size-default"]'
driver.find_element("xpath", pop_window).click()

# find the flights and select the information we want
flight_rows = driver.find_elements("xpath", '//div[@class="inner-grid keel-grid"]')
print(flight_rows)

list_prices = []
list_cabine_luggage = []
list_company_names = []

for WebElement in flight_rows:
    elementHTML = WebElement.get_attribute('outerHTML')
    elementSoup = bs( elementHTML, 'html.parser')

    # price
    temp_price = elementSoup.find("div", {"class" : "col-price result-column js-no-dtog"})
    price = temp_price.find("span", {"class":"price-text"} )
    list_prices.append(price.text)

    #cabine luggage included 
    #temp_cabine_luggage = elementSoup.find("div", {"class" : "Flights-Results-FlightFeeIcons _iai"})
    #cabine_luggage = temp_cabine_luggage.find("div", {"class" : "_h-8 _iab _jw2 _h5"})
    #list_cabine_luggage.append(cabine_luggage.text)

    # list of airlines
    airline_names = elementSoup.find("span", {"class": "codeshares-airline-names"}).text
    list_company_names.append(airline_names)

print(list_prices)
print(list_cabine_luggage)
print(list_company_names)

# create kayak_scrapped_data.h5: 
'''
if file_exists==False:
    with h5py.File('D:\Data quality data wrangling\web_scraped_kaya.hdf5','w') as hf:
        hf.create_dataset("Price", maxshape=(None,), data=list_prices, chunks = True)
        hf.create_dataset("Cabine luggage", maxshape=(None,), data=list_cabine_luggage, chunks = True)
        hf.create_dataset("Airlane company", maxshape=(None,), data= list_company_names, chunks = True)
        hf.attrs["User"] = "Jairo Gonzalez"
        h5py.File.close(hf)
  

else:
    with h5py.File('D:\Data quality data wrangling\web_scraped_kaya.hdf5','a') as hf: 
        hf["Price"].resize((hf["Price"].shape[0] + np.asarray(list_prices).shape[0]), axis = 0)
        hf["Price"][-np.asarray(list_prices).shape[0]:] = list_prices

        hf["Cabine luggage"].resize((hf["Cabine luggage"].shape[0] + np.asarray(list_cabine_luggage).shape[0]), axis = 0)
        hf["Cabine luggage"][-np.asarray(list_cabine_luggage).shape[0]:] = list_cabine_luggage

        hf["Airlane company"].resize((hf["Airlane company"].shape[0] + np.asarray(list_company_names).shape[0]), axis = 0)
        hf["Airlane company"][-np.asarray(list_company_names).shape[0]:] = list_company_names

        h5py.File.close(hf)'''
        
sleep(10)
# same code for the skyscanner
edreams = url_df['web'].iloc[1]

driver.get(edreams)
sleep(25)


pop_up = '//*[@id="didomi-notice-agree-button"]'

driver.find_element("xpath", pop_up ).click()
# find the flights and select the information we want
flight_rows_edreams = driver.find_elements("xpath", '//div[@class="css-34j4b3-Box e17fzqxg0"]')
print(flight_rows_edreams)


# create kayak_scrapped_data.h5: 

list_prices_edreams = []
list_seats_edreams = []
list_company_names_edreams = []

for WebElement in flight_rows_edreams:
    elementHTML = WebElement.get_attribute('outerHTML')
    elementSoup = bs( elementHTML, 'html.parser')

    # price
    #temp_price = elementSoup.find("div", {"class" : "styles__PriceContainer-sc-1hhvl2t-2 gQWYxt"})
    #temp_price = elementSoup.find("div", {"class" : "css-5wgyez-Box e17fzqxg0"})
    price = elementSoup.find("span", {"class" : "css-1iu0vlo-StyledContainer e16uabde3"})
    list_prices_edreams.append(price.text)
    

 
    # list of airlines
    airline_names = elementSoup.find("div", {"class": "css-1um4vyc-BaseText-Body e8tl7c60"}).text
    list_company_names_edreams.append(airline_names)

print(list_prices_edreams, list_company_names_edreams)


# create kayak_scrapped_data.h5: 


sleep(10)

atrapalo = url_df['web'].iloc[2]

driver.get(atrapalo)
waiting_time = randint(20,30)
sleep(waiting_time)

# find the flights and select the information we want
flight_rows_atrapalo = driver.find_elements("xpath", '//div[@class="sc-papXJ styles__GridWithoutPadding-sc-pp754f-4 bzkfVv hAgvqZ"]')

print(flight_rows_atrapalo)

# create kayak_scrapped_data.h5: 

list_prices_atrapalo = []

list_company_names_atrapalo = []

for WebElement in flight_rows_atrapalo:
    elementHTML = WebElement.get_attribute('outerHTML')
    elementSoup = bs( elementHTML, 'html.parser')

    # price
    
    price = elementSoup.find("span", {"class" : "sc-hAZoDl eAxILV styles__Price-sc-1hhvl2t-3 kiYAXQ"}).text
    list_prices_atrapalo.append(price)
    

 
    # list of airlines
    airline_names = elementSoup.find("span", {"class": "sc-hAZoDl eAxILV CompanyName-sc-1dl04th-0 jMMcFH"}).text
    list_company_names_atrapalo.append(airline_names)

print(list_prices_atrapalo)

print(list_company_names_atrapalo)



L = [list_company_names, list_prices, list_company_names_atrapalo, list_prices_atrapalo, list_prices_edreams, list_company_names_edreams]
Prices_list = [list_prices, list_prices_atrapalo, list_prices_edreams]
Airline = [list_company_names, list_company_names_atrapalo, list_company_names_edreams]
K = {"Price": Prices_list, "Airline" : Airline}
d = {"Price kayak": list_prices, "Price Atrapalo" : list_prices_atrapalo, "Price edreams" : list_prices_edreams, "Airline edreams" : list_company_names_edreams, "Airline kayak" : list_company_names, "Airline atrapalo" : list_company_names_atrapalo}
dataframe = pd.DataFrame.from_dict(d, orient = 'index')
dataframe.transpose()
dataframe = dataframe.astype(str)
print(dataframe)



h5File =  str(datetime.date.today()) + "fromdf.h5" 
print(h5File)

dataframe.to_hdf(h5File, key= 'df', mode = 'a')

path = os.path.abspath(h5File)
directory = os.path.dirname(path)
print(directory)


file_exists = os.path.exists('D:\Data quality data wrangling\web_scraped_kayak.hdf5')
if file_exists==False:
    with h5py.File('D:\Data quality data wrangling\web_scraped_kaya.hdf5','w') as hf:
        hf.create_dataset("Price", maxshape=(None,), data=list_prices, chunks = True)
        hf.create_dataset("Airlane company", maxshape=(None,), data= list_company_names, chunks = True)
        hf.attrs["User"] = "Jairo Gonzalez"
        hf["Price"].resize((hf["Price"].shape[0] + np.asarray(list_prices_edreams).shape[0]), axis = 0)
        hf["Price"][-np.asarray(list_prices_edreams).shape[0]:] = list_prices_edreams

        hf["Airlane company"].resize((hf["Airlane company"].shape[0] + np.asarray(list_company_names_edreams).shape[0]), axis = 0)
        hf["Airlane company"][-np.asarray(list_company_names_edreams).shape[0]:] = list_company_names_edreams
  
        hf["Price"].resize((hf["Price"].shape[0] + np.asarray(list_prices_atrapalo).shape[0]), axis = 0)
        hf["Price"][-np.asarray(list_prices_atrapalo).shape[0]:] = list_prices_atrapalo

        hf["Airlane company"].resize((hf["Airlane company"].shape[0] + np.asarray(list_company_names_atrapalo).shape[0]), axis = 0)
        hf["Airlane company"][-np.asarray(list_company_names_atrapalo).shape[0]:] = list_company_names_atrapalo

        hf["Price"].resize((hf["Price"].shape[0] + np.asarray(list_prices).shape[0]), axis = 0)
        hf["Price"][-np.asarray(list_prices).shape[0]:] = list_prices

        hf["Airlane company"].resize((hf["Airlane company"].shape[0] + np.asarray(list_company_names).shape[0]), axis = 0)
        hf["Airlane company"][-np.asarray(list_company_names).shape[0]:] = list_company_names
        h5py.File.close(hf)

else:
    with h5py.File('D:\Data quality data wrangling\web_scraped_kaya.hdf5','a') as hf: 
        hf["Price"].resize((hf["Price"].shape[0] + np.asarray(list_prices_edreams).shape[0]), axis = 0)
        hf["Price"][-np.asarray(list_prices_edreams).shape[0]:] = list_prices_edreams

        hf["Airlane company"].resize((hf["Airlane company"].shape[0] + np.asarray(list_company_names_edreams).shape[0]), axis = 0)
        hf["Airlane company"][-np.asarray(list_company_names_edreams).shape[0]:] = list_company_names_edreams
  
        hf["Price"].resize((hf["Price"].shape[0] + np.asarray(list_prices_atrapalo).shape[0]), axis = 0)
        hf["Price"][-np.asarray(list_prices_atrapalo).shape[0]:] = list_prices_atrapalo

        hf["Airlane company"].resize((hf["Airlane company"].shape[0] + np.asarray(list_company_names_atrapalo).shape[0]), axis = 0)
        hf["Airlane company"][-np.asarray(list_company_names_atrapalo).shape[0]:] = list_company_names_atrapalo

        hf["Price"].resize((hf["Price"].shape[0] + np.asarray(list_prices).shape[0]), axis = 0)
        hf["Price"][-np.asarray(list_prices).shape[0]:] = list_prices

        hf["Airlane company"].resize((hf["Airlane company"].shape[0] + np.asarray(list_company_names).shape[0]), axis = 0)
        hf["Airlane company"][-np.asarray(list_company_names).shape[0]:] = list_company_names
        h5py.File.close(hf)

df = pd.read_hdf('D:\Data quality data wrangling\web_scraped_kaya.hdf5')
print(df)       

print("end")