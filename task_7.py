def digit_root(num):
    root = 0
    if num <= 10 ** 7:
        for i in str(num):
            root += int(i)
        while len(str(root)) > 1:
            root = (int(str(root)[0]) + int(str(root)[1]))  
        return root
    else:
        return 