from flask import Flask, render_template  # render_templateを追加

app = Flask(__name__)

@app.route("/")
def hello():
    # 複数の情報をセットにした「辞書」のリストを作成
    post_list = [
        {
            "title": "初めての投稿",
            "date": "2026-04-18",
            "content": "Flaskを使ってブログを開設しました！これから頑張ります。"
        },
        {
            "title": "Renderで公開成功",
            "date": "2026-04-19",
            "content": "ついに世界中に公開できました。URLを友達に教えようと思います。"
        },
        {
            "title": "Pythonのリストについて",
            "date": "2026-04-20",
            "content": "辞書を使うと、タイトル以外の情報も一緒に扱えるので便利ですね。"
        }
    ]
    return render_template("index.html", title="マイ・プログラミング日記", posts=post_list)
    
if __name__ == "__main__":
    app.run(debug=True)