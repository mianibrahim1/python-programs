class Solution(object):
    def isHappy(self, n):
        string = str(n), suming = 0, dictionary = {}, not_found = True
        while not_found:
            for i in range(len(string)):
                suming += int(string[i]) ** 2
            string = str(suming)
            suming = 0
            if string == '1':
                return True
            if dictionary.get(string,0) == 1:
                not_found = True
            else:
                dictionary[string] = dictionary.get(string,0) + 1
        return False
