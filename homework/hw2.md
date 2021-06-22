## [程式碼](https://github.com/sleepy9487/ai109b/blob/main/homework/hw2.py):

```
board = [-1] * 8  #board 8x8


def printboard(result): #隨機打印出□■□
    for v in result:
        length = len(result)
        print('□ '*v + '■ ' + '□ '* (length-v-1))
    print('\n')

def is_valid(board, row, col): #如果打印出來的■的行或列或斜邊有其他■ 就不印出來
    for r in range(row):
        if col == board[r] or abs(row - r) == abs(col - board[r]):
            return False
        continue
    return True

def eightQueen(board, row): #一列一列打印出來
    if row >= len(board):
        printboard(board)
        return True

    for col in range(len(board)): #已經出現過■就不打印出來換下行
        if is_valid(board, row, col):
            board[row] = col
            if eightQueen(board, row+1):
                pass
                #return True
    return False

eightQueen(board, 0)

```
>參考別人的程式加以註釋
## 結果
■ □ □ □ □ □ □ □   
□ □ □ □ ■ □ □ □   
□ □ □ □ □ □ □ ■  
□ □ □ □ □ ■ □ □  
□ □ ■ □ □ □ □ □  
□ □ □ □ □ □ ■ □  
□ ■ □ □ □ □ □ □  
□ □ □ ■ □ □ □ □  


■ □ □ □ □ □ □ □  
□ □ □ □ □ ■ □ □  
□ □ □ □ □ □ □ ■  
□ □ ■ □ □ □ □ □  
□ □ □ □ □ □ ■ □  
□ □ □ ■ □ □ □ □  
□ ■ □ □ □ □ □ □  
□ □ □ □ ■ □ □ □  


■ □ □ □ □ □ □ □  
□ □ □ □ □ □ ■ □  
□ □ □ ■ □ □ □ □  
□ □ □ □ □ ■ □ □  
□ □ □ □ □ □ □ ■  
□ ■ □ □ □ □ □ □  
□ □ □ □ ■ □ □ □  
□ □ ■ □ □ □ □ □  


■ □ □ □ □ □ □ □  
□ □ □ □ □ □ ■ □  
□ □ □ □ ■ □ □ □  
□ □ □ □ □ □ □ ■  
□ ■ □ □ □ □ □ □  
□ □ □ ■ □ □ □ □  
□ □ □ □ □ ■ □ □  
□ □ ■ □ □ □ □ □  


□ ■ □ □ □ □ □ □  
□ □ □ ■ □ □ □ □  
□ □ □ □ □ ■ □ □  
□ □ □ □ □ □ □ ■  
□ □ ■ □ □ □ □ □  
■ □ □ □ □ □ □ □  
□ □ □ □ □ □ ■ □  
□ □ □ □ ■ □ □ □  


□ ■ □ □ □ □ □ □  
□ □ □ □ ■ □ □ □  
□ □ □ □ □ □ ■ □  
■ □ □ □ □ □ □ □  
□ □ ■ □ □ □ □ □  
□ □ □ □ □ □ □ ■  
□ □ □ □ □ ■ □ □  
□ □ □ ■ □ □ □ □  


□ ■ □ □ □ □ □ □  
□ □ □ □ ■ □ □ □  
□ □ □ □ □ □ ■ □  
□ □ □ ■ □ □ □ □  
■ □ □ □ □ □ □ □  
□ □ □ □ □ □ □ ■  
□ □ □ □ □ ■ □ □  
□ □ ■ □ □ □ □ □  


□ ■ □ □ □ □ □ □
□ □ □ □ □ ■ □ □
■ □ □ □ □ □ □ □
□ □ □ □ □ □ ■ □
□ □ □ ■ □ □ □ □
□ □ □ □ □ □ □ ■
□ □ ■ □ □ □ □ □
□ □ □ □ ■ □ □ □


