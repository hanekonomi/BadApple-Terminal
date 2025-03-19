# BadApple Terminal
Bad Apple!!の[影絵PV](https://www.nicovideo.jp/watch/sm8628149)をターミナルで再生するプログラムです。

## 動作環境
* Python3.x

確認にはPython3.13.0を使用しました。  
video2text.pyの実行にはopencv-pythonが必要です。  
また、videoandaudioplayer.pyの実行にはsimpleaudioが必要です。

## 使い方
### data.txtの生成
video2text.pyと同じフォルダに`badapple.mp4`を配置してください。
引数には生成したい画像の幅を入力してください。  
例：`python video2text.py (画像の幅)`

### ターミナルでの再生
videoplayer.pyと同じフォルダにdata.txtを配置してください。  
例：`python videoplayer.py`

### 音声付きでの再生
videoplayer.pyと同じフォルダに`data.txt`と`badapple.wav`を配置してください。  
例：`python videoandaudioplayer.py`

## あといろいろ
このプログラムの作成には[このリポジトリ](https://github.com/tem6/badapple/)の[README.md](https://github.com/tem6/badapple/blob/master/README.md)を参考にしました。  
次作るときは、もっとしっかり作りたいです。
