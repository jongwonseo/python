from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print(soup)
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
article_tags = soup.find_all(name='span', class_='titleline')
article_texts = []
article_links = []

for article_tag in article_tags:
  text = article_tag.find('a').getText()
  article_texts.append(text)

  link = article_tag.find('a').get('href')
  article_links.append(link)
  
article_upvotes = [ int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]



# print(article_texts)
# print(article_links)
# print(article_upvotes)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])

