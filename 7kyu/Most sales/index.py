# 7kyu - Most sales

""" You work in the best consumer electronics corporation, and your boss wants to find out 
which three products generate the most revenue. Given 3 lists of the same length like these:

    products: ["Computer", "Cell Phones", "Vacuum Cleaner"]
    amounts: [3, 24, 8]
    prices: [199, 299, 399]

return the three product names with the highest revenue (amount * price).

Note: if multiple products have the same revenue, order them according to their original positions in the input list. """

# def top3(products, amounts, prices):
#     result = []
#     revenue = [amounts[i] * prices[i] for i in range(len(products))]
#     for i in range(3):
#         highest = revenue.index(max(revenue))
#         result.append(products[highest])
#         revenue[highest] = -1
#     return result

# from heapq import nlargest

# def top3(products, amounts, prices):
#     items = zip(products, amounts, prices)
#     return [p for p, _, _ in nlargest(3, items, key=lambda x: x[1] * x[2])]


# def top3(products, amounts, prices):
#     revenue = [(products[i], amounts[i] * prices[i])
#                for i in range(len(products))]
#     return [item[0] for item in sorted(revenue, key=lambda x: x[1], reverse=True)[:3]]

def top3(products, amounts, prices):
    revenue = {}
    for product, amount, price in zip(products, amounts, prices):
        revenue[product] = amount * price
    return sorted(revenue, key=lambda x: revenue[x], reverse=True)[:3]


q = top3(["Computer", "Cell Phones", "Vacuum Cleaner"], [3, 24, 8], [
         199, 299, 399]), ["Cell Phones", "Vacuum Cleaner", "Computer"]
q
q = top3(["Cell Phones", "Vacuum Cleaner", "Computer", "Autos", "Gold", "Fishing Rods", "Lego", " Speakers"], [
         5, 25, 2, 7, 10, 3, 2, 24], [51, 225, 22, 47, 510, 83, 82, 124]), ['Vacuum Cleaner', 'Gold', ' Speakers']
q
q = top3(["Cell Phones", "Vacuum Cleaner", "Computer", "Autos", "Gold", "Fishing Rods", "Lego", " Speakers"], [
         0, 12, 24, 17, 19, 23, 120, 8], [9, 24, 29, 31, 51, 8, 120, 14]), ['Lego', 'Gold', 'Computer']
q
