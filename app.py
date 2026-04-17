from flask import Flask, render_template  # render_templateを追加

app = Flask(__name__)

@app.route("/")
def hello():
    # 記事のタイトルをリストで用意
    post_list = ["初めての投稿", "Flaskの勉強中", "CSSでデザインしてみた"]
    return render_template("index.html", title="マイ・プログラミング日記", posts=post_list)

if __name__ == "__main__":
    app.run(debug=True)