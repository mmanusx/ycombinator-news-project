from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
# open file yerine requests i kullandık
# print(response.text) # requests i normalde api'ler için kullanıyoruz ama siteyi verince tüm html vb okuyor

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)
articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    article_links.append(article_link)


article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# yanlarında points ifadesi var bundan kurtulmak istiyoruz .split() i kullanıcam

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])



# print(article_texts)
# print(article_links)
# print(article_upvotes)

### Yol II En Yüksek Puanı alan makalenin index'ini bulma
# max_point = 0
# for each in article_upvotes:
#     if each > max_point:
#         max_point = each
# max_index = article_upvotes.index(max_point)
# print(max_index)

###### Sadece ilk elementleri bulmak için
# article_tag = soup.find(name="a", class_="titlelink")
# article_text = article_tag.getText()
# article_link = article_tag.get("href")
# article_upvote = soup.find(name="span", class_="score").getText()
#
# # Yol II select ile
# #article_upvote_code = soup.select_one(".subtext .score")
# #article_upvote = article_upvote_code.getText()
#
# print(article_text)
# print(article_link)
# print(article_upvote)
















####################### kütüphane Açıklamaları #####################################
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/


# import lxml // eğer site xml ile yazılmışsa parse etmek için bu ktp

# with open("website.html", encoding="utf-8") as file: # emojiden dolayı encoding hatası verdi, utf-8 olduğunu belirttim
#     contents = file.read()
#     # print(contents) bütün siteyi bir stringin içine attı ve yazabiliyor
#     # print(type(contents)) stringin içinden elementleri seçmek için BS ktp kullanılacak
#
#
# soup = BeautifulSoup(contents, "html.parser") ### Parse işlemi # site lxml ise ktp import edildikten sonra "lxml" yazılır
# # print(soup.title)
# # print(soup.title.name) # name of the title tag is also "title"
# # print(soup.title.string) # title elementinin içindeki stringi verir
# # print(soup.prettify()) # print html file with indentation to console
# # print(soup.a) # birden fazla element varsa ilk bulduğu elementi tutar
# # istediğimiz tüm elementleri tutmak için doc tan find_all() fonksiyonunu buldum
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href")) # achor tag ların href link kısımlarını aldım
#     #pass
#
# heading = soup.find(name="h1", id="name") # birtane olduğu için find_all() kullanmadık
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading") # class keyword is reserved keyword with python yani python bu kelimeyi kullanıyor, bu yüzden kütüphane de class yerine class_ attribute yapmışlar
# # print(section_heading.getText()) elementin içindeki texti verir
# print(section_heading.get("class")) # belirli attribute deki değeri döndürür class ı heading
#
# ############## Aynı elementden birden fazla olduğunda sorun çıkıyor
# ############## Bunu engellemek için o elementin neyi eşsiz diye bakmamız lazım
#
# # ??? analamadığım yer bazı yerlerde find bazı yerlerde select kullanılması aradaki fark???
# # find yada find_all tag, class, id de // select() css syntax da kullanılıyor childirin  olaylarında "h1 a{}" yapmak istediğimizde
#
# # company_url = soup.select_one(selector="p a") # select_one select den farklı yalnızca ilk eşeleşeni alır
# # print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings) # liste dönecek
