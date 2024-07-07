# file_manipulator

## 概要

- アプリケーションプログラムがオペレーティングシステムとどのように相互作用するかを学習
- Linux ファイルシステムに格納されているデータにアクセスして操作するプログラムを構築

## 技術スタック

- Python
- macOS

## 作成したスクリプト

- guess_the_number_game.py
  - コマンドラインで起動し、input関数で渡した数字の範囲の内でランダムな数値を当てるゲーム
  - 起動方法
    - `python file_manipulator.py`
- file_manipulator.py
  - コマンドラインで起動し、ファイルの操作を行うプログラム
    - 以下のバリデーションを行う
      - コマンドごとの引数の数が正しいか
      - 引数で指定されたコマンドが正しいか
      - 引数で指定されたファイルが存在するか
      - replace-stringで指定したneedleがファイル内に存在するか
  - 起動方法
    - `python file_manipulator/file_manipulator.py {command} {コマンドごとに必要な引数}`
  - コマンドごとの処理と必要な引数
    - reverse
      - `reverse {inputpath} {outputpath}`
        - inputpathの内容を逆順にしてoutputpathにファイルを作成する
    - copy
      - `copy {inputpath} {outputpath}`
        - inputpathの内容をoutputpathに同一内容のファイルを作成する
    - duplicate-contents
      - `duplicate-contents {inputpath} {number}`
        - inputpathの内容をnumberの回数コピーして、inputpathに追記する
    - replace-string
      - `replace-string {inputpath} {needle} {newstring}`
        - inputpathの内容のneedleをnewstringに置換する
