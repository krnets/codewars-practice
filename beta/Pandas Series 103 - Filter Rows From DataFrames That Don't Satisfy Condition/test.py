import codewars_test as test
from kata import filter_dataframe
import pandas as pd


@test.describe("Example Tests")
def example_tests():
    df = pd.DataFrame(
        data=[[1, 2, 3], [4, 5, 6], [6, 3, 2], [1, 1, 7]], columns=list("ABC")
    )
    column = "A"
    func = lambda x: x <= 2
    df_out = pd.DataFrame(
        data=[[4, 5, 6], [6, 3, 2]], index=[1, 2], columns=list("ABC")
    )
    test.expect(filter_dataframe(df, column, func).equals(df_out))
