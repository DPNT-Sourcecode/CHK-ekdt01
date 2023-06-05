import math

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    checkout = Checkout()
    price = checkout.calculate_total_price(skus)
    return price


class Checkout:
    def __init__(self) -> None:
        self.prices = {
            'A':50,
            'B':30,
            'C':20,
            'D':15,
            'E':40
        }

        self.special_offers = {
            'A':[(5, 200), (3, 130)],
            'B':(2, 45),
            'E':(3, 80)
        }

    def calculate_total_price(self, order):
        if not isinstance(order, str):
            raise TypeError(f"Expected string, got {type(order).__name__}")
        item_count = {}
        total_price = 0
        for item in order:
            if item not in self.prices:
                return -1
            
            if item not in self.special_offers:
                total_price += self.prices[item]
                continue

            # if on special offer we need to keep track of the number of items and check if special offer needed
            item_count[item] = 1 if item not in item_count else item_count[item] + 1
            special_offer_amount = self.special_offers[item][0]
            special_offer_price = self.special_offers[item][1]

            # special offer needed
            if item_count[item] != 0 and item_count[item] % special_offer_amount == 0:
                total_price += special_offer_price - ( special_offer_amount - 1 ) * self.prices[item]
                continue

            # special offer not needed yet
            total_price += self.prices[item]    

        return total_price



        
# checkout = Checkout()

# print(checkout('AAAABBBCCDD') )
    

    
        


