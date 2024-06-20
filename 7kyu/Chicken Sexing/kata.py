# def correctness(bobs_decisions, expert_decisions):
#     return sum(
#         (1, 0, 0.5)[(b != e) + (b != e and "?" in (b, e))]
#         for b, e in zip(bobs_decisions, expert_decisions)
#     )


def correctness(bobs_decisions, expert_decisions):
    return sum(b == e or 0.5 * ("?" in (b, e)) 
               for b, e in zip(bobs_decisions, expert_decisions))
