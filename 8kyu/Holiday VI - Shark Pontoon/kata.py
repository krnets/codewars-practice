import codewars_test as test


def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin:
        shark_speed /= 2
    your_time = pontoon_distance / you_speed
    shark_time = shark_distance / shark_speed
    return ("Shark Bait!", "Alive!")[your_time < shark_time]


test.assert_equals(shark(12, 50, 4, 8, True), "Alive!")
test.assert_equals(shark(7, 55, 4, 16, True), "Alive!")
test.assert_equals(shark(24, 0, 4, 8, True), "Shark Bait!")
