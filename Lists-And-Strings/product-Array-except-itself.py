numbers = [1,2,3,4]


def productArrayExceptSelf(numbers):

    product_so_far = 1
    prefix = []
    for leftNums in range(len(numbers)):
        prefix.append(product_so_far)
        product_so_far *= numbers[leftNums]
        print(product_so_far)
    for rightNums in reversed(range(len(numbers))):
        prefix[rightNums] *= product_so_far
        product_so_far *= numbers[rightNums]

    return prefix
       

productArrayExceptSelf(numbers)