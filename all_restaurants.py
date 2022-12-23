import requests
from time import sleep
from api_key import API_KEY


def make_request(query, offset=0, limit=20):
    r = requests.get(
        "https://api.yelp.com/v3/businesses/search",
        params={'sort_by': 'best_match', 'limit': limit,
                'location': query, 'offset': offset},
        headers={'Authorization': f'Bearer {API_KEY}',
                 'accept': 'application/json'}
    )
    response = r.json()
    return response.get('total'), response.get('businesses')


def all_restaurants(query):
    total = 1
    limit = 20
    offset = 0
    businesses_pool = []

    while offset < total:
        sleep(0.2)
        total, businesses = make_request(query, offset, limit)
        offset += limit
        businesses_pool += businesses
    """
    Retrieve ALL the restaurants on Yelp for a given query.
    Args:
    query (string): Search term
    Returns:
    results (list): list of dicts representing each business
    """

    return businesses_pool
