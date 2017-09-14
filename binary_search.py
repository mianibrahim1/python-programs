#python
#sample algorithm

class binary_search:
    def __init__(self):
        pass
    def find_number(self, array, find_num):
        self.first = 0
        self.last = len(array)
        self.not_found = False
        while not self.not_found:
            self.middle = int((self.last + self.first)/2)
            print self.first
            if array[self.middle] == find_num:
                return self.middle
            elif array[self.middle] < find_num:
                self.first = self.middle
            elif array[self.middle] > find_num:
                self.last = self.middle

            if self.last == 0 or self.first == len(array) - 1:
                self.not_found = True


#basic test cases
new_class = binary_search()
print new_class.find_number([1,2,3,4],5)
print new_class.find_number([1,2,3],2)
print new_class.find_number([1,2,3],1)
