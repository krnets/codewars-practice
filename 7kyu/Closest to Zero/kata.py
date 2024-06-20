def closest(lst):
    ans = min(lst, key=abs)
    return (ans, None)[ans and -ans in lst]
