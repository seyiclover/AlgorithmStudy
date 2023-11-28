# 첫째 줄 둘째 줄 입력 변수
import sys

n = int(sys.stdin.readline())
nums = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

def binarysearch(nums, target):
    lt=0
    rt=n-1
    while lt<=rt:
        mid=(lt+rt)//2
        if nums[mid]==target:
            return "yes"
        elif nums[mid]>target:
            rt=mid-1
        else:
            lt=mid+1
    return "no"

for target in targets:
    if binarysearch(nums, target)=="yes":
        print(1, end=' ')
    else:
        print(0, end=' ')
