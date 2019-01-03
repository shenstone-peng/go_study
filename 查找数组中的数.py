# 题目描述
### 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

class solution:
    def find(self,target,array):
        ans = False
        if(array == None):
           return ans
        else:
            row=len(array)
            col=len(array[0])
            i=row-1
            j=0
        while(i>=0 and j<col):
            if(target == array[i][j]):
                ans = True
                break
            elif(target < array[i][j]):
                i=i-1
            elif(target > array[i][j]):
                j=j+1
        return ans
    
