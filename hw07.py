import os
import pandas as pd
import numpy as np
import requests
import bs4
import time
import json
import re


# ---------------------------------------------------------------------
# Question # 1
# ---------------------------------------------------------------------
def send_requests(apiKey, *args):
    """

    :param apiKey: apiKey from newsapi website
    :param args: number of languages as strings
    :return: a list of dictionaries, where keys correspond to languages
    and values correspond to Response objects

    >>> responses = send_requests(os.environ['API_KEY'], "ru", "fr")
    >>> isinstance(responses[0], dict)
    True
    >>> isinstance(responses[1], dict)
    True
    """

    return ...


def gather_info(resp):
    """
    Finds some basic information from the obtained responses
    :param resp: a list of dictionaries
    :return: a list with the following items:
    language that has the most number of news
    most common base url for every language
    >>> responses = send_requests(os.environ['API_KEY'], "ru", "fr")
    >>> result = gather_info(responses)
    >>> isinstance(result[0], str)
    True
    >>> len(result) == len(responses) + 1
    True
    """

    return ...

# ---------------------------------------------------------------------
# Question # 2
# ---------------------------------------------------------------------


####################
#Problem Regex
####################

def match_1(string):
    """
    regex to match description 2.1
    >>> match_1("abcdefge")
    True
    >>> match_1("abcdef")
    True
    >>> match_1("abc")
    True
    >>> match_1("ab")
    False
    :param string: some text
    :return: Returns whether or not a string matches abc
    """

    return ...

def match_2(string):
    """
    regex to match description 2.2
    :param string: some text
    :return: Returns whether or not a string matches three digits
    >>> match_2("abc123xyz")
    True
    >>> match_2("define 123")
    True
    >>> match_2("var g = 123;")
    True
    >>> match_2("12")
    False
    """

    return ...

def match_3(string):
    """
    regex to match description 2.3
    :param string: some text
    :return: Returns whether or not a string matches description 2.3
    >>> match_3("cat.")
    True
    >>> match_3("896.")
    True
    >>> match_3("?=+.")
    True
    >>> match_3("abc1")
    False
    """

    return ...

def match_4(string):
    """
    regex to match description 2.4
    :param string: some text
    :return: Returns whether or not a string matches description 2.4
    >>> match_4("can")
    True
    >>> match_4("fan")
    True
    >>> match_4("man")
    True
    >>> match_4("ran")
    False
    """

    return ...

def match_5(string):
    """
    regex to match description 2.5
    :param string: some text
    :return: Returns whether or not a string matches description 2.5
    >>> match_5("dog")
    True
    >>> match_5("log")
    True
    >>> match_5("hog")
    True
    >>> match_5("bog")
    False
    """

    return ...

def match_6(string):
    """
    regex to match description 2.6
    :param string: some text
    :return: Returns whether or not a string matches description 2.6
    >>> match_6("Can")
    True
    >>> match_6("Ana")
    True
    >>> match_6("Bob")
    True
    >>> match_6("steve")
    False
    """

    return ...

def match_7(string):
    """
    regex to match description 2.7
    :param string: some text
    :return: Returns whether or not a string matches description 2.7
    >>> match_7("wazzzzup")
    True
    >>> match_7("wazzup")
    True
    >>> match_7("wazzzzzzzzup")
    True
    >>> match_7("wazup")
    False
    """

    return ...

def match_8(string):
    """
    regex to match description 2.8
    :param string: some text
    :return: Returns whether or not a string matches description 2.8
    >>> match_8("aaaabcc")
    True
    >>> match_8("aabbbbc")
    True
    >>> match_8("aacc")
    True
    >>> match_8("a")
    False
    """

    return ...

def match_9(string):
    """
    regex to match description 2.9
    :param string: some text
    :return: Returns whether or not a string matches description 2.9
    >>> match_9("1 file found?")
    True
    >>> match_9("2 files found?")
    True
    >>> match_9("24 files found?")
    True
    >>> match_9("No files found.")
    False
    """

    return ...

def match_10(string):
    """
    regex to match description 2.10
    :param string: some text
    :return: Returns whether or not a string matches description 2.10
    >>> match_10("1.   abc")
    True
    >>> match_10("2.	abc")
    True
    >>> match_10("3.           abc")
    True
    >>> match_10("4.abc")
    False
    """

    return ...

def match_11(string):
    """
    regex to match description 2.11
    :param string: some text
    :return: Returns whether or not a string matches description 2.11
    >>> match_11("Mission: successful")
    True
    >>> match_11("Last Mission: unsuccessful")
    False
    >>> match_11("Mission: very successful")
    True
    >>> match_11("Next Mission: successful upon capture of target")
    False
    """

    return ...


# ---------------------------------------------------------------------
# Question # 3
# ---------------------------------------------------------------------

def extract_personal(s):
    """
    :Example:
    >>> fp = os.path.join('data', 'messy.test.txt')
    >>> s = open(fp, encoding='utf8').read()
    >>> emails, ssn, bitcoin, addresses = extract_personal(s)
    >>> emails[0] == 'test@test.com'
    True
    >>> ssn[0] == '423-00-9575'
    True
    >>> bitcoin[0] == '14F'
    True
    >>> addresses[0] == '530 High Street'
    True
    """

    return ...

# ---------------------------------------------------------------------
# Question # 4
# ---------------------------------------------------------------------

def tfidf_data(review, reviews):
    """
    :Example:
    >>> fp = os.path.join('data', 'reviews.txt')
    >>> reviews = pd.read_csv(fp, header=None, squeeze=True)
    >>> review = open(os.path.join('data', 'review.txt'), encoding='utf8').read().strip()
    >>> out = tfidf_data(review, reviews)
    >>> out['cnt'].sum()
    85
    >>> 'before' in out.index
    True
    """
    return ...


def relevant_word(out):
    """
    :Example:
    >>> fp = os.path.join('data', 'reviews.txt')
    >>> reviews = pd.read_csv(fp, header=None, squeeze=True)
    >>> review = open(os.path.join('data', 'review.txt'), encoding='utf8').read().strip()
    >>> out = tfidf_data(review, reviews)
    >>> relevant_word(out) in out.index
    True
    """
    return ...


# ---------------------------------------------------------------------
# Question # 5
# ---------------------------------------------------------------------

def hashtag_list(tweet_text):
    """
    :Example:
    >>> testdata = [['RT @DSC80: Text-cleaning is cool! #NLP https://t.co/xsfdw88d #NLP1 #NLP1']]
    >>> test = pd.DataFrame(testdata, columns=['text'])
    >>> out = hashtag_list(test['text'])
    >>> (out.iloc[0] == ['NLP', 'NLP1', 'NLP1'])
    True
    """

    return ...


def most_common_hashtag(tweet_lists):
    """
    :Example:
    >>> testdata = [['RT @DSC80: Text-cleaning is cool! #NLP https://t.co/xsfdw88d #NLP1 #NLP1']]
    >>> test = hashtag_list(pd.DataFrame(testdata, columns=['text'])['text'])
    >>> most_common_hashtag(test).iloc[0]
    'NLP1'
    """

    return ...


# ---------------------------------------------------------------------
# Question # 6
# ---------------------------------------------------------------------


def create_features(ira):
    """
    :Example:
    >>> testdata = [['RT @DSC80: Text-cleaning is cool! #NLP https://t.co/xsfdw88d #NLP1 #NLP1']]
    >>> test = pd.DataFrame(testdata, columns=['text'])
    >>> out = create_features(test)
    >>> anscols = ['text', 'num_hashtags', 'mc_hashtags', 'num_tags', 'num_links', 'is_retweet']
    >>> ansdata = [['text cleaning is cool', 3, 'NLP1', 1, 1, True]]
    >>> ans = pd.DataFrame(ansdata, columns=anscols)
    >>> (out == ans).all().all()
    True
    """
    
    return ...

# ---------------------------------------------------------------------
# DO NOT TOUCH BELOW THIS LINE
# IT'S FOR YOUR OWN BENEFIT!
# ---------------------------------------------------------------------


# Graded functions names! DO NOT CHANGE!
# This dictionary provides your doctests with
# a check that all of the questions being graded
# exist in your code!

GRADED_FUNCTIONS = {
    'q01': ['send_requests', 'gather_info'],
    'q02': ['match_%d' % x for x in range(1, 12)],
    'q03': ['extract_personal'],
    'q04': ['tfidf_data', 'relevant_word'],
    'q05': ['hashtag_list', 'most_common_hashtag'],
    'q06': ['create_features']
}


def check_for_graded_elements():
    """
    >>> check_for_graded_elements()
    True
    """
    
    for q, elts in GRADED_FUNCTIONS.items():
        for elt in elts:
            if elt not in globals():
                stmt = "YOU CHANGED A QUESTION THAT SHOULDN'T CHANGE! \
                In %s, part %s is missing" %(q, elt)
                raise Exception(stmt)

    return True

