scrabble_values = dict(
    dict.fromkeys("AEIOULNRST", 1),
    **dict.fromkeys("DG", 2),
    **dict.fromkeys("BCMP", 3),
    **dict.fromkeys("FHVWY", 4),
    **dict.fromkeys("K", 5),
    **dict.fromkeys("JX", 8),
    **dict.fromkeys("QZ", 10)
)


def scrabble_score(st):
    return sum(scrabble_values.get(c, 0) for c in st.upper())
