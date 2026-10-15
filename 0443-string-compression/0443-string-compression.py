class Solution:
    def compress(self, chars: list[str]) -> int:
        
        i = 0
        counter = 1
        prev = ""
        for char in chars:
            if char != prev:
                if counter >1:
                    for digit in str(counter):
                        chars[i] = digit
                        i+=1
                    # i +=1
                    counter = 1
                
                chars[i] = char
                prev = char
                i+=1
            
            else:
                counter+=1
        
        if counter>1:
            for digit in str(counter):
                chars[i] = digit
                i+=1
        # else:
        #     chars[i] = prev

        return i
