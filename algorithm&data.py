# 1.求1+2+...+n的和
def add_to_n(n):
    return 0 if n <= 0 else n + add_to_n(n-1)


# 2.求斐波那契数列的第n项
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        pre1 = 1
        pre2 = 0
        result = 0
        for i in range(2, n+1):
            result = pre1 + pre2
            pre2 = pre1
            pre1 = result
        return result


# 3.快速排序
def quick_sort(lst, begin, end):
    if begin < end:
        index = partition(lst, begin, end)
        quick_sort(lst, begin, index-1)
        quick_sort(lst, index+1, end)
    return lst


def partition(lst, begin, end):
    pivot = lst[begin]
    left = begin+1
    right = end
    while left <= right:
        while left <= right and lst[left] <= pivot:
            left += 1
        while left <= right and lst[right] > pivot:
            right -= 1
        if left <= right:
            lst[left], lst[right] = lst[right], lst[left]
    lst[begin], lst[right] = lst[right], lst[begin]
    return right


# 快排黑魔法
def qs(lst):
    if len(lst) <= 1:
        return lst
    return qs([i for i in lst[1:] if i <= lst[0]]) + [lst[0]] + \
        qs([i for i in lst[1:] if i > lst[0]])


# 4.旋转数组的最小数字
def get_min(numbers):
    """
    输入一个升序数组的一个旋转，输出旋转数组的最小数字
    例：输入[3,4,5,1,2], 输出1
    :param numbers: 整型数组
    :return: 最小数字
    """
    if len(numbers) < 1:
        return
    begin = 0
    end = len(numbers) - 1
    index = begin
    while numbers[begin] >= numbers[end]:
        if end - begin == 1:
            index = end
            break
        mid = (begin+end) // 2

        if numbers[mid] == numbers[begin] and numbers[mid] == numbers[end]:
            return in_order(numbers, begin, end)

        if numbers[mid] >= numbers[begin]:
            begin = mid
        if numbers[mid] <= numbers[end]:
            end = mid
    return numbers[index]


def in_order(numbers, begin, end):
    result = numbers[begin]
    for number in numbers[1: end+1]:
        if result > number:
            result = number
    return result


# 5.二进制中1的个数
def count_of_1(n):
    count = 0
    while n:
        n = (n-1) & n
        count += 1
    return count


# 6.数值的整数次方
def power(base, exponent):
    if base == 0 and exponent < 0:
        raise Exception('Invalid input.')
    if base == 0:
        return 0

    abs_exponent = exponent
    if exponent < 0:
        abs_exponent = -exponent

    result = 1
    for i in range(1, abs_exponent+1):
        result *= base

    return result if exponent >= 0 else 1/result


# 7.字符串的全排列
def f(s):
    result = []
    if len(s) == 0 or len(s) == 1:
        return result.append(s)
    elif len(s) == 2:
        return [s, s[1]+s[0]]
    else:
        for i in range(len(s)):
            c = s[i]
            rest = s[:i] + s[i+1:]
            result.extend([c + substr for substr in f(rest)])
    return result


# 8. 1~n整数中1出现的次数
def numbers_of_1(n):
    numbers = 0
    for i in range(1, n+1):
        while i:
            if i % 10 == 1:
                numbers += 1
            i //= 10
    return numbers


# 9.数字序列中某一位的数字
def digit_at_index(index):
    if index < 0:
        return -1
    left = 0
    right = 9
    wei = 1  # 数字位数
    while True:
        n = (right - left + 1) * wei
        if index < n:
            break
        else:
            left = right + 1
            right = right * 10 + 9
            wei += 1
            index -= n
    i = index // wei
    j = index % wei
    digit = str(left+i)[j]
    return digit


# 10.从字符串中找出一个最长不含重复字符的子字符串,返回该最长子字符串的长度
def longest_substr_without_duplication(string):
    cur_len = 0
    max_len = 0
    d = {}
    for i in range(len(string)):
        if d.get(string[i]) is None or i - d.get(string[i]) > cur_len:
            cur_len += 1
        else:
            if cur_len > max_len:
                max_len = cur_len
            cur_len = i - d.get(string[i])
        d[string[i]] = i
    if cur_len > max_len:
        max_len = cur_len
    return max_len


# if __name__ == '__main__':
#     print(longest_substr_without_duplication('aaaaaa'))

