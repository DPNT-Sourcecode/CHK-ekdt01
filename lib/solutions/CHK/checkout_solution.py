import math


class Checkout:
    def __init__(self) -> None:
        self.prices = {
            'A':50,
            'B':30,
            'C':20,
            'D':15,
            'E':40,
            'F':10,
            'G':20,
            'H':10,
            'I':35,
            'J':60,
            'K':80,
            'L':90,
            'M':15,
            'N':40,
            'O':10,
            'P':50,
            'Q':30,
            'R':50,
            'S':30,
            'T':20,
            'U':40,
            'V':50,
            'W':20,
            'X':90,
            'Y':10,
            'Z':50
        }
        

        self.special_free_items = {
            'E':[(2, 'B')],
            'N':[(3, 'M')],
            'R':[(3, 'Q')],
        }

        self.special_offers = {
            'A':[(3, 130), (5, 200)],
            'B':[(2, 45)],
            'F':[(3, 2 * self.prices['F'])],
            'H':[(5, 45), (10, 80)],
            'K':[(2, 150)],
            'P':[(5, 200)],
            'Q':[(3, 80)],
            'U':[(4, 3 * self.prices['U'])],
            'V':[(2, 90), (3, 130)],
        }

        for offer in self.special_offers:
            self.special_offers[offer].sort(key = lambda x: x[1] / x[0])

    def calculate_special(self, count, special):
        special_amount, special_price = special
        special_count = math.floor(count / special_amount)
        remaining = count % special_amount
        total_price = special_price * special_count
        return total_price, remaining

    def calculate_special_free_item(self, item_count, item, special):
        count = item_count[item]
        special_amount, free_item = special
        special_count = math.floor(count / special_amount)
        if free_item in item_count:
            item_count[free_item] = max(0, item_count[free_item] - special_count)

        return item_count
    
    def calculate_price(self, item, count):
        return self.prices[item] * count

    def calculate_total_price(self, order):
        if not isinstance(order, str):
            raise TypeError(f"Expected string, got {type(order).__name__}")
        item_count = {}
        total_price = 0
        for item in order:
            if item not in self.prices:
                return -1

            # if on special offer we need to keep track of the number of items and check if special offer needed
            item_count[item] = 1 if item not in item_count else item_count[item] + 1
        
        for item in self.special_free_items:
            if item in order:
                specials = self.special_free_items[item]
                for offer in specials:
                    item_count = self.calculate_special_free_item(item_count, item, offer)


        # we need to make sure the special offers are in order of the best value per item
        for item in self.special_offers:
            if item in order:
                specials = self.special_offers[item]
                for offer in specials:
                    offer_price, remaining = self.calculate_special(item_count[item], offer)
                    item_count[item] = remaining
                    total_price += offer_price

        for item in self.prices:
            if item in item_count:
                total_price += self.calculate_price(item, item_count[item])


        return total_price


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    checkout = Checkout()
    price = checkout.calculate_total_price(skus)
    return price 
        
# print(checkout("A"))
# print(checkout("B"))
# print(checkout("C"))
# print(checkout("D"))
# print(checkout("EEEEBBBB"))




