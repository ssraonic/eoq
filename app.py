from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample Questions (you can modify)
questions = [
    {
        "question": "What is AI?",
        "options": ["Artificial Intelligence", "Automatic Input", "Advanced Internet", "None"],
        "answer": "Artificial Intelligence"
    },
    {
        "question": "Python is a?",
        "options": ["Snake", "Programming Language", "Car", "Game"],
        "answer": "Programming Language"
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0
        for i, q in enumerate(questions):
            user_ans = request.form.get(f"q{i}")
            if user_ans == q['answer']:
                score += 1
        return redirect(url_for('result', score=score))
    return render_template('quiz.html', questions=questions)

@app.route('/result')
def result():
    score = request.args.get('score')
    return render_template('result.html', score=score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)
