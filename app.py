import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# ✨ ここにあなたのGASのURLを貼り付けてください ✨
SCRIPT_URL = "https://docs.google.com/spreadsheets/d/1CWRanrAKtjzicCa4I1qUWNdfs-GnL6z7vxHWA6PSK-s/edit?usp=sharing"

@app.route('/', methods=['GET', 'POST'])
def wish_form():
    if request.method == 'POST':
        name = request.form['name']
        color = request.form['color']
        hometown = request.form['hometown']
        wish = request.form['wish']

        # Googleスプレッドシートへ送信
        data = {
            "name": name,
            "color": color,
            "hometown": hometown,
            "wish": wish
        }
        try:
            requests.post(SCRIPT_URL, json=data)
            print("✅ Google Sheetsに送信しました！")
        except Exception as e:
            print("⚠️ 送信エラー:", e)

        return render_template('result.html', name=name, color=color, hometown=hometown, wish=wish)
    return render_template('form.html')

if __name__ == '__main__':
    app.run()
