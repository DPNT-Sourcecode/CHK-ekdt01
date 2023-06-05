import math

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    legal_items = ['A', 'B', 'C', 'D']
    item_count = {}
    for item in skus:
        if item not in legal_items:
            return -1
        
        item_count[item] = 1 if item not in item_count else item_count[item] + 1


class Checkout:
    def __init__(self, order) -> None:
        self.prices = {
            'A':50,
            'B':30,
            'C':20,
            'D':15
        }

        self.special_offers = {
            'A':(3, 130),
            'B':(2, 45)
        }

        self.skus = order

    def calculate_total_price(self):
        item_count = {}
        total_price = 0
        for item in self.skus:
            if item not in self.prices:
                return -1
            
            if item not in self.special_offers:
                total_price += item * self.prices[item]
                continue

            item_count[item] = 1 if item not in item_count else item_count[item] + 1
            special_offer_amount = self.special_offers[item][0]
            special_offer_price = self.special_offers[item][1]
            if item_count[item] != 0 and item_count[item] % special_offer_amount == 0:
                price_amount_to_add = special_offer_price - ( special_offer_amount - 1 ) * self.prices[item]
            else:
                price_amount_to_add = self.prices[item]
            
            total_price += price_amount_to_add



        

    

    
        


