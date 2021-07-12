l = [1,2,3,4,5,6,7,8,9]

target = 12
#output (5,7), (4,8), (9,3)

final_result = []
for i in l:
    print(i)
    result = target-i
    if result != i:
        if result in l:
            final_result.append((i, result))
            l.remove(result)


print(final_result)



