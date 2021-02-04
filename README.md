## About
CNN/DMデータセットを`url_lists`の中のテキストファイルの内容によってtrain/val/testに割り振るやつ

## url_listの中何入れればいいのよ
[これ](https://github.com/abisee/cnn-dailymail)．pointer-generaterとかと同じ．

## Usage
```
python separate.py <cnn_stories_dir> <dm_stories_dir>
```
それぞれ`train`,`val`,`test`に振り分けられる

