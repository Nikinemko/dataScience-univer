import requests
from api_key import API_KEY


def yelp_search(query):
    r = requests.get(
        "https://api.yelp.com/v3/businesses/search",
        params={'sort_by': 'best_match', 'limit': 50, 'location': query},
        headers={'Authorization': f'Bearer {API_KEY}',
                 'accept': 'application/json'}
    )
    response = r.json()
    """
        Make an authenticated request to the Yelp API.
        Args:
        query (string): Search term
        Returns:
        total (integer): total number of businesses on Yelp
       corresponding to the query
        businesses (list): list of dicts representing each business
        """

    return response.get('total'), response.get('businesses')
