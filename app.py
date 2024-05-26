from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Carregar o arquivo CSV
df = pd.read_csv('output.csv')

# Função para obter questões aleatórias
def get_random_questions(num_questions, subjects):
    filtered_df = df[df['Question'].str.contains('|'.join(subjects))]
    if num_questions > len(filtered_df):
        num_questions = len(filtered_df)
    questions = filtered_df.sample(n=num_questions)
    return questions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['POST'])
def quiz():
    num_questions = int(request.form['num_questions'])
    subjects = request.form.getlist('subjects')
    questions = get_random_questions(num_questions, subjects)
    return render_template('quiz.html', questions=questions.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
