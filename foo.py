class Foo():

    def bigger1(self, num : int) -> bool:
        return num > 1
    
    def lowerOrEqual1(self, num : int) -> bool:
        if self.bigger1(num) == True:
            return False
        else :
            return True