#12.廣播（Broadcasting）
import numpy as np

a = np.array([1, 2, 3])

b = 10

c = a + b

print(c)

#13.範例 ：某公司3 天的銷售資料如表，現在公司決定每個商品統一調漲價格：商品 A +10 元，商品 B +20 元，商品 C +30 元，請使用廣播計算調整後的銷售數據。
import numpy as np

a = np.array([

    [100, 120, 90],

    [110, 130, 95],

    [105, 125, 100]

])

b = np.array([10, 20, 30])

c = a + b

print("原始銷售：",a)

print("調整金額：",b)

print("調整後銷售：",c)

#14.常用統計函數：


#函數 說明
#sum() 加總
#mean() 平均
#max() 最大值
#min() 最小值
#argmax() 最大值的索引
#argmin() 最小值的索引

#15.常用統計函數：
import numpy as np

a = np.array([10, 50, 30])

print(np.argmax(a))

print(np.argmin(a))

#16.常用統計函數：
import numpy as np

a = np.array(["A", "B", "C"])

b = np.array([10, 20, 30])

c = np.argmax(b)

d = np.argmin(b)

print("最大的品項:", a[c])

print("最小的品項:", a[d])