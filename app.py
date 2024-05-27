from flask import Flask, render_template, request
import pandas as pd
import random

app = Flask(__name__)

# Carregar o arquivo CSV
df = pd.read_csv('output.csv')

# Função para obter questões aleatórias ou sequenciais
def get_questions(num_questions, randomize):
    if randomize:
        questions = df.sample(n=num_questions)
    else:
        questions = df.head(num_questions)
    return questions.to_dict(orient='records')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['POST'])
def quiz():
    num_questions = int(request.form['num_questions'])
    randomize = request.form['random_questions'] == 'yes'
    questions = get_questions(num_questions, randomize)
    return render_template('quiz.html', questions=questions)

if __name__ == '__main__':
    app.run(debug=True)
