function otherAngle(a, b) {
    // let sumOfTwoAngles = a + b 
    // return thirdAngle = 180 - sumOfTwoAngles
    if (a < 0 || b < 0) {
        return 0
    }
    if ((a + b) >= 180) {
        return 0
    }
    return 180 - a - b
}


q = otherAngle(30, 60)
q

// Test.assertEquals(otherAngle(30, 60), 90);

// Test.assertEquals(otherAngle(60, 60), 60);

// Test.assertEquals(otherAngle(43, 78), 59);

// Test.assertEquals(otherAngle(10, 20), 150);