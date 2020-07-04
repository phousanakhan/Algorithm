def rotate(self, nums: List[int], k: int) -> None:
    toRotate = 0
    while toRotate != k:
        tempList = (nums[0:-1])
        del nums[:-1]
        nums.extend(tempList)
        toRotate += 1