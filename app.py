from flask import Flask, render_template

app = Flask(__name__)

# 記事データをリスト（辞書の集まり）として定義
POSTS = [
    {
        "id": 1,
        "title": "初めての投稿",
        "date": "2026-04-18",
        "content": "Flaskを使ってブログを開設しました！これから頑張ります。"
    },
    {
        "id": 2,
        "title": "Renderで公開成功",
        "date": "2026-04-19",
        "content": "ついに世界中に公開できました。URLを友達に教えようと思います。"
    },
    {
        "id": 3,
        "title": "Pythonのリストについて",
        "date": "2026-04-20",
        "content": "辞書を使うと、タイトル以外の情報も一緒に扱えるので便利ですね。"
    },
    {
        "id": 4,
        "title": "これからの目標",
        "date": "2026-04-21",
        "content": "次はデータベースを使って、もっと本格的なブログに挑戦したいです！"
    },
     {
        "id": 5,
        "title": "家族の紹介",
        "date": "2026-04-21",
        "content": "妻、娘、息子、孫3人です。"
    }
]

@app.route("/")
def hello():
    # 外部で定義したPOSTSをHTMLに渡す
    return render_template("index.html", title="マイ・プログラミング日記", posts=POSTS)
