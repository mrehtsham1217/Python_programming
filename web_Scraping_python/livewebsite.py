from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
# print(soup.prettify())-->Will print all the webiste in left align

# article_tag = soup.find(name="a")
# article_tag = soup.find_all("span", name="a", class_='titleline')
article_upvote = [int(scores.getText().split()[0])
                  for scores in soup.find_all(name="span", class_="score")]
largest_point = max(article_upvote)
print(largest_point)
# print(article_upvote.getText())
print(article_upvote)

# span_with_titleline = soup.find("span", class_="titleline")
# ancher_in_titleline = span_with_titleline.find("a")
# upvote_in_titleline = span_with_titleline.find(name="span", class_="score")
# print(span_with_titleline)
# print(ancher_in_titleline)
# print(upvote_in_titleline)
