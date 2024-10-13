from flask import (
    Flask, 
    render_template,
    redirect, 
    request,
    url_for
)


app = Flask(__name__)

alunos = [
    {'id': 1, 'nome': 'Jonas', 'idade': 28, 'curso': 'python', 'nota': 10},
    {'id': 2, 'nome': 'Lucas', 'idade': 25, 'curso': 'python', 'nota': 9},
]

def buscar_aluno_por_id(id: int):
    for aluno in alunos:
        if aluno['id'] == int(id):
            return aluno


@app.route('/')
def index():
    return 'Olá mundo!'


@app.route('/alunos')
def list_alunos():
    return render_template('alunos.html', alunos=alunos)


id_atual = 2


@app.route('/add-aluno', methods=['GET', 'POST'])
def add_aluno():
    global id_atual
    if request.method == 'POST':
        nome = request.form.get('nome')
        idade = request.form.get('idade')
        curso = request.form.get('curso')
        nota = request.form.get('nota')
        id_atual += 1
        aluno = {
            "id": id_atual,
            "nome": nome,
            "idade": idade,
            "curso": curso,
            "nota": nota
        }
        alunos.append(aluno)
        return redirect(url_for('list_alunos'))
    return render_template('add-aluno.html')


@app.route('/deletar-aluno/<id>')
def deletar_aluno(id: int):
    aluno = buscar_aluno_por_id(id)
    print(aluno, '--------------')
    alunos.remove(aluno)
    return redirect(url_for('list_alunos'))


@app.route('/atualizar-aluno/<id>', methods=['GET', 'POST'])
def update_aluno(id: int):
    aluno = buscar_aluno_por_id(id)
    if request.method == 'POST':
        aluno['nome'] = request.form.get('nome')
        aluno['idade'] = request.form.get('idade')
        aluno['curso'] = request.form.get('curso')
        aluno['nota'] = request.form.get('nota')
        return redirect(url_for('list_alunos'))
    return render_template('update-aluno.html', aluno=aluno)


if __name__ == '__main__':
    app.run(debug=True)