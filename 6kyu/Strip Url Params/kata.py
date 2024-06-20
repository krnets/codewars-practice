import urllib.parse as urllib


def strip_url_params(url, params_to_strip=None):
    parsed_url = urllib.urlparse(url)
    query_params = urllib.parse_qs(parsed_url.query)
    params = [
        "{}={}".format(k, v[0])
        for k, v in query_params.items()
        if not params_to_strip or k not in params_to_strip
    ]
    return "{}?{}".format(parsed_url.path, "&".join(params)) if params else parsed_url.path
