from retrieve_html import retrieve_html
from yelp_search import yelp_search
from all_restaurants import all_restaurants
from parse_yelp_page import parse_yelp_page
from extract_yelp_reviews import extract_yelp_reviews

print("----------- Q0 -----------")
facebook_article = retrieve_html(
    'https://www.nytimes.com/2016/08/28/magazine/inside-facebooks-totally-insane-unintentionally-gigantic-hyperpartisan-political-media-machine.html')
print(facebook_article)

print("----------- Q1 -----------")
num_records, data = yelp_search('Pittsburgh')
print(num_records)
print(list(map(lambda x: x['name'], data)))

print("----------- Q2 -----------")
data = all_restaurants('Polish Hill, Pittsburgh')
print(len(data))
print([x['name'] for x in data])

print("----------- Q3 -----------")
reviews, num_pages, *other = parse_yelp_page(
    "https://www.yelp.com/biz/the-porch-at-schenley-pittsburgh")
print(list(reviews))
print(num_pages)

print("----------- Q3.5 -----------")
reviews = extract_yelp_reviews(
    "https://www.yelp.com/biz/the-porch-at-schenley-pittsburgh")
print(list(reviews))
