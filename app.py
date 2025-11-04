import requests
import os # Render用にosをインポート
from flask import Flask, render_template, request

app = Flask(__name__)

# ✨ ステップ2でコピーしたGASの「ウェブアプリURL」を貼り付け ✨
SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzDe-Fkdqx0_B4WakNH9OJ8uNybeMADfakJkuBJX0S-m9fs8hMGoaO-AQc61Knbs59w/exec" 

@app.route('/', methods=['GET', 'POST'])
def wish_form():
    if request.method == 'POST':
        # フォームからデータを取得
        name = request.form['name']
        color = request.form['color']
        hometown = request.form['hometown']
        wish = request.form['wish']

        # Googleスプレッドシートへ送信するデータ（JSON形式）
        data = {
            "name": name,
            "color": color,
            "hometown": hometown,
            "wish": wish
        }
        
        try:
            # GASのWebアプリURLにJSONデータをPOST
            response = requests.post(SCRIPT_URL, json=data)
            response.raise_for_status() # エラーがあれば例外を発生
            
            print(f"✅ Google Sheetsに送信しました。レスポンス: {response.json()}")

        except Exception as e:
            print(f"⚠️ 送信エラー: {e}")
            # エラーが発生した場合でも、ユーザーには結果画面を表示
            # 本番環境ではエラーページにリダイレクトする方が親切です

        # 完了ページを表示
        return render_template('result.html', name=name, color=color, hometown=hometown, wish=wish)
    
    # GETリクエストの場合はフォームを表示
    return render_template('form.html')

if __name__ == '__main__':
    # Renderが使用するポートとホストを指定
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=True) # debug=Trueは開発中のみ推奨