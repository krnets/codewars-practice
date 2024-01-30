def xbonacci(signature, n):
    m = len(signature)
    while len(signature) < n:
        signature.append(sum(signature[-m:]))
    return signature[:n]