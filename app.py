from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        color = request.form['color']
        hometown = request.form['hometown']
        wish = request.form['wish']

        print("==== フォームの送信を受け取りました ====")
        print(f"名前: {name}")
        print(f"灯籠の色: {color}")
        print(f"出身地: {hometown}")
        print(f"願いごと: {wish}")
        print("=========================================")

        return render_template('result.html', name=name, color=color, hometown=hometown, wish=wish)

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
