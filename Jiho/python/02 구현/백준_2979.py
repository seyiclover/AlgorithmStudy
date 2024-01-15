# 1대, 2대, 3대
A, B, C = map(int, input().split(' '))

# 차 들어온 시간, 나간 시간
c1_in, c1_out = map(int, input().split(' '))
c2_in, c2_out = map(int, input().split(' '))
c3_in, c3_out = map(int, input().split(' '))

# 총 시간
merged = [c1_in, c1_out, c2_in, c2_out, c3_in, c3_out]
merged = sorted(merged)

merged_times = {i: 0 for i in range(merged[0], merged[-1])}

# 각 차가 머문 시간
car1 = {i: 0 for i in range(c1_in, c1_out)}
car2 = {i: 0 for i in range(c2_in, c2_out)}
car3 = {i: 0 for i in range(c3_in, c3_out)}

for idx1, value1 in merged_times.items():

    # car1
    for idx2, value2 in car1.items():
        if idx1 == idx2: 
            merged_times[idx1] += 1
    
    # car2
    for idx2, value2 in car2.items():
        if idx1 == idx2: 
            merged_times[idx1] += 1

    # car2
    for idx2, value2 in car3.items():
        if idx1 == idx2: 
            merged_times[idx1] += 1
            
# A, B, C

count_1 = sum(value == 1 for value in merged_times.values())
count_2 = sum(value == 2 for value in merged_times.values())
count_3 = sum(value == 3 for value in merged_times.values())

res_A = 1 * A * count_1
res_B = 2 * B * count_2
res_C = 3 * C * count_3

print(res_A + res_B + res_C)
