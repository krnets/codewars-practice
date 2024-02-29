def recycle(a):
    bins = { bin_type: [] for bin_type in "paper glass organic plastic".split() }

    for item in a:
        mat1 = item.get("material")
        mat2 = item.get("secondMaterial")
        item_type = item.get("type")
        bins[mat1].append(item_type)

        if mat2:
            bins[mat2].append(item_type)

    return tuple(bins.values())
