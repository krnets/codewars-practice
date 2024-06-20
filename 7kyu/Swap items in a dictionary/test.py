import codewars_test as test
from kata import switch_dict

before = {
          'Ice': 'Cream',
          'Age': '21',
          'Light': 'Cream',
          'Double': 'Cream'
          }

expected_ans = {
                'Cream': ['Ice', 'Double', 'Light'],
                '21': ['Age']
                }


usr_ans = switch_dict(before)

# Sort lists inside dict
usr_ans = {k: sorted(usr_ans[k]) for k in usr_ans}
expected_ans = {k: sorted(expected_ans[k]) for k in expected_ans}

test.describe('Basic tests')

test.it('Sample case')
test.assert_equals(usr_ans, expected_ans)