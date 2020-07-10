from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)


def scrap_wion():
    headlines_collection = ''
    counter = 0
    news_media_url = 'https://www.wionews.com/world?page=1'
    raw_HTML = simple_get(news_media_url)

    bts4_obj = BeautifulSoup(raw_HTML, 'html.parser')
    file_handler = open('Wion_Headlines.txt', 'w')

    for index, item in enumerate(bts4_obj.find_all('a')):
        if(index > 69 and index < 193 and len(item.text) > 0):
            filtered_headline = item.text.replace(
                '\u2192', '').replace('Read Article', '').lstrip()
            if(len(filtered_headline) > 0):
                counter += 1
                headlines_collection = f'{headlines_collection} Headline number {counter}: {filtered_headline} .\n'

    file_handler.write(headlines_collection)
    file_handler.close()
    return headlines_collection


def scrap_inshorts():
    headlines_collection = ''
    counter = 0
    news_media_url = 'https://inshorts.com/en/read'
    raw_HTML = simple_get(news_media_url)

    bts4_obj = BeautifulSoup(raw_HTML, 'html.parser')
    file_handler = open('Inshorts_Headlines.txt', 'w')
    for item in bts4_obj.find_all('span', attrs={"itemprop": "headline"}):
        counter += 1
        headlines_collection = f'{headlines_collection} Headline number {counter}: {item.text} .\n'
        headlines_collection = headlines_collection.replace(
            '\u20b9', 'rupees ')
    file_handler.write(headlines_collection)
    file_handler.close()
    return headlines_collection


def scrap_headlines(newsChannel):
    if (newsChannel == 'wion'):
        return scrap_wion()
    else:
        return scrap_inshorts()
