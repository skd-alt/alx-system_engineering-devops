#!/usr/bin/python3
"""Returns a list containing the titles of all hot articles."""

import requests
after = None


def recurse(subreddit, hot_list=[]):
    """Returns a list containing the titles of all hot articles for a given
    subreddit. If no results are found return None.
    """
    global after
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) \
                Gecko/20100101 Firefox/108.0"
    }
    params = {
        "after": after,
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        after_data = response.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = response.json().get("data").get("children")

        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
