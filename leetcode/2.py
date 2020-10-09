def findDiagonalOrder(matrix):
    lst = []
    if len(matrix) == 0:
        return lst
    height = len(matrix)
    print(height)
    width = len(matrix[0])
    print(width)
    if height == 1:
        for i in range(width):
            lst.append(matrix[0][i])
        return lst
    elif width == 1:
        for i in range(width):
            lst.append(matrix[i][0])
        return lst

    lst.append(matrix[0][0])
    j, k = 0, 0
    status = -1
    # if prev is top-left side, current direction goes down
    while True:
        if status == -1:
            if k < len(matrix) - 1:
                # new pivot [j][k+1]
                k += 1
                # pivot
                pivot_k = k
                print(matrix[j][k])
                lst.append(matrix[j][k])
                # print operation
                while True:
                    j += 1
                    k -= 1
                    print(matrix[j][k])
                    lst.append(matrix[j][k])
                    if j == pivot_k:
                        break
            else:
                j += 1
                pivot_j = j
                print(matrix[j][k])
                lst.append(matrix[j][k])
                if j != len(matrix) - 1:
                    while True:
                        j += 1
                        k -= 1
                        print(matrix[j][k])
                        lst.append(matrix[j][k])
                        if k == pivot_j:
                            break
                else:
                    j = -1
            status = status * -1
        # goes up
        if status == 1:
            if j < len(matrix) - 1:
                # new pivot [j+1][k]
                j += 1
                # pivot
                pivot_j = j
                print(matrix[j][k])
                lst.append(matrix[j][k])
                # print operation
                while True:
                    j -= 1
                    k += 1
                    print(matrix[j][k])
                    lst.append(matrix[j][k])
                    if k == pivot_j:
                        break
            else:
                k += 1
                pivot_k = k
                print(matrix[j][k])
                lst.append(matrix[j][k])
                if k != len(matrix) - 1:
                    while True:
                        j -= 1
                        k += 1
                        print(matrix[j][k])
                        lst.append(matrix[j][k])
                        if j == pivot_k:
                            break
                else:
                    k = -1
            status = status * -1

        if j == -1 or k == -1:
            break
    return lst


list =[[2,3]]
#print(len(list))
print(findDiagonalOrder(list))

# incorrect first trial -- only apply for N x N matrix
###
# class Solution:
#     def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
#         lst = []
#         if len(matrix) == 0:
#             return lst
#         lst.append(matrix[0][0])
#         status = -1
#         for i in range(1, len(matrix)):
#             # if status == -1, operation goes down, otherswise goes up
#             if status == -1:
#                 j, k = 0, i
#                 while True:
#                     lst.append(matrix[j][k])
#                     j += 1
#                     k -= 1
#                     if j < 0 or k < 0:
#                         break
#             else:
#                 j, k = i, 0
#                 while True:
#                     lst.append(matrix[j][k])
#                     j -= 1
#                     k += 1
#                     if j < 0 or k < 0:
#                         break
#             status = -status
#         length = len(matrix) - 1
#         for i in range(1, length+1):
#             if status == -1:
#                 j, k = i, length
#                 while True:
#                     lst.append(matrix[j][k])
#                     j += 1
#                     k -= 1
#                     #print(j, k)
#                     if j > length or k > length:
#                         break
#             else:
#                 j, k = length, i
#                 while True:
#                     lst.append(matrix[j][k])
#                     j -= 1
#                     k += 1
#                     if j > length or k > length:
#                         break
#             status = -status
#         return lst
