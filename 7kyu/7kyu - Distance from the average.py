# 7kyu - Distance from the average

""" Given a starting list/array of data, it could make some statistical sense to know 
how much each value differs from the average.

If for example during a week of work you have collected 55,95,62,36,48 contacts for your business, 
it might be interesting to know the total (296), the average (59.2), but also how much you moved away 
from the average each single day.

For example on the first day you did something less than the said average (55, meaning -4.2 compared to the average), 
much more in the second day (95, 35.8 more than the average and so on).

The resulting list/array of differences starting from [55, 95, 62, 36, 48] is thus [4.2, -35.8, -2.8, 23.2, 11.2].

Assuming you will only get valid inputs (ie: only arrays/lists with numbers), create a function to do that, 
rounding each difference to the second decimal digit (this is not needed in Haskell); 
extra points if you do so in some smart, clever or concise way

With Clojure to round use:
(defn roundTo2 [n] (/ (Math/round (* n 100.0)) 100.0)) """


def distances_from_average(test_list):
    average = sum(test_list) / len(test_list)
    return [round(average - x, 2) for x in test_list]

q = distances_from_average([55, 95, 62, 36, 48]), [4.2, -35.8, -2.8, 23.2, 11.2]
q
q = distances_from_average([1, 1, 1, 1, 1]), [0, 0, 0, 0, 0]
q
q = distances_from_average([1, -1, 1, -1, 1, -1]), [-1.0, 1.0, -1.0, 1.0, -1.0, 1.0]
q
q = distances_from_average([1, -1, 1, -1, 1]), [-0.8, 1.2, -0.8, 1.2, -0.8]
q
q = distances_from_average([2, -2]), [-2.0, 2.0]
q
q = distances_from_average([1]), [0]
q
q = distances_from_average([123, -65, 32432, -353, -534]), [6197.6, 6385.6, -26111.4, 6673.6, 6854.6]
q
# q = distances_from_average(range(101)), list(range(50,-51,-1))
# q
# q = distances_from_average(range(1001)), list(range(500,-501,-1))
# q
# q = distances_from_average(range(1000001)), list(range(500000,-500001,-1))
# q
