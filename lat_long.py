
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
BASE_URL="https://www.google.com/search?q="
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
#function to scrape latitude and longitude
def get_coordinates(sector):
    search_term=f"sector {sector} gurgaon longitude and latitude"
    response=requests.get(BASE_URL+search_term,headers=headers)
    if response.status_code==200:
        soup=BeautifulSoup(response.content,'html.parser')
        coordinates_div=soup.find("div",class_="Z0LcW t2b5Cf")
        if coordinates_div:
            return coordinates_div.text

    return None
#creating a data frame
df=pd.DataFrame(columns=["Sector","coordinates"])
for sector in range(1,116):
    coordinates=get_coordinates(sector)
    df=df.append({"Sector":f"sector{sector}","coordinates":coordinates},ignore_index=True)
    time.sleep(2)
#save data frame
df.to_csv("gurgaon_sectors_coordinates.csv",index=False)