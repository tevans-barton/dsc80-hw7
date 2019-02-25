import os
import pandas as pd
import numpy as np
import requests
import bs4
import time
import json
import re

os.environ['API_KEY'] = 'e2210554892140e9bd1b8c87f7242100'


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
    toReturn = []
    for arg in args:
        url = ('https://newsapi.org/v2/top-headlines?'
                'language=' + str(arg) + '&'
                'apiKey=' + str(apiKey))
        toReturn.append({arg : requests.get(url)})
    return toReturn


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
    lang_most = get_most_results(resp)
    urlList = []
    for x in resp:
        bigUrlList = get_urls(json.loads(list(x.values())[0].text))
        urlList.append(most_common_in_list(bigUrlList))
    return [lang_most] + urlList

def get_most_results(resp):
    max_articles = 0
    langToReturn = ''
    for x in resp:
        tempdict = json.loads(list(x.values())[0].text)
        if tempdict['totalResults'] >= max_articles:
            langToReturn = list(x.keys())[0]
    return langToReturn

def get_urls(dict):
    urls = []
    for article in dict['articles']:
        urls.append(re.sub('/', '', re.findall('/[A-Za-z0-9 \.]+/', article['url'])[0]))
    return urls

def most_common_in_list(urlList):
    return max(set(urlList), key=urlList.count)





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
    result = re.match('.*abc.*', string)
    if result:
        return True
    else:
        return False

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
    result = re.match('.*[0-9]{3}.*', string)
    if result:
        return True
    else:
        return False

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
    result = re.match('.{3}\..*', string)
    if result:
        return True
    else:
        return False

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
    result = re.match('.*(c|m|f)an.*', string)
    if result:
        return True
    else:
        return False

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
    result = re.match('[^b].*og.*', string)
    if result:
        return True
    else:
        return False

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
    result = re.match('^[A-Z]', string)
    if result:
        return True
    else:
        return False

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
    result = re.match('.*waz+zup.*', string)
    if result:
        return True
    else:
        return False

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
    result = re.match('.*a+(b|c)+', string)
    if result:
        return True
    else:
        return False

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
    result = re.match('[0-9]+ file(s){0,1} found\?', string)
    if result:
        return True
    else:
        return False

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
    result = re.match('.*[0-9]+\.\s+.+', string)
    if result:
        return True
    else:
        return False

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
    result = re.match('(^(Mission:)).*(( successful)$)', string)
    if result:
        return True
    else:
        return False


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
    emails = re.findall('[A-Za-z0-9]+@[A-Za-z0-9]+\.[a-z]{3}', s)
    ssn = re.findall('ssn:[0-9]{3}-[0-9]{2}-[0-9]{4}',s)
    ssn = [re.sub('ssn:', '', x) for x in ssn]
    bitcoin = re.findall('bitcoin:[A-Za-z0-9]+', s)
    bitcoin = [re.sub('bitcoin:', '', x) for x in bitcoin]
    addresses = re.findall('[0-9]+ [A-Za-z ]+', s)
    return (emails, ssn, bitcoin, addresses)

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
    words = review.split()
    wordSeries = pd.Series(words)
    index = np.sort(wordSeries.unique())
    cnt = wordSeries.value_counts().sort_index()
    tf = cnt / len(words)
    idfList = []
    tfidfList = []
    for w in index:
        re_pat = '\\b%s\\b' % w
        idfList.append(np.log(len(reviews) / reviews.str.contains(re_pat).sum()))
    idf = pd.Series(idfList, index = index)
    for i in index:
        tfidfList.append(tf[i] * idf[i])
    tfidf = pd.Series(tfidfList, index = index)
    df = pd.DataFrame({'cnt' : cnt, 'tf' : tf, 'idf' : idf, 'tfidf' : tfidf}, index = index)
    return df



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
    df = out.sort_values('tfidf', ascending = False)
    return df.index[0]


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
    return tweet_text.apply(lambda x : [word.replace('#', '') for word in re.findall('#[A-Za-z0-9]+', x)])


def most_common_hashtag(tweet_lists):
    """
    :Example:
    >>> testdata = [['RT @DSC80: Text-cleaning is cool! #NLP https://t.co/xsfdw88d #NLP1 #NLP1']]
    >>> test = hashtag_list(pd.DataFrame(testdata, columns=['text'])['text'])
    >>> most_common_hashtag(test).iloc[0]
    'NLP1'
    """
    wordlists = tweet_lists.sum()
    return tweet_lists.apply(lambda x : find_max(x, wordlists))

def find_max(small_list, big_list):
    if len(small_list) == 0:
        return np.NaN
    elif len(small_list) == 1:
        return small_list[0]
    else:
        tempdict = {}
        for x in small_list:
            tempdict[big_list.count(x)] = x
        return tempdict[np.max(list(tempdict.keys()))]


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
    df = pd.DataFrame()
    df['text'] = ira['text'].apply(lambda x : clean_text(x))
    df['num_hashtags'] = pd.Series([len(x) for x in hashtag_list(ira['text'])])
    df['mc_hashtags'] = pd.Series(most_common_hashtag(hashtag_list(ira['text'])))
    df['num_tags'] = ira['text'].apply(lambda x : len(re.findall('@[A-Za-z0-9]+', x)))
    df['num_links'] = ira['text'].apply(lambda x : len(re.findall('http.*', x)))
    df['is_retweet'] = ira['text'].apply(lambda x : is_retweet(x))
    return df

def is_retweet(string):
    result = re.match('^(RT)', string)
    if result:
        return True
    else:
        return False

def clean_text(string):
    string = re.sub('@[A-Za-z0-9]+', '', string)
    string = re.sub('#[A-Za-z0-9]+', '', string)
    string = re.sub('RT', '', string)
    string = re.sub('http.*', '', string)
    string = re.sub('[^A-Za-z0-9 ]',' ', string)
    string = string.lower().lstrip().rstrip()
    return string

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

