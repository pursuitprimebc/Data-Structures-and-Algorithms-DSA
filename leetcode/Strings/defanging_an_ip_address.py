''' problem - Defanging an IP Address
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".
'''


class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged_address = ""
        for char in address:
            if char == ".":
                defanged_address += "[.]" 
            else:
                defanged_address += char
        return defanged_address