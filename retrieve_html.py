import requests


def retrieve_html(url):
    r = requests.get(url)
    """
    Return the raw HTML at the specified URL.
    Args:
    url (string): 
    Returns:
    status_code (integer):
    raw_html (string): the raw HTML content of the response, 
    properly encoded according to the HTTP headers.
    """

    return r.status_code, r.text
