# 1.替换字符串中的空格
def replace_blank(string):
    """
    替换空格
    例子： 输入 "we are happy"  输出"we%20are%20happy"
    :param string:字符串
    :return: 字符串
    """
    if string:
        original_length = len(string)
        num_of_blank = 0
        for c in string:
            if c == ' ':
                num_of_blank += 1
        new_length = original_length + num_of_blank * 2
        str_list = ['' for i in range(new_length)]
        index_original = original_length - 1
        index_new = new_length - 1
        while 0 <= index_original <= index_new:
            if string[index_original] == ' ':
                index_new -= 2
                str_list[index_new:index_new+3] = '%20'
            else:
                str_list[index_new] = string[index_original]
            index_new -= 1
            index_original -= 1
        return ''.join(str_list)


# 2.合并两个有序数组
def combine(a1, a2):
    """
    a1和a2都为有序数组（升序），将a2中所有的数有序的插入a1中
    :param a1: 有序数组
    :param a2: 有序数组
    :return: 合并后的有序数组a1
    """
    if a1 and a2:
        index_a1 = len(a1) - 1
        index_a2 = len(a2) - 1
        a1.extend([None for i in range(len(a2))])
        index_new = len(a1)-1
        while index_a1 >= 0 and index_a2 >= 0:
            if a1[index_a1] > a2[index_a2]:
                a1[index_new] = a1[index_a1]
                index_a1 -= 1
                index_new -= 1
            elif a1[index_a1] < a2[index_a2]:
                a1[index_new] = a2[index_a2]
                index_a2 -= 1
                index_new -= 1
            else:
                a1[index_new-1: index_new+1] = a1[index_a1], a2[index_a2]
                index_a1 -= 1
                index_a2 -= 1
                index_new -= 2
        if index_a1 < 0:
            a1[:index_new+1] = a2[:index_a2+1]


if __name__ == '__main__':
    arr1 = [1, 3, 4, 7, 9]
    arr2 = [1, 2, 5, 8, 9]
    combine(arr1, arr2)
    print(arr1)
