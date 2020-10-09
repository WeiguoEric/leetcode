def findDup(array):
    if len(array) == 0:
        return false
    for i in range(len(array)):
        while array[i] != i:
            if array[i] == array[array[i]]:
                print("True")
                print(array[array[i]], array)
                return array
            else:
                temp = array[array[i]]
                array[array[i]] = array[i]
                array[i] = temp

array = [3,1,2,0,2,5,3]
findDup(array)
