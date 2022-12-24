# import pickle
# import gzip
import re
from bs4 import BeautifulSoup
from retrieve_html import retrieve_html


# with gzip.open("parse_yelp_page_dict.pkl.gz", "rb") as f:
#     parse_yelp_page_dict = pickle.load(f)


def parse_yelp_page(url):
    html = retrieve_html(url)[1]
    # html = parse_yelp_page_dict[url]

    soup = BeautifulSoup(html, 'html.parser')
    reviews_html = soup.select("#reviews > section > div > div > ul > li")
    pages_count = len(soup.select(
        "div[class^='pagination-links'] > div[class^='pagination-link-container']"))
    print("Parsing: ", soup.select_one(
        "div[role='navigation'] > div:last-child > span").string)
    current_page, max_pages = re.findall("^(\d+) of (\d+)", soup.select_one(
        "div[role='navigation'] > div:last-child > span").string)[0]
    reviews = map(lambda item: {
        'author': item.select_one(".user-passport-info > span > a").string,
        'rating': re.findall("^\d+", item.select_one("div > div > div > div:first-child > span > div").attrs['aria-label'])[0],
        'date': item.select_one("div > div:nth-child(2) > div > div:last-child > span").string,
        'description': item.select_one("div > div > p[class^='comment'] > span").string
    }, reviews_html)
    """
    Parse the reviews on a single page of a restaurant.

    Args:
    url (string): URL string corresponding to a Yelp restaurant
    Returns:
    tuple(list, int): a tuple of two elements
    first element: list of dictionaries corresponding to the
    extracted review information
    second element: Number of pages total
    """

    # To use downloaded data, replace any command (or any equivalent
    # using requests)
    # html = retrieve_html(url)[1]
    # with the command:
    # html = parse_yelp_page_dict[url]

    return reviews, pages_count, int(current_page), int(max_pages)
