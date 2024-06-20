import codewars_test as test


def histogram(results):
    total = sum(results)
    arr = []

    for i, freq in enumerate(reversed(results)):
        row = str(len(results) - i) + "|"
        if freq > 0:
            row += (
                "\u2588" * (freq * 50 // total) + " " + str(freq * 100 // total) + "%"
            )
        row += "\n"
        arr.append(row)
    return "".join(arr)


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        results = [7, 3, 70, 15, 0, 5]
        expected = (
            "6|██ 5%\n"
            + "5|\n"
            + "4|███████ 15%\n"
            + "3|███████████████████████████████████ 70%\n"
            + "2|█ 3%\n"
            + "1|███ 7%\n"
        )
        test.assert_equals(histogram(results), expected)

        results = [0, 0, 0, 0, 0, 0]
        expected = "6|\n" + "5|\n" + "4|\n" + "3|\n" + "2|\n" + "1|\n"
        test.assert_equals(histogram(results), expected)

        results = [0, 0, 11, 0, 0, 0]
        expected = (
            "6|\n"
            + "5|\n"
            + "4|\n"
            + "3|██████████████████████████████████████████████████ 100%\n"
            + "2|\n"
            + "1|\n"
        )
        test.assert_equals(histogram(results), expected)
