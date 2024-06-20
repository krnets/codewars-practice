# class Harshad:
#     @staticmethod
#     def is_valid(number):
#         return number and number % sum(map(int, str(number))) == 0

#     @staticmethod
#     def get_next(number):
#         number += 1
#         while not Harshad.is_valid(number):
#             number += 1
#         return number

#     @staticmethod
#     def get_series(count, start=0):
#         h_set = set()
#         num = start
#         while len(h_set) < count:
#             h_num = Harshad.get_next(num)
#             h_set.add(h_num)
#             num = h_num
#         return sorted(h_set)


from itertools import count, islice


class Harshad:
    @staticmethod
    def is_valid(number):
        return number % sum(map(int, str(number))) == 0

    @staticmethod
    def get_next(number):
        return next(i for i in count(number + 1) if Harshad.is_valid(i))

    @staticmethod
    def get_series(total, start=0):
        return list(islice(filter(Harshad.is_valid, count(start + 1)), total))


# print(Harshad.get_next(0))
# print(Harshad.is_valid(1))
# print(Harshad.get_series(3, 1000))
