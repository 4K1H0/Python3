# calc.pyプログラム
#
# メニューに従って処理を行うプログラム


# main()
def main():

    showmenu()
    while((int_command = getint()) != 9):
        if int_command == 1:
            datainput()
            break
        elif int_command == 2:
            display()
            break
        elif int_command == 3:
            correct()
            break
        elif int_command == 4:
            calc()
            break
        elif int_command == 5:
            search()
            break
        elif int_command == 6:
            sort()
            break
        else:
            print("メニューの番号で選んでください。\n")
        showmenu()
    return 0


# datainput()
def datainput():
    print("\n\n1 データの新規入力・追加\n")


# display()
def display():
    print("\n\n2 データの出力\n")


# correct()
def correct():
    print("\n\n3 データの修正\n")


# calc()
def calc():
    print("\n\n4 平均・分散・標準偏差の計算\n")


def search():
    print("\n\n5 計算\n")


# sort()
def sort():
    print("\n\n6 整列\n")


# showmenu()
def shownmenu():
    print("\n\n計算処理プログラム\n"):

