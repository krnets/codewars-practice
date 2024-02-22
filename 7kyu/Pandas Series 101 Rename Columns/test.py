import codewars_test as test
from kata import rename_columns
from random import randint, sample
import pandas as pd
import numpy as np


@test.describe('Example Tests')
def example_tests():
    df_input = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6]], columns=list('123'))
    names = ('A', 'B', 'C')
    df_output = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6]], columns=list('ABC'))
    user_solution = rename_columns(df_input, names)
    if type(user_solution) != type(df_output):
        test.fail(
            f"You've returned object of {type(user_solution)}. You must return a DataFrame object")
        return
    test.expect(user_solution.equals(
        df_output), f'Wrong output: Expected:\n{df_output}\n\nActual:\n{user_solution}')


@test.describe('Random Tests')
def random_tests():

    def generate_random_case(valid=True, max_rows=30, max_cols=15):
        n_rows, n_cols = randint(0, max_rows), randint(0, max_cols)
        df = pd.DataFrame(data=np.random.randint(
            0, 100, size=(n_rows, n_cols)), columns=range(n_cols))
        options = ("abs", "delattr", "hash", "memoryview", "set", "all", "dict", "help", "min", "setattr", "any", "dir", "hex", "next", "slice", "ascii", "divmod", "id", "object", "sorted", "bin", "enumerate", "input", "oct", "staticmethod", "bool", "eval", "int", "open", "str", "breakpoint",
                   "exec", "isinstance", "ord", "sum", "bytearray", "filter", "issubclass", "pow", "super", "bytes", "float", "iter", "print", "tuple", "callable", "classmethod", "getattr", "locals", "repr", "zip", "compile", "globals", "map", "reversed", "import", "complex", "hasattr", "max", "round")
        return df, sample(options, k=n_cols)

    def _rename_columns_solution(df, names):
        df_res = df.copy()
        df_res.columns = names
        return df_res

    def _do_one_test(valid=True):
        df, names = generate_random_case(valid=valid)
        df_original = df.copy()
        names_original = names[:]
        expected_solution = _rename_columns_solution(df, names)
        user_solution = rename_columns(df, names)
        if type(user_solution) != type(expected_solution):
            test.fail(
                f"You've returned object of {type(user_solution)}. You must return a DataFrame object")
            return
        test.expect(user_solution.equals(expected_solution),
                    f'Wrong output: Expected:\n{expected_solution}\n\nActual:\n{user_solution}')
        test.expect(df_original.equals(df),
                    "You must not modify the original DataFrame")

    @test.it('Random Valid Test Cases')
    def random_valid_test_cases():
        for _ in range(20):
            _do_one_test(valid=True)
