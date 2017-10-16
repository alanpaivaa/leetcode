class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        consecutive_empty = 1
        can_place_flowers_count = 0
        for flower_spot in flowerbed:
            if flower_spot == 0:
                consecutive_empty += 1
            elif flower_spot == 1:
                if consecutive_empty >= 3:
                    can_place_flowers_count += (consecutive_empty - 1) / 2
                consecutive_empty = 0

        if consecutive_empty >= 2:
            can_place_flowers_count += consecutive_empty / 2

        return n <= can_place_flowers_count