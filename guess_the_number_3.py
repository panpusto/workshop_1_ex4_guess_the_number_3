from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def play_the_game():
    if request.method == "GET":
        return render_template('start.html')

    elif request.method == "POST":

        min_value = int(request.form.get('min_value'))
        max_value = int(request.form.get('max_value'))

        user_answer = request.form.get('user_answer')
        guess = int(request.form.get('guess', 500))

        if user_answer == "too big":
            max_value = guess
        if user_answer == "too small":
            min_value = guess
        elif user_answer == "you won":
            return render_template('win.html', guess=guess)

        guess = (max_value - min_value) // 2 + min_value

        return render_template(
            'game.html',
            min_value=min_value,
            max_value=max_value,
            guess=guess
        )


if __name__ == "__main__":
    app.run(debug=True)