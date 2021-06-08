import requests
import operator
from bs4 import BeautifulSoup
from collections import Counter


def word_frequencies(url):
    """
    Downloads the content from the given URL and returns a dict {word -> frequency}
    giving the count of each word on the page. Ignores HTML tags in the response.
    :param url: Full URL of HTML page
    :return: dict {word -> frequency}
    """
    source_code = requests.get(url).text

    count = Counter()
    word_list = []
 
    # BeautifulSoup object which will
    # ping the requested url for data
    soup = BeautifulSoup(source_code, 'html.parser')

    text = soup.get_text()

    words = text.lower().split()

    for word in words:
        symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/., "

        #Remove the symbols
        for i in range(len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            word_list.append(word)

    return Counter(word_list)
