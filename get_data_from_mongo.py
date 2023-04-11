from db import drop_tender_collection, insert_many, my_db_connect
from etender_get_data import start_scrap

url: str = "https://etenders.gov.eg/"

my_data = start_scrap(url)
new_tender = []
print("get all data from mongodb")
data = list(my_db_connect.etender_collection.find())


for i in data:
    if i in my_data:
        pass

    else:
        new_tender.append(i)

insert_many(new_tender)
print(f"the new tender is : {new_tender}")
print(f"the new tender length is : {len(new_tender)} tender")
