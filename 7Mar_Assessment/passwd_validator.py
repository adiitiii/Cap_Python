class Solution:
    def strong_passwords(self, passwords):
        strong = []
        ## Write your code here
        
        for pwd in passwords:
            if (len(pwd) >= 8 and
                any(c.isupper() for c in pwd) and
                any(c.isdigit() for c in pwd) and
                any(c in "@#$" for c in pwd)):
                
                strong.append(pwd)
       
        return strong