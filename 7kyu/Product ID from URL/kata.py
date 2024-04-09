import re

# def get_product_id(url):
#     return re.search(r"-(\d+)-\d+\.html", url).group(1)

def get_product_id(url):
    return url.split('-')[-2]