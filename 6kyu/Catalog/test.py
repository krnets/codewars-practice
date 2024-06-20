import codewars_test as test
from kata import catalog

s = """<prod><name>drill</name><prx>99</prx><qty>5</qty></prod>
<prod><name>hammer</name><prx>10</prx><qty>50</qty></prod>
<prod><name>screwdriver</name><prx>5</prx><qty>51</qty></prod>
<prod><name>table saw</name><prx>1099.99</prx><qty>5</qty></prod>
<prod><name>saw</name><prx>9</prx><qty>10</qty></prod>
<prod><name>chair</name><prx>100</prx><qty>20</qty></prod>
<prod><name>fan</name><prx>50</prx><qty>8</qty></prod>
<prod><name>wire</name><prx>10.8</prx><qty>15</qty></prod>
<prod><name>battery</name><prx>150</prx><qty>12</qty></prod>
<prod><name>pallet</name><prx>10</prx><qty>50</qty></prod>
<prod><name>wheel</name><prx>8.80</prx><qty>32</qty></prod>
<prod><name>extractor</name><prx>105</prx><qty>17</qty></prod>
<prod><name>bumper</name><prx>150</prx><qty>3</qty></prod>
<prod><name>ladder</name><prx>112</prx><qty>12</qty></prod>
<prod><name>hoist</name><prx>13.80</prx><qty>32</qty></prod>
<prod><name>platform</name><prx>65</prx><qty>21</qty></prod>
<prod><name>car wheel</name><prx>505</prx><qty>7</qty></prod>
<prod><name>bicycle wheel</name><prx>150</prx><qty>11</qty></prod>
<prod><name>big hammer</name><prx>18</prx><qty>12</qty></prod>
<prod><name>saw for metal</name><prx>13.80</prx><qty>32</qty></prod>
<prod><name>wood pallet</name><prx>65</prx><qty>21</qty></prod>
<prod><name>circular fan</name><prx>80</prx><qty>8</qty></prod>
<prod><name>exhaust fan</name><prx>62</prx><qty>8</qty></prod>
<prod><name>window fan</name><prx>62</prx><qty>8</qty></prod>"""


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(catalog(s, "ladder"), "ladder > prx: $112 qty: 12")
        test.assert_equals(
            catalog(s, "saw"),
            "table saw > prx: $1099.99 qty: 5\r\nsaw > prx: $9 qty: 10\r\nsaw for metal > prx: $13.80 qty: 32",
        )
        test.assert_equals(catalog(s, "wood pallet"), "wood pallet > prx: $65 qty: 21")
        test.assert_equals(
            catalog(
                "<prod><name>extractor</name><prx>24.8</prx><qty>12</qty></prod>\n\n<prod><name>exhaust fan</name><prx>93.5</prx><qty>8</qty></prod>\n\n<prod><name>bicycle wheel</name><prx>13.1</prx><qty>20</qty></prod>\n\n<prod><name>car battery</name><prx>12.2</prx><qty>45</qty></prod>\n\n<prod><name>bumper</name><prx>24.8</prx><qty>20</qty></prod>\n\n<prod><name>saw</name><prx>34.00</prx><qty>12</qty></prod>\n\n<prod><name>wood pallet</name><prx>17.6</prx><qty>17</qty></prod>\n\n<prod><name>exhaust fan</name><prx>20.00</prx><qty>8</qty></prod>\n\n<prod><name>circular fan</name><prx>24.8</prx><qty>15</qty></prod>\n\n<prod><name>screwdriver</name><prx>128.00</prx><qty>14</qty></prod>\n\n<prod><name>exhaust fan</name><prx>71.4</prx><qty>9</qty></prod>\n\n<prod><name>car battery</name><prx>13.1</prx><qty>12</qty></prod>\n\n<prod><name>hoist</name><prx>12.2</prx><qty>20</qty></prod>\n\n<prod><name>saw</name><prx>13.1</prx><qty>33</qty></prod>\n\n<prod><name>table saw</name><prx>34.00</prx><qty>50</qty></prod>\n\n",
                "saw",
            ),
            "saw > prx: $34.00 qty: 12\r\nsaw > prx: $13.1 qty: 33\r\ntable saw > prx: $34.00 qty: 50",
        )
