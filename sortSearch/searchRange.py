def searchRange(self, nums, target):
    def search(low, high):
        if nums[low] == target == nums[high]:
            return [low, high]
        if nums[low] <= target <= nums[high]:
            mid = (low + high) / 2
            l, r = search(low, mid), search(mid+1, high)
            return max(l, r) if -1 in l+r else [l[0], r[1]]
        return [-1, -1]
    return search(0, len(nums)-1)
