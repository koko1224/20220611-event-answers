def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述

    # 判定する部分の左側のインデックスを保持
    i = 0
    # 判定する部分の右側のインデックスを保持
    j = len(sorted_array) - 1

    # 値を発見する or すべて探索し終えるまで繰り返す
    while i <= j:
        center_index = (j + i) // 2
        center_num = sorted_array[center_index]

        # 値を見つけたとき，indexをreturnして終了
        if center_num == target_number:
            return center_index
        # ターゲットの方が大きい場合，中央から後半を探索
        elif center_num < target_number:
            i = center_index + 1
        # ターゲットの方が小さい場合，中央から前半を探索
        else:
            j = center_index - 1

    # ここまで記述
    
    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()