import codewars_test as test
from solution import max_common
from random import randint, sample
import string
import pandas as pd
import numpy as np

@test.describe('Example Tests')
def example_tests():
    @test.it('Sample test')
    def sample_tests():
        df_a = pd.DataFrame(data=[[2.5, 2.0, 2.0], [2.0, 2.0, 2.0]], columns=list('ABC'))
        df_b = pd.DataFrame(data=[[1.0, 6.0, 7.0, 1.0], [8.5, 1.0, 9.0, 1.0]], columns=list('CBDE'))
        df_out = pd.DataFrame(data=[[2.5, 6.0, 2.0], [2.0, 2.0, 8.5]], columns=list('ABC'))
        test.expect(max_common(df_a, df_b).equals(df_out))
    
@test.describe('Random Tests')
def random_tests():
    
    def generate_random_case(min_rows=0, max_rows=30, min_cols=0, max_cols=len(string.ascii_uppercase)//2, min_value=0, max_value=100): 
        n_rows, a_cols, b_cols = randint(min_rows, max_rows), randint(min_cols, max_cols), randint(0, max_cols)
        df_a = pd.DataFrame(data=np.random.uniform(min_value, max_value, size=(n_rows, a_cols)), columns=sample(string.ascii_uppercase, k=a_cols))
        df_b = pd.DataFrame(data=np.random.uniform(min_value, max_value, size=(n_rows, b_cols)), columns=sample(string.ascii_uppercase, k=b_cols))
        return df_a, df_b

    def _max_common_solution(df_a, df_b): 
        df_res = df_a.copy()
        common = set(df_a.columns).intersection(set(df_b.columns))
        for col in common: 
            df_res[col] = [max(x, y) for x, y in zip(df_a[col], df_b[col])]
        return df_res

    def _do_one_test(valid=True):
        df_a, df_b = generate_random_case()
        df_original_a = df_a.copy()
        df_original_b = df_b.copy()
        
        expected = _max_common_solution(df_a, df_b)
        actual = max_common(df_a, df_b)
        
        dtypes_correct = actual.dtypes.equals(expected.dtypes)
        input_a_correct = df_original_a.equals(df_a)
        input_b_correct = df_original_b.equals(df_b)
        if not dtypes_correct:
            test.fail(f"Column types are different:\n\n{actual.dtypes}\n\nShould be\n\n{expected.dtypes}")
        elif not input_a_correct:
            test.fail(f"Don't modify the input\n\n{df_original_a}")
        elif not input_b_correct:
            test.fail(f"Don't modify the input\n\n{df_original_b}")
        else:    
            test.expect(actual.equals(expected), f"{actual}\n\nShould be\n\n{expected}")
            
    @test.it('Random Valid Test Cases')
    def random_valid_test_cases():
        for _ in range(30):
            _do_one_test()