from datetime import datetime, timedelta


# def seconds_ago(s, n):
#     fmt = "%Y-%m-%d %X"
#     return str(datetime.strptime(s, fmt) - timedelta(seconds=n))


def seconds_ago(s, n):
    return str(datetime.fromisoformat(s) - timedelta(seconds=n))
