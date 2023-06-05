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
            'K':70,
            'L':90,
            'M':15,
            'N':40,
            'O':10,
            'P':50,
            'Q':30,
            'R':50,
            'S':20,
            'T':20,
            'U':40,
            'V':50,
            'W':20,
            'X':17,
            'Y':20,
            'Z':21
        }
        

        self.special_free_items = {
            'E':[(2, 'B')],
            'N':[(3, 'M')],
            'R':[(3, 'Q')],
        }

        # have set this in order of most to least expensive 
        # this way it will remove it in that order and best deal for customer
        self.multi_special_offers = {
            'ZSTYX': (3, 45)
        }

        self.single_special_offers = {
            'A':[(3, 130), (5, 200)],
            'B':[(2, 45)],
            'F':[(3, 2 * self.prices['F'])],
            'H':[(5, 45), (10, 80)],
            'K':[(2, 120)],
            'P':[(5, 200)],
            'Q':[(3, 80)],
            'U':[(4, 3 * self.prices['U'])],
            'V':[(2, 90), (3, 130)],
        }

        for offer in self.single_special_offers:
            self.single_special_offers[offer].sort(key = lambda x: x[1] / x[0])

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
    
    def calculate_special_free_item_offers(self, order):
        for item in self.special_free_items:
            if item in order:
                specials = self.special_free_items[item]
                for offer in specials:
                    item_count = self.calculate_special_free_item(item_count, item, offer)
        return item_count
    
    def calculate_special_multi_item_offers(self, item_count, total_price):
        for offer in self.multi_special_offers:
            total_count = sum(item_count[key] for key in offer if key in item_count)

            offer_price, remaining = self.calculate_special(total_count, self.multi_special_offers[offer])
            
            item_price_order = list(offer)
            item_price_order.sort(key = lambda x: self.prices[x])
            
            for item in item_price_order:
                
                if remaining <= 0:
                    break

                if item not in item_count:
                    continue
                
                if item_count[item] < remaining:
                    offer_price += self.prices[item] * item_count[item]
                    remaining -= item_count[item]
                    item_count[item] = 0
                else:
                    offer_price += self.prices[item] * remaining
                    item_count[item] -= remaining
                    remaining = 0

            for item in item_price_order:
                item_count[item] = 0
            
            total_price += offer_price
        return item_count, total_price

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
        
        item_count = self.calculate_special_free_item_offers(order)
        item_count, total_price = self.calculate_special_multi_item_offers(item_count, total_price)



        for offer in self.multi_special_offers:
            total_count = sum(item_count[key] for key in offer if key in item_count)

            offer_price, remaining = self.calculate_special(total_count, self.multi_special_offers[offer])
            
            item_price_order = list(offer)
            item_price_order.sort(key = lambda x: self.prices[x])
            
            for item in item_price_order:
                
                if remaining <= 0:
                    break

                if item not in item_count:
                    continue
                
                if item_count[item] < remaining:
                    offer_price += self.prices[item] * item_count[item]
                    remaining -= item_count[item]
                    item_count[item] = 0
                else:
                    offer_price += self.prices[item] * remaining
                    item_count[item] -= remaining
                    remaining = 0

            for item in item_price_order:
                item_count[item] = 0
            
            total_price += offer_price


        # we need to make sure the special offers are in order of the best value per item
        for item in self.single_special_offers:
            if item in order:
                specials = self.single_special_offers[item]
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
        

print(checkout('CXYZYZC'))


