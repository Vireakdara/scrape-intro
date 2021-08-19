from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com")
yc_web_page = response.text
# print(response.text)

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)
article = soup.find_all(name="a", class_="storylink")

article_texts = []
article_links = []

for arr in article:
    article_tag = arr.getText()
    article_texts.append(article_tag)
    article_link = arr.get("href")
    article_links.append(article_link)

article_scores = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
print(article_scores)

sorted_index = []
for arr_index in article_scores:
    num_index = article_scores.index(max(article_scores))
    sorted_index.append(num_index)
    article_scores.remove(article_scores[num_index])
print(sorted_index)


for arr in sorted_index:
    print(article_texts[arr])
    print(article_links[arr])

    print(article_scores[2])




# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#     # print(contents)
#
# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.p)
#
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
#
# # for tags in all_anchor_tags:
#     # print(tags.getText())
#     # print(tags.get("href"))
#
#
# heading = soup.find_all(name="h1", id="name")
# print(heading)
#
# book_heading = soup.find(name="h3", class_="heading")
# print(book_heading.string)
#
# company_url = soup.select_one(selector="p em")
# print(company_url)
#
# name = soup.select("#name")
# print(name)
