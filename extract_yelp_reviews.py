from parse_yelp_page import parse_yelp_page


def extract_yelp_reviews(url):
    current_page = 0
    max_pages = 1
    all_reviews = []
    while current_page <= max_pages:
        reviews, _, current_page, max_pages = parse_yelp_page(
            f'{url}?start={current_page * 10}')
        all_reviews += reviews
    """
    Retrieve ALL of the reviews for a single business on Yelp.
    Parameters:
    url (string): Yelp URL corresponding to the business of 
    interest.
    Returns:
    reviews (list): list of dictionaries containing extracted 
    review information
    """
    return all_reviews
