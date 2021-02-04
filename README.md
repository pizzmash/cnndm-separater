## About
CNN/DMデータセットを`url_lists`の中のテキストファイルの内容によってtrain/val/testに割り振るやつ

## url_listの中何入れればいいのよ
[これ](https://github.com/abisee/cnn-dailymail)．pointer-generaterとかと同じ．

## Usage
```
git clone https://github.com/pizzmash/cnndm-separater
cd cnndm-separater
wget https://raw.githubusercontent.com/abisee/cnn-dailymail/master/url_lists/all_train.txt url_lists/all_train.txt
wget https://raw.githubusercontent.com/abisee/cnn-dailymail/master/url_lists/all_val.txt url_lists/all_val.txt
wget https://raw.githubusercontent.com/abisee/cnn-dailymail/master/url_lists/all_test.txt url_lists/all_test.txt
python separate.py <cnn_stories_dir> <dm_stories_dir>
```
それぞれ`train`,`val`,`test`に振り分けられる

