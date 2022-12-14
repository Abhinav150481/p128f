from bs4 import BeautifulSoup
import requests
import pandas as pd

START_URL = (
    "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
)
wiki = requests.get(START_URL)
soup = BeautifulSoup(wiki.text, "html.parser")
star_table=soup.find_all("table")
temp_list = []
tableRows=star_table[7].find_all("tr")
for tr in tableRows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

name = []
distance = []
mass = []
radius = []

for i in range(1, len(temp_list)):
    name.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])

df = pd.DataFrame(
    list(zip(name, distance, mass, radius)),
    columns=["Star_name", "Distance", "Mass", "Radius"],
)
df.to_csv("dwarfstars.csv")