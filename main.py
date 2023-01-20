from bs4 import BeautifulSoup
import csv
import requests
from itertools import zip_longest

job_titles = []
information = []
# 1st step use requests to fetch the url
result = requests.get(
    "https://wuzzuf.net/search/jobs/?a=hpb&filters%5Bcareer_level%5D%5B0%5D=Entry%20Level&q=data%20engineering")

# 2nd step save page content/markup
src = result.content
print(src)

# 3rd step create soup object to parse content
soup = BeautifulSoup(src, "lxml")
print(soup)
# What I need to extract!?
#  Job title:

job_titles = soup.find_all("h2", {"class": "css-m604qf"})

#  Description
information = soup.find_all("div", {"class": "css-y4udm8"})

# loop to extract only text

for i in range(len(job_titles)):
    job_titles.append(job_titles[i].text)
    information.append(information[i].text)
print(job_titles, information)


# deal with csv to split informations
file_list = [job_titles, information]
exported = zip_longest(*file_list)
with open("/home/ikhalidma/Desktop/web_scrapping/jobs_split.csv", "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["Job_Title", "Diff_Information"])
    wr.writerows(exported)
