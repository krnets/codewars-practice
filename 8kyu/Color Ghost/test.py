from solution import Ghost
import codewars_test as test

# ghosts = [Ghost().color for _ in range(100)]
# test.expect(ghosts.count("white") >= 1)
# test.expect(ghosts.count("yellow") >= 1)
# test.expect(ghosts.count("purple") >= 1)
# test.expect(ghosts.count("red") >= 1)

ghosts = [Ghost().color for _ in range(100)]
colors = "white yellow purple red".split()

for s in colors:
    n = ghosts.count(s) >= 1
    test.expect(n, f"With 100 elements there should be at least one '{s}'")
    if not n:
        break
else:
    test.assert_equals(set(ghosts) - set(colors),
                       set(), "Incorrect colors found")
