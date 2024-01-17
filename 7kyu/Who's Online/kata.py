from collections import defaultdict


# def who_is_online(friends):
#     online, offline, away = [], [], []

#     for x in friends:
#         username, status, last_activity = x["username"], x["status"], x["last_activity"]
#         if status == "online":
#             if last_activity > 10:
#                 away.append(username)
#             else:
#                 online.append(username)
#         elif status == "offline":
#             offline.append(username)

#     if online and offline and away:
#         return {"online": online, "offline": offline, "away": away}
#     elif online and away:
#         return {"online": online, "away": away}
#     elif offline and away:
#         return {"offline": offline, "away": away}
#     elif online and offline:
#         return {"online": online, "offline": offline}
#     elif online:
#         return {"online": online}
#     elif offline:
#         return {"offline": offline}
#     elif away:
#         return {"away": away}
#     else:
#         return defaultdict(list)


def who_is_online(friends):
    result = defaultdict(list)

    for friend in friends:
        status = friend["status"]

        if status == "online" and friend["last_activity"] > 10:
            status = "away"

        result[status].append(friend["username"])

    return result
