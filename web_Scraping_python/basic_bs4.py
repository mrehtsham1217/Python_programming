from bs4 import BeautifulSoup
import lxml
with open("website.html") as file:
    content = file.read()
# make soup object
soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
# print(soup.title.name)  # will give title
# print(soup.title.string)
# print(soup)  # This will give you the whole html file
# print(soup.prettify())  # everything in a left align
# print(soup.a)#it will give only first ancher tag
# print(soup.p)#it will give only first paragraph

# -------->find_all() will find every tag with name------->
all_ancher_tags = soup.find_all(name="a")
all_para_tags = soup.find_all(name="p")
# print(all_ancher_tags)
# print("\n-----------------------------\n")
# print(all_para_tags)

"""
for tags in all_ancher_tags:
    print(tags.getText())
print("\n-----------------------------\n")
for tags in all_para_tags:
    print(tags.getText())

for tags in all_ancher_tags:
    print(tags.get("href"))
heading = soup.find(name="h1", id="name")
heading_class = soup.find(name="h3", class_="heading")
print(heading)
print(heading_class)
print(heading_class.get("class"))

# if you want the exact ancher tag than you can use css selector in python

company_url = soup.select_one(selector="p a")
print(company_url)
#get name by id
name_id = soup.select_one(selector="#name")
print(name_id)
"""
# get name by class
heading_class = soup.select(".heading")
print(heading_class)

#  1-->select_one
# 2-->select
# 3-->find
# 4-->find_all()
