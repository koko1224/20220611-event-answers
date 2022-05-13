def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述

    # 先頭からのインデックスを保存する変数
    i = 0
    # 末端からのインデックスを保存する変数
    j = len(array) - 1

    while i < j:
        # iを固定してpivot未満の値を見つけたとき
        if array[j] < pivot:
            # array[i]とarray[j]の中身を入れ替え
            tmp = array[j]
            array[j] = array[i]
            array[i] = tmp
            # iを次のpivot以上の値のインデックスに更新
            while array[i] < pivot and i < j:
                i+=1
        j-=1

    # pivotが最も小さい時, i=0でループが終了
    # 配列の後ろは未ソートなので，iの値を1に更新
    i = i if i > 0 else 1

    # 小さかった部分と大きかった部分に分け再起処理
    return sort(array[:i]) + sort(array[i:])

    # ここまで記述

if __name__ == '__main__':
    main()