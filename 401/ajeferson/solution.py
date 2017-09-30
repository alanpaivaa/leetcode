class Solution(object):

    # Time complexity: O(4^N*6^N)
    # Space complexity: O(1)
    def hh(self, n, ih, ch, results):
        self.hm(n, ch, 0, 0, results)
        for i in range(ih, 4):
            self.hh(n - 1, i+1, ch + 2**i, results)

    def hm(self, n, ch, im, cm, results):
        if ch > 11 or cm > 59: return
        if n == 0:
            results.append("%01d:%02d" % (ch, cm))
        for i in range(im, 6):
            self.hm(n - 1, ch, i+1, cm + 2**i, results)

    def readBinaryWatch(self, n):
        results = []
        self.hh(n, 0, 0, results)
        return results
