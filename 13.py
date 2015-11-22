for bai in range(1,10):
    for shi in range(1,10):
        for ge in range(1,10):
            num1 = 100 * bai +10 * shi +ge
            num2 = 100 * ge + 10* shi + bai
            if num1 == num2:
                print num1
