from bs4 import BeautifulSoup
import requests
import datetime

def scrapeGlobalCase():
    try:
        url = 'https://www.worldometers.info/coronavirus/'
        req = requests.get(url)
        bs_obj = BeautifulSoup(req.text, 'html.parser')
        data = bs_obj.find_all('div', class_='maincounter-number')
        num_confirmed = int(data[0].text.strip().replace(',', ''))
        num_deaths = int(data[1].text.strip().replace(',', ''))
        num_recovered = int(data[2].text.strip().replace(',', ''))
        num_active = num_confirmed - num_deaths - num_recovered
        time_now = datetime.datetime.now()
        
        return {'date': str(time_now), 'confirmed_cases': num_confirmed, 'active_cases': num_active, 'recovered_cases': num_recovered, 'deaths': num_deaths }
    except Exception as e:
        print(e)
    
# print(scrapeGlobalCase())