# Flash_management_system

# 概要
League of Legends（LoL）というゲームのフラッシュと呼ばれるプレイヤー毎に5分に一度だけ使える強力なスキルを管理するタイマープログラムです。
フラッシュは短距離を瞬間移動するスキルで敵のスキルを避ける、敵に近づく、敵から逃げる等々非常に多岐に渡る使用方法があります。
そのため敵プレイヤーがフラッシュを使用してから5分以内に仕掛けることで試合を優勢に進めることができます。
しかし、敵プレイヤー5人のフラッシュのクールタイムを把握していることは難しいため、このタイマープログラムでいつでもクールタイムを把握できるようにします。

# GIt URL
https://github.com/fujisawa-git/flash_management_system.git

# 使用方法
プログラムを起動するとフラッシュの画像が縦に5枚並んでいます。
それぞれのボタンをクリックするとタイマーが起動し、フラッシュのクールタイムである300秒のカウントをします。
間違えて押してしまった場合は真横のリセットボタンを押すと、それぞれ隣のタイマーと紐づいているためリセット可能です。
リセット後は再度フラッシュの画像のボタンを押すとカウントダウンすることができます。

# 課題解決
フラッシュの有無がわかるか否かでその後の行動が180°変わることもあるため、視覚的にフラッシュの有無をわかるようにする。

# 要件定義(上から優先順位高)
1.タイマーを5つ用意
2.タイマーリセット機能追加
3.タイマーボタンをフラッシュの画像に
4.タイマーボタンを押すと画像を白黒に変更
/*ここまで実装完了*/
5.フラッシュ以外のスキルのためにタイマーを5つ追加

# 実装予定機能
・フラッシュ以外にも10種類ほどスキルがあり、フラッシュを含めてその内2つを選択するため、そのスキルの管理もできるようにする。（フラッシュ選択率は90％以上、他のスキルはフラッシュほど管理の重要性が低い）
・timer.sleep()を使用していることもあり300秒ぴったりカウントができていないことの修正

# 使用中の画像
![Flash_management](https://github.com/fujisawa-git/flash_management_system/assets/145174935/f9ff9999-6e2c-4c30-afbd-043d7b295408)

# ローカルでの使用方法記述欄
./Flash_management_system/dist/を丸ごとコピーしFlash_manage.exeを起動すると使用できます。


https://fujisawa-git.github.io/flash_management_system/