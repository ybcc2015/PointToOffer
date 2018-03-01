# 1.找出数组中重复的数字
def duplicate(numbers, length):
    """
    一个长度为n的数组，里面的数字在0~n-1范围内，
    数组内可能有重复的数字，请找出任意一个重复的数字
    例： 输入[2,3,1,0,2,5,3] 输出2或3或-1（-1代表无重复数字或数组无效）
    :param numbers: 整型数组
    :param length: 数组长度
    :return:重复的数字或-1
    """
    if length <= 1:
        return -1

    for number in numbers:
        if number < 0 or number > length-1:
            return -1

    for i in range(length):
        while numbers[i] != i:
            if numbers[i] != numbers[numbers[i]]:
                temp = numbers[i]
                numbers[i] = numbers[temp]
                numbers[temp] = temp
            else:
                return numbers[i]
    return -1


# 2.不修改数组找出重复数字
def get_duplicate(numbers, length):
    """
    在一个长度为n的数组里，所有数字在1~n-1范围内，所以至少有一个数字是重复的
    请找出任意一个重复的数字，但不能修改数组
    例：输入[2,3,5,4,3,2,6,7], 输出2或者3，-1代表数组无效
    :param numbers: 数组
    :param length: 数组长度
    :return:
    """
    if length <= 1:
        return -1

    for number in numbers:
        if number < 1 or number > length-1:
            return -1

    start = 1
    end = length - 1
    while end >= start:
        mid = (start+end)//2
        count = count_range(numbers, length, start, mid)

        if end == start:
            if count > 1:
                return start

        if count > mid-start+1:
            end = mid
        else:
            start = mid+1
    # return -1


def count_range(numbers, length, start, end):
    """
    计算数组中属于范围[start,end]内的数字的个数
    :param numbers: 数组
    :param length: 数组大小
    :param start: 起始范围
    :param end: 终止范围
    :return:
    """
    count = 0
    for number in numbers:
        if start <= number <= end:
            count += 1
    return count


# 3.二维数组中查找数字
def find(matrix, rows, cols, number):
    """
    在一个二维整型数组中，每一行按照从左至右递增的顺序排序，每一列按照从上至下递增的顺序排序，
    判断该数组中是否含有要查找的整数
    :param matrix: 二维数组
    :param rows: 数组的行数
    :param cols: 数组的列数
    :param number: 要查找的数字
    :return: True or False
    """
    found = False
    if rows > 0 and cols > 0:
        row = 0
        col = cols-1
        while row < rows and col >= 0:
            if matrix[row][col] > number:
                col -= 1
            elif matrix[row][col] < number:
                row += 1
            else:
                found = True
                break
    return found


# 4.找出数组中只出现一次的一个数字
def find_appear_once(numbers):
    """
    一个整型数组除了一个数字只出现一次外，其他数字都出现了两次，找出这个只出现一次的数字
    :param numbers: 整型数组
    :return: 数字
    """
    if len(numbers) < 1:
        return
    result = 0
    for num in numbers:
        result ^= num
    return result


# 5.找出数组中只出现一次的两个数字
def find_2_appear_once(numbers):
    """
    一个整型数组除了两个数字只出现一次外，其他数字都出现了两次，找出这2个只出现一次的数字
    :param numbers: 整型数组
    :return: 数字
    """
    if len(numbers) < 2:
        return

    result_oxr = 0
    for num in numbers:
        result_oxr ^= num
    index = find_bits_isone(result_oxr)

    res1 = res2 = 0
    for num in numbers:
        if (num >> index) & 1:
            res1 ^= num
        else:
            res2 ^= num

    return res1, res2


# 在num的二进制表示中找到最右边是1的位，并返回其位置
def find_bits_isone(num):
    index = 0
    while (num & 1) == 0 and index < 32:
        num >>= 1
        index += 1
    return index


# 4.找出数组中只出现一次的一个数字
def find_appear_once_1(numbers):
    """
    一个整型数组除了一个数字只出现一次外，其他数字都出现了3次，找出这个只出现一次的数字
    :param numbers: 整型数组
    :return: 数字
    """
    if len(numbers) < 1:
        return

    bit_sum = [0 for i in range(32)]
    for i in range(len(numbers)):
        bit_mark = 1
        for j in range(31, -1, -1):
            bit = numbers[i] & bit_mark
            if bit:
                bit_sum[j] += 1
            bit_mark <<= 1

    result = 0
    for i in range(32):
        result <<= 1
        result += bit_sum[i] % 3

    return result


# 5.调整数组顺序使奇数位于偶数前面
def reorder_odd_even(lst):
    if len(lst) == 0:
        return
    begin = 0
    end = len(lst) - 1
    while begin < end:
        while begin < end and (lst[begin] & 1) != 0:
            begin += 1
        while begin < end and (lst[end] & 1) == 0:
            end -= 1
        if begin < end:
            lst[begin], lst[end] = lst[end], lst[begin]
    return lst


# 6.连续子数组的最大和
def max_sum_of_subarray(lst):
    if len(lst) == 0:
        return
    cur_sum = 0
    max_sum = 0
    for n in lst:
        cur_sum += n
        if cur_sum < 0:
            cur_sum = 0
        if cur_sum > max_sum:
            max_sum = cur_sum
    return max_sum


# 7.递增数组中数值与下标相等的元素(每个元素都是唯一的)
def find_number_equal_index(lst):
    if len(lst) == 0:
        return -1
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == mid:
            return mid
        if lst[mid] > mid:
            right = mid - 1
        else:
            left = mid + 1
    return -1


# 8.输入一个递增的数组和一个数字s,在数组中查找两个数,使他们的和正好等于s.
#   返回这一对数字的下标.如果有多对数字,输出任意一对即可.
def find_indexs(lst, s):
    if len(lst) < 2:
        return
    left = 0
    right = len(lst) - 1
    while left < right:
        cur_sum = lst[left] + lst[right]
        if cur_sum == s:
            return left, right
        elif cur_sum > s:
            right -= 1
        else:
            left += 1


if __name__ == '__main__':
    nums = [3]
    print(find_indexs(nums, 3))

