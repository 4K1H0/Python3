# calc.pyプログラム
#
# メニューに従って処理を行うプログラム


# main()
def main():

    showmenu()
    int_command = getint()
    while(int_command != 9):
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
def showmenu():
    print("\n\n計算処理プログラム\n")
    print("処理番号を入力してください。\n")
    print("1 データの新規入力・追加\n")
    print("2 データの出力\n")
    print("3 データの修正\n")
    print("4 平均・分散・標準偏差の計算\n")
    print("5 検索\n")
    print("6 整列\n")
    print(" \n")
    print("9 終了\n")


# getint()
def getint():
    int_n = input()
    try:
        int_n = int(int_n)
    except ValueError:
        print("例外処理: 数字以外が入力されました。\n")
        int_n = -1
    return int_n


# 実行
if __name__=="__main__":
    main()
