import random


def sort(original, order_by="ASC"):
    if order_by == "ASC":
        pass
    for i in range(len(original)):
        min_index = i
        for j in range(i+1,len(original)):
            if original[min_index] > original[j]:
                min_index = j
        original[i], original[min_index] = original[min_index], original[i]
    print(original)


if __name__ == "__main__" :
    numbers = [elements for elements in range(300)]
    random.shuffle(numbers)
    print(numbers)
    sort(numbers)
