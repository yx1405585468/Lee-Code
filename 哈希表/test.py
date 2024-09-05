import time

record = [1] * 100000000  # 创建一个包含100万个元素的列表，所有元素都是1

# 使用索引遍历
start_time = time.time()
for i in range(len(record)):
    if record[i] != 0:
        pass
end_time = time.time()
index_traversal_time = end_time - start_time

# 直接遍历值
start_time = time.time()
for val in record:
    if val != 0:
        pass
end_time = time.time()
value_traversal_time = end_time - start_time

print(f"索引遍历所需时间：{index_traversal_time} 秒")
print(f"值遍历所需时间：{value_traversal_time} 秒")

"""
事实上，遍历值比遍历索引的速度更快
索引遍历所需时间：10.65746259689331 秒
值遍历所需时间：5.434825658798218 秒
"""
