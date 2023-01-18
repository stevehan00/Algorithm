    def defangIPaddr(self, address: str) -> str:
        lst = address.split('.')
        s = ""
        for i in range(len(lst)):
            if i == len(lst) - 1:
                s += lst[i]
            else:
                s+= lst[i] + "[.]"
    
        return s