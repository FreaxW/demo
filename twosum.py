#leetcode题目：给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标

def twosum(li: list,target: int) ->list:
    dit = dict()
    for i in range(len(li) - 1):
        num = target - li[i]
        if num not in dit:
            dit[li[i]] = i
        else:
            return [dit[num],i]
            
if __name__ == '__main__':
    print(twosum([1,2,4,5,7],9))
            
