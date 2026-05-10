# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

# 95 % faster, 50 % memory

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        rv = ''
        l = len(s)
        stack = []
        i = 0
        
        while (i < l):
            c = s[i]
            if c.isnumeric():
                # read the counter
                count = ''
                while (s[i] != '['):
                    count += s[i]
                    i += 1
                    
                stack.append([int(count), ''])
                
                i += 1 # skip the [
            elif (c == ']'):
                # build the string
                res = ''
                [count, chunk] = stack.pop()
                for y in range(count):
                    res += chunk
                    
                if len(stack) > 0:
                    stack[-1][1] += res
                else:
                    rv += res
                
                i += 1
            else:
                if len(stack) > 0:
                    stack[-1][1] += c
                else:
                    rv += c
                i += 1            
        
        return rv

