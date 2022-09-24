import copy

if __name__ == '__main__':
    print('a')

    # input data
    number_list = []
    for i in range(4):
        number_list.append(input("Number:"))
    print(number_list)

    # 1st step
    # select number
    # input : number_list
    # output : number_list_for_this_time
    number_list_wk1 = copy.deepcopy(number_list)
    number_list_for_this_time = []
    print(number_list_wk1[:1])
    print(number_list_wk1[1:])
    print(number_list_wk1[:1] + number_list_wk1[1:])
    for i, n in enumerate(number_list_wk1):
        number_list_for_this_time.append(n)
        number_list_wk2 = number_list_wk1[:i] + number_list_wk1[i:]
        for j, m in enumerate(number_list_wk2):
            number_list_for_this_time.append(m)
            number_list_wk3 = number_list_wk2[:j] + number_list_wk2[j:]
            for k, o in enumerate(number_list_wk3):
                number_list_for_this_time.append(o)
                number_list_wk4 = number_list_wk3[:k] + number_list_wk3[k:]
                for l, p in enumerate(number_list_wk4):
                    number_list_for_this_time.append(p)
                    #print(number_list_for_this_time)


    # 2nd step
    # select operator
    # input : operator list (empty)
    # output : operator list

    # 3rd step
    # calcurate numbers by operator
    # input : number_list_for_this_time, operator list
    # output : result

    # 4th step
    # print result
