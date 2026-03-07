class Solution:
    def unique_products(self, products):
        result = []
        
        for p in products:
            if products.count(p) == 1:
                result.append(p)

        return result