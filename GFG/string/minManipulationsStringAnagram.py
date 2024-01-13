class Solution:
    def minManipulation(self, n, s, t): 
        # code here
        smap = {}
        tmap = {}

        for i in s:
            smap[i] = 1 + smap.get(i, 0)

        for j in t:
            tmap[j] = 1 + tmap.get(j, 0) 
            
        # print(smap, tmap)

        cnt = 0

        for it in tmap:
            if it not in smap:
                cnt += tmap[it]

            if it in smap and tmap[it] > smap[it]:
                cnt += tmap[it] - smap[it]

        return cnt
