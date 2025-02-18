import pandas as pd
import numpy as np
import requests
import random
from bs4 import BeautifulSoup
import sys
import codecs

sys.stdout.reconfigure(encoding='utf-8')

if __name__ == '__main__':
    df = pd.read_csv("Categories/TheCatogories.csv", encoding="utf-8")

    for index, row in df.iterrows():
        field = row['Field_ID']
        subfield = row["SubField_ID"]
        # TODO: CurrPage needs to increase by 1 until end
        currPage = 1
        samples = []
        print("We are at ", index, " out 62")
        while True:
            random_number = random.uniform(0, 1)
            print(random_number)
            parameters = {
                "PageID": 112,
                "CurrPage": currPage,
                "spec": field,
                "spec1": subfield,
                "searchoption": "And",
                "rand": random_number
            }
            r = requests.get(
                "https://www.oea.org.lb/Arabic/GetMembers.aspx", params=parameters)

            # increase currPage
            response = r.text
            print(field, subfield, " We are at this curr Page ", currPage)
            currPage = currPage + 1
            if("لا يوجد أي نتيجة" in response):
                print("End of Disicpline at ", currPage)
                break

            soup = BeautifulSoup(response, 'html.parser')
            # print(response)
            engineer_IDs = soup.find_all(class_="date")
            arabic_names = soup.find_all(class_="company")
            latin_names = soup.find_all(class_="field")
            links = soup.find_all(class_="more")

            data = {"Engineer_ID": engineer_IDs,
                    "Arabic_Names": arabic_names,
                    "Latin_Names": latin_names,
                    "Links": links
                    }
            sample = pd.DataFrame(data=data)
            sample["Engineer_ID"] = sample["Engineer_ID"].astype(
                str).str.replace('<div class="date"><b>رقم المهندس: </b>', '')
            sample["Engineer_ID"] = sample["Engineer_ID"].str.replace(
                '</div>', '')
            sample["Arabic_Names"] = sample["Arabic_Names"].astype(
                str).str.replace('<div class="company"><b>الاسم: </b>', '')
            sample["Arabic_Names"] = sample["Arabic_Names"].str.replace(
                '</div>', '')
            sample["Latin_Names"] = sample["Latin_Names"].astype(
                str).str.replace('<div class="field"><b>Latin Name: </b>', '')
            sample["Latin_Names"] = sample["Latin_Names"].str.replace(
                '</div>', '')
            sample["Links"] = sample["Links"].astype(
                str).str.replace('<div class="more"><a href="', '')
            sample["Links"] = sample["Links"].str.replace(
                '">التفاصيل</a></div>', '')

            sample["Field_ID"] = field
            sample["SubField_ID"] = subfield
            sample["Field"] = row["Field"]
            sample["SubField"] = row["SubField"]
            samples.append(sample)
        displine = pd.concat(samples, ignore_index=True)

        displine.to_csv("Data/" + str(field) + " " + str(subfield) + ".csv", index=False)
