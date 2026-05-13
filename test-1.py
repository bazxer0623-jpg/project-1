#1.一維 ndarray

import numpy as np

a = np.array([1, 2, 3])

print(a.shape)



#2.二維 ndarray

import numpy as np

b = np.array([[1, 2, 3],

        [4, 5, 6]])

print(b.shape)



#3.三維 ndarray

#一矩陣範例：

import numpy as np

c = np.array([[[1, 2],

               [3, 4]]])

print(c.shape)


#4.三維ndarray
#二矩陣範例：
import numpy as np

c = np.array([[[1, 2],[3,4]],

    [[5, 6],[7, 8]]])

print(c.shape)


#5.axis 運算的方向
axis = 0#（直的 ↓）

axis = 1#（橫的 →）


import numpy as np
sales = np.array([

    [100, 120, 90],

    [110, 130, 95],

    [105, 125, 100]

])

print("每天銷售:", sales.sum(axis=1))

print("每商品銷售:", sales.sum(axis=0))

print("總銷售:", sales.sum())


#6.索引範例
import numpy as np

a = np.array([10, 20, 30, 40, 50])

print("第五題",a[0])


#7.切片array[起始:結束:步長] 範例：

import numpy as np

a = np.array([10, 20, 30, 40, 50])

print(a[0:4:2])



#8.整列 / 整欄存取範例：
import numpy as np

a = np.array([

[10, 20, 30],

[40, 50, 60],

[70, 80, 90]

])

print(a[1])

print(a[:,2])

print(a[0,:])

#9.整列 / 整欄存取範例：
import numpy as np

a = np.array([

[10, 20, 30],

[40, 50, 60],

[70, 80, 90]

])

print(a[1])

print(a[:,2])

print(a[0,:])

#10.二維 ndarray 的切片語法結構：array[列的範圍, 欄的範圍 ]
import numpy as np

a = np.array([

[10, 20, 30],

[40, 50, 60],

[70, 80, 90]

])

print(a[0:2,:])

print(a[:,1:3])

print(a[0:2,1:3])



#11.三維 ndarray 的切片
#語法結構：array[(層, 列, 欄) ]

import numpy as np

a = np.array([

[[10, 20, 30],

[40, 50, 60],

[70, 80, 90]],

[[100, 110, 120],

[130, 140, 150],

[160, 170, 180]]

])

print(a[0:2,:,:])

print(a[:,1:3,:])

print(a[0:2,:,1:3])