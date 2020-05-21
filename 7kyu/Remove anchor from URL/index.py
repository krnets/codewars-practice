# 7kyu - Remove anchor from URL

""" Complete the function/method so that it returns the url with anything after the anchor (#) removed.

# returns 'www.codewars.com'
remove_url_anchor('www.codewars.com#about')

# returns 'www.codewars.com?page=1' 
remove_url_anchor('www.codewars.com?page=1')  """

# import re

# def remove_url_anchor(url):
#     return re.sub(r'#.*', '', url)

def remove_url_anchor(url):
    return url.split('#')[0]

# def remove_url_anchor(url):
#     return url.partition('#')[0]


q = remove_url_anchor("www.codewars.com#about")  # "www.codewars.com"
q
# "www.codewars.com/katas/?page=1
q = remove_url_anchor("www.codewars.com/katas/?page=1#about")
q
q = remove_url_anchor("www.codewars.com/katas/")  # "www.codewars.com/katas/
q
