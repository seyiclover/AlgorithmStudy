start = input()
mapp = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}

row = mapp[start[0]]
col = int(start[1])

end = []

# 수평으로 두 칸 이동
if row + 2 <= 8:
    if col + 1 <= 8:
        end.append(f'{row+2}{col+1}')
    if col - 1 >= 1:
        end.append(f'{row+2}{col-1}')
    
if row - 2 >= 1:
    if col + 1 <= 8:
        end.append(f'{row-2}{col+1}')
    if col - 1 >= 1:
        end.append(f'{row-2}{col-1}')

# 수직으로 두 칸 이동
if col + 2 <= 8:
    if row + 1 <= 8:
        end.append(f'{row+1}{col+2}')

    if row - 1 >= 1:
        end.append(f'{row-1}{col+2}')

if col - 2 >= 1:
    if row + 1 <= 8:
        end.append(f'{row+1}{col-2}')

    if row - 1 >= 1:
        end.append(f'{row-1}{col-2}')


print(len(end))
