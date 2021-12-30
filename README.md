# 小学生の計算力コンテスト

塾の宿題に計算力コンテストがあります。
計算力コンテストの設計は一回のテストに50問があり、一番目から何番目まで全正解できるのをテストする目的です。
１から正解を続けることが重要だと考えられていますから一問でも正解できないとテストは終了します。
ただ、紙資料でのテストはこのようなテストに不向きなのでweb式の計算力コンテストにしてみました。


紙資料に定義された計算力のレベル：

- 50問全正解、計算力は仙人級
- 40〜49、計算力は達人級
- 30〜39、計算力は人並み以上
- 20〜29、計算力は普通
- 10〜19、計算力はやや不足気味
- 9以下、計算力は不足気味


## テスト内容

./data下のLaTeXファイルはテスト問題、txtファイルは解答です。

例:

```
./data
   |- math4-32.latex        # "4-32"はSapix塾資料の番号、四年生第32回のテスト
   |- math4-32-answer.txt   # 解答
```

## 答えのフォーマット

回答のInputにLaTeXは使わないので以下の特別フォーマットは必要：

- 分数は「/」を使う, 例："1/3"、クォーテーションマークは不要
- 帯分数は整数と分数の間一つ空白を入れる、例：7/3の帯分数は"2 1/3"
- 一回答に複数部分がある場合、各部分の間「,」を入れる、例："12,33"


## インストールと実行

### 必要なpython libのインストール

[streamlit](https://github.com/streamlit/streamlit)を使って簡単にこのweb式のコンテストを作りました。

pipでstreamlitをインストールする例：

```
$ pip install -r requirements.txt
```

### 実行

```
$ streamlit run streamlit_math.py
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  ...

```

### 補足

./data下のテスト問題はSapixの紙資料からの問題集なのでCopyrightの問題はあったらご連絡ください。
コードはフリーです。
