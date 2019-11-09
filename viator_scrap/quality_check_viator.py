import pandas as pd

df = pd.read_csv("/Users/oscartse/Desktop/Klook_WebScrappingProject/viator_scrap/viator_scrap/spiders/records.csv")
counter = 0
for i in df["count"]:
    counter+=i
print(counter)