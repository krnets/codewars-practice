# def count_developers(lst):
#     return sum(attendee['continent'] == 'Europe' and attendee['language'] == 'JavaScript' for attendee in lst)

# def count_developers(lst):
#     return len([*filter(lambda x: x['continent'] == 'Europe' and x['language'] == 'JavaScript', lst)])

def count_developers(lst):
    return sum([*map(lambda x: x['continent'] == 'Europe' and x['language'] == 'JavaScript', lst)])

list1 = [
          { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'JavaScript' },
          { 'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti', 'continent': 'Oceania', 'age': 28, 'language': 'JavaScript' },
          { 'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan', 'continent': 'Asia', 'age': 35, 'language': 'HTML' },
          { 'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan', 'continent': 'Asia', 'age': 30, 'language': 'CSS' }
        ]
        
list2 = [
          { 'firstName': 'Oliver', 'lastName': 'Q.', 'country': 'Australia', 'continent': 'Oceania', 'age': 19, 'language': 'HTML' },
          { 'firstName': 'Lukas', 'lastName': 'R.', 'country': 'Austria', 'continent': 'Europe', 'age': 89, 'language': 'HTML' }
        ]
        
        
q = count_developers(list1)  # 1
q
q = count_developers(list2)  # 0
q