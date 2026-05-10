# Compare two version numbers version1 and version2, dotted

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        ar1 = version1.split('.')
        ar2 = version2.split('.')
        for i in range(0,len(ar1)):
            i1 = int(ar1[i])
            if i >= len(ar2):
                if i1 > 0:
                    return 1
                else:
                    continue

            i2 = int(ar2[i])
            if (i1 > i2):
                return 1
            
            if (i2 > i1):
                return -1
                
        for j in range(i, len(ar2)):
            if j >= len(ar1):
                if int(ar2[j]) > 0:
                    print "here " + str(j)
                    return -1
        
        return 0

