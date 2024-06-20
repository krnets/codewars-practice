import codewars_test as test
from kata import encipher

@test.describe("Unusual cipher")
def unusual_cipher():
    
    @test.it('Sample tests')
    def test_case():     
            plaintexts =  ['Jackdaws love my big sphinx of quartz',
                          'Pack my box with five dozen liquor jugs',
                          'The quick onyx goblin jumps over the lazy dwarf',
                          'Cwm fjord bank glyphs vext quiz',
                          'How razorback jumping frogs can level six piqued gymnasts',
                          'Cozy lummox gives smart squid who asks for job pen'
                          ]
            ciphers = ['EPBNOEZQ ANAD XF KBH QFBRKE QY SVLIUWM',
                     'LYBN XF DKG YBPS METD OSVRO PRNWNE RTHQ',
                     'ZBX OTRBN QOXG DQCPRK RTIFK QADI UDM AYWF GVLEYM',
                     'GUH MEKEC DPON CYFLSZ ADIW NWMT',
                     'DSU XFVNEDPBN RTIFRKH YENHQ DLU RDARA KMI YXKVRG HFXOLKZQM',
                     'DNWF RLIMES GQETM OMQEF IUKST RGV DSFO NKA SER KDAIQR'
                     ]
        
            for i,j in zip(plaintexts, ciphers):
                    test.assert_equals(encipher(i, 'playfair jexample'), j, 'whoops! try again..')