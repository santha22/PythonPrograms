class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        amp = {}
        bmp = {}
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in range(len(s)):
            if i < len(s) // 2:
                if s[i] in vowels:
                    if s[i] in amp:
                        amp[s[i]] += 1
                    
                    else:
                        amp[s[i]] = 1

            else:
                if s[i] in vowels:
                    if s[i] in bmp:
                        bmp[s[i]] += 1

                    else:
                        bmp[s[i]] = 1

        cnt1 =  cnt2 = 0
        
        for it in amp:
            cnt1 += amp[it]

        for it in bmp:
            cnt2 += bmp[it]

        if cnt1 == cnt2:
            return True

        return False


        
