class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        my_list_of_s = {}
        my_list_of_t = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            my_list_of_s[s[i]] = my_list_of_s.get(s[i],0) + 1
            my_list_of_t[t[i]] = my_list_of_t.get(t[i],0) + 1

        if my_list_of_t == my_list_of_s:
            return True
        else :
            return False
