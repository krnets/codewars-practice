# 7kyu - Converting Currency II

""" Given the current exchange rate between the USD and the EUR is 1.1363636 
write a function that will accept the Curency type to be returned 
and a list of the amounts that need to be converted.

Don't forget this is a currency so the result will need to be rounded to the second decimal.

'USD' Return format should be '$100,000.00'
'EUR' Return format for this kata should be '100,000.00€'

to_currency is a string with values 'USD','EUR' , values_list is a list of floats

solution(to_currency,values)

solution('USD',[1394.0, 250.85, 721.3, 911.25, 1170.67]) 
# ['$1,584.09', '$285.06', '$819.66', '$1,035.51', '$1,330.31']

solution('EUR',[109.45, 640.31, 1310.99, 669.51, 415.54]) 
# ['96.32€', '563.47€', '1,153.67€', '589.17€', '365.68€'] """

# EURUSD_xrate = 1.1363636

# def solution(to_cur, value):
#     if to_cur == 'USD':
#         return [f'${EURUSD_xrate * x:,.2f}' for x in value]
#     elif to_cur == 'EUR':
#         return [f'{x / EURUSD_xrate:,.2f}€' for x in value]


# EUR_USD = 1.1363636

# def solution(to_cur, values):
#     return [f'${EUR_USD * v:,.2f}' if to_cur == 'USD' else f'{v / EUR_USD:,.2f}€' for v in values]

def solution(to_cur, values):
    rate, fmt = {
        'USD': (1.1363636, '${:,.2f}'),
        'EUR': (1 / 1.1363636, '{:,.2f}€'),
    }[to_cur]
    values = [v * rate for v in values]
    return list(map(fmt.format, values))


q = solution('USD', [1.01, 83.29, 5.0, 23.23, 724.22])
q
# ['$1.15', '$94.65', '$5.68', '$26.40', '$822.98']
q = solution('USD', [1394.0, 250.85, 721.3, 911.25, 1170.67])
q
# ['$1,584.09', '$285.06', '$819.66', '$1,035.51', '$1,330.31']
q = solution('EUR', [109.45, 640.31, 1310.99, 669.51, 415.54])
q
# ['96.32€', '563.47€', '1,153.67€', '589.17€', '365.68€']
q = solution('EUR', [589.29, 662.31, 1349.71, 117.93, 8.25])
q
# ['518.58€', '582.83€', '1,187.74€', '103.78€', '7.26€']
