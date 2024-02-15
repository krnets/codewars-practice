import codewars_test as test
from kata import shortener


@test.describe("Sample tests")
def sample_tests():
    @test.it("Tests")
    def _():
        tc1 = ('No one expects the Spanish Inquisition! Our chief weapon is surprise, '
               'fear and surprise; two chief weapons, fear, surprise, and ruthless efficiency! '
               'And that will be it.')
        tc1x = ('No one expects the Spanish Inquisition! Our chief weapon is surprise, '
                'fear and surprise; two chief weapons, fear,Surprise,AndRuthlessEfficiency!'
                'AndThatWillBeIt.')
        test.assert_equals(shortener(tc1), tc1x)

        tc2 = "This message is already short enough!"
        test.assert_equals(shortener(tc2), tc2)

        tc3 = ('ThereIsNoSpoonThereIsNoSpoonThereIsNoSpoonThereIsNoSpoonThereIsNoSpoon'
               'ThereIsNoSpoonThereIsNoSpoonThereIsNoSpoonThereIsNoSpoonThereIsNoSpoon'
               'ThereIsNoSpoonThereIsNoSpoonThereIsNoSpoon')
        test.assert_equals(shortener(tc3), tc3)

        tc4 = ('SMS messages are limited to 160 characters. It tends to be irritating, '
               'especially when freshly written message is 164 characters long. '
               'SMS messages are limited to 160 characters. It tends to be irritating, '
               'especially when freshly written message is 164 characters long.')
        tc4x = ('SMSMessagesAreLimitedTo160Characters.ItTendsToBeIrritating,Especially'
                'WhenFreshlyWrittenMessageIs164CharactersLong.SMSMessagesAreLimitedTo160'
                'Characters.ItTendsToBeIrritating,EspeciallyWhenFreshlyWrittenMessageIs'
                '164CharactersLong.')
        test.assert_equals(shortener(tc4), tc4x)