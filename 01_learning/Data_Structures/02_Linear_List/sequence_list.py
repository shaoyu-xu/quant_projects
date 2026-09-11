class SqList: # 顺序表类
    def __init__(self): 
        self.initcapacity = 5 # 初始容量设为5
        self.capacity = self.initcapacity # 容量设置为初始容量
        self.data = [None] * self.capacity # 设置顺序表的空间
        self.size = 0 # 长度设置为0

# 线性表的基本运算算法

    def resize(self, newcapacity): # 改变顺序表的容量为newcapacity
        assert newcapacity >= 0 #检查参数正确性的断言
        olddata = self.data # 保持顺序表的原始数据
        self.data = [None] * newcapacity # 重新设置顺序表的空间
        for i in range(self.size): # 将原始数据复制到新的顺序表
            self.data[i] = olddata[i]

# 整体建立顺序表

    def CreateList(self, a):
        self.size = 0
        for i in range(0, len(a)):
            if self.size == self.capacity: # 出现溢出
                self.resize(2 * self.capacity) # 容量加倍
            self.data[self.size] = a[i] # 添加元素a[i]
            self.size += 1 # 顺序表长度加1

# 顺序表的基本运算算法

    def Add(self, e): # 在顺序表的末尾添加一个元素e
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        self.data[self.size] = e
        self.size += 1

    def getsize(self): # 求顺序表的长度
        return self.size

    def __getitem__(self, i): # 求序号i的元素值
        assert 0 <= i < self.size # 检查参数i正确性的断言
        return self.data[i]

    def __setitem__(self, i, e): # 设置序号i的元素值
        assert 0 <= i < self.size
        self.data[i] = e

    def GetNo(self, e): # 查找第一个为e的元素的序号
        i = 0
        while i < self.size and self.data[i] != e:
            i += 1
        if (i >= self.size):
            return -1
        else:
            return i

    def Insert(self, i, e): # 在顺序表中序号i的位置上插入元素e
        assert 0 <= i <= self.size
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        for j in range(self.size, i, -1): # 将data[i]及后面的元素后移一个位置
            self.data[j] = self.data[j-1]
        self.data[i] = e # 插入元素e
        self.size += 1 # 长度加1

    def Delete(self, i): # 在顺序表中删除序号i的元素
        assert 0 <= i <= self.size - 1
        for j in range(i, self.size-1):
            self.data[j] = self.data[j+1] # 将data[i]后面的元素前移一个位置
        self.size -= 1
        if self.capacity > self.initcapacity and self.size <= self.capacity/4:
            self.resize(self.capacity//2) # 容量减半

    def display(self): # 输出顺序表
        for i in range(0, self.size):
            print(self.data[i], end = ' ')
        print()



