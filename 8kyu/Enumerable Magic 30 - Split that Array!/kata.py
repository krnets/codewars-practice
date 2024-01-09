def partition(arr, classifier_method):
    left, right = [], []

    for x in arr:
        if classifier_method(x):
            left.append(x)
        else:
            right.append(x)

    return left, right
