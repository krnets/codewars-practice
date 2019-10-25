function litres(time) {
    return Math.floor(time * 0.5);
}

q = litres(2) // 1, 'should return 1 litre'
q
q = litres(1.4) // 0, 'should return 0 litres'
q
q = litres(12.3)//  6, 'should return 6 litres'
q
q = litres(0.82)//  0, 'should return 0 litres'
q
q = litres(11.8)// , 5, 'should return 5 litres'
q
q = litres(1787)//  893, 'should return 893 litres'
q
q = litres(0)//  0, 'should return 0 litres'
q