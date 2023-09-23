import tkinter
import threading
import time

start_flag = [False] * 5
reset_flag = [False] * 5
flash_time = [300] * 5
exit_flag = False

#タイマー
def timer(pos):
    global labels

    count = flash_time[pos]

    while not exit_flag:
        if reset_flag[pos]:
            count = flash_time[pos]
            s_buttons[pos].config(text = "")
            reset_flag[pos] = False
            start_flag[pos] = False
            s_buttons[pos].configure(image=img)
        if start_flag[pos]:
            count -= 1
            s_buttons[pos].config(text = count)
            if count <= 0:
                start_flag[pos] = False
                count = flash_time[pos]
                s_buttons[pos].config(text = "")
                s_buttons[pos].configure(image=img)

            time.sleep(1)

#タイマー開始ボタンが押されたときのイベント
def s_button_clk(event, pos):
    global start_flag

    start_flag[pos] = True
    s_buttons[pos].configure(image=img_click)

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
    global thread_3
    global thread_4
    global thread_5

    exit_flag = True

    thread_1.join()
    thread_2.join()
    thread_3.join()
    thread_4.join()
    thread_5.join()

    root.destroy()

root = tkinter.Tk()
root.geometry("200x360")

img = tkinter.PhotoImage(file='./spell_image/flash.png')
img_click = tkinter.PhotoImage(file='./spell_image/flash_click.png')

#スタートボタンの設定
s_buttons = [tkinter.Button(root, image=img, font=('MS UI Gothic', 30, "bold"), fg='black', compound='center') for num in range(5)]
[s_buttons[i].grid(row=i, column=0) for i in range(len(s_buttons))]

#lambda関数でボタンクリック関数へ変数を渡せる
s_buttons[0].bind("<ButtonPress>", lambda event : s_button_clk(event, 0))
s_buttons[1].bind("<ButtonPress>", lambda event : s_button_clk(event, 1))
s_buttons[2].bind("<ButtonPress>", lambda event : s_button_clk(event, 2))
s_buttons[3].bind("<ButtonPress>", lambda event : s_button_clk(event, 3))
s_buttons[4].bind("<ButtonPress>", lambda event : s_button_clk(event, 4))

#リセットボタンの設定
r_buttons = [tkinter.Button(root, text="reset", font=('MS UI Gothic', 30, "normal"), fg='black', compound='center') for num in range(5)]
[r_buttons[i].grid(row=i, column=1) for i in range(len(r_buttons))]

r_buttons[0].bind("<ButtonPress>", lambda event : r_button_clk(event, 0))
r_buttons[1].bind("<ButtonPress>", lambda event : r_button_clk(event, 1))
r_buttons[2].bind("<ButtonPress>", lambda event : r_button_clk(event, 2))
r_buttons[3].bind("<ButtonPress>", lambda event : r_button_clk(event, 3))
r_buttons[4].bind("<ButtonPress>", lambda event : r_button_clk(event, 4))

root.protocol("WM_DELETE_WINDOW", exit_root)

#並行してタイマーを使用するためスレッドをtimerに関して作る、ポジションがわかるように引数を渡す
thread_1 = threading.Thread(target=timer, args = (0,))
thread_2 = threading.Thread(target=timer, args = (1,))
thread_3 = threading.Thread(target=timer, args = (2,))
thread_4 = threading.Thread(target=timer, args = (3,))
thread_5 = threading.Thread(target=timer, args = (4,))

#スレッド起動
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
thread_5.start()

#メインループ
root.mainloop()