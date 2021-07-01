class Solution:
    def defangIPaddr(self, address):
        answer=address.replace(".","[.]")
        return answer