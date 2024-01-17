def find_admin(lst, lang):
    return [ *filter( lambda dev: dev["language"] == lang and dev["githubAdmin"] == "yes", lst) ]
