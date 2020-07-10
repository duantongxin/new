line = ">"
while True:
    try:
        input_file = input("您要编辑文件的路径>>")
        file_ = open(input_file, "w+")
    except :
        print("请检查您的路径和权限！：-）")
        break
    new_input = input("您要[编辑]文件还是[读取]>>")
    try:
        if new_input == "编辑":
            while True :
                one_input = input(line)
                if one_input == "退出编辑":
                    break
                file_.writelines(one_input)
                file_.write("\r")
                file_.flush()
        elif new_input == "读取":
            for f_read in fell.readlines():
                print(f_read)
        else:
            pass
    except:
        print("请您检查您的文件名或您的方式！：-）")
        break
    try:
        two_input = input("您要退出么(y/n)>")
        if two_input == "y":
            break
        elif two_input == "n":
            pass
    except:
        print("只能输入(y/n)小写!：-）")
        file_.close()
        break
