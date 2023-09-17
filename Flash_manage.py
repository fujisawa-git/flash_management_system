import tkinter
import threading
import time

start_flag = [False] * 5
reset_flag = [False] * 5
flash_time = [3] * 5
exit_flag = False

#タイマー
def timer(pos):
    global labels

    count = flash_time[pos]

    while not exit_flag:
        s_flag = start_flag[pos]
        r_flag = reset_flag[pos]
        if r_flag:
            count = flash_time[pos]
            labels.config(text = count)
            s_flag = False
            reset_flag[pos] = False
            start_flag[pos] = False
        if s_flag:
            count -= 1
            labels.config(text = count)
            if count <= 0:
                start_flag[pos] = False
                count = flash_time[pos]

            time.sleep(1)

#タイマー開始ボタンが押されたときのイベント
def s_button_clk(event, pos):
    global start_flag

    start_flag[pos] = True

#タイマーリセットボタンが押されたときのイベント
def r_button_clk(event, pos):
    global reset_flag

    reset_flag[pos] = True

#タイマーのループから出た後にアプリを終了する
def exit_root():
    global exit_flag
    global root 
    global thread_1
    global thread_2

    exit_flag = True

    thread_1.join()
    thread_2.join()

    root.destroy()

root = tkinter.Tk()
root.geometry("200x200")

#TOP用スタートボタン
s_button_1 = tkinter.Button(
    root,
    text = "Flash_TOP"
)
s_button_1.pack()

#TOP用時間表示ラベル
labels = tkinter.Label(
    root,
    text = 0,
)
labels.pack()

#JG用スタートボタン
s_button_2 = tkinter.Button(
    root,
    text = "Flash_JG"
)
s_button_2.pack()

#リセット用ボタン(現在TOPのみ利用可能)
r_button = tkinter.Button(
    root,
    text="reset",
)
r_button.pack()

#lambda関数でボタンクリック関数へ変数を渡せる
s_button_1.bind("<ButtonPress>", lambda event : s_button_clk(event, 0))
s_button_2.bind("<ButtonPress>", lambda event : s_button_clk(event, 1))
r_button.bind("<ButtonPress>", lambda event : r_button_clk(event, 0))
root.protocol("WM_DELETE_WINDOW", exit_root)

#並行してタイマーを使用するためスレッドをtimerに関して作る、ポジションがわかるように引数を渡す
thread_1 = threading.Thread(target=timer, args = (0,))
thread_2 = threading.Thread(target=timer, args = (1,))

#スレッド起動
thread_1.start()
thread_2.start()

#メインループ
root.mainloop()