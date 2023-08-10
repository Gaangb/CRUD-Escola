# Esta aplicação serve para realizar cadastro de alunos em uma escola. A aplicação permite:
# 1- Adicionar um novo aluno ok
# 2- Ver os alunos que estudam na escola ok
# 3- Alterar os dados de algum aluno
# 4- Deletar um aluno

from flask import Flask
from flask import request
from flask import jsonify
import json

app = Flask(__name__)

alunos = [{
    'id': 0,
    'nome': 'aluno teste',
    'rg': 1122334455,
    'serie': 6,
    'turma': 'A'
}]


@app.route('/add_aluno', methods=['POST'])
def add_aluno():
    try:
        dados = json.loads(request.data)
        if dados['nome'] and dados['rg'] and dados['serie'] and dados['turma']:
            posicao = len(alunos)
            dados['id'] = posicao
            alunos.append(dados)
            return jsonify(alunos[posicao])
    except KeyError:
        return jsonify({'status': 'falha ao adicionar aluno',
                        'mensagem': 'Verifique os dados informados'})


@app.route('/')
def get_alunos():
    return jsonify(alunos)


@app.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_aluno_by_id(id):

    try:
        if request.method == 'GET':
            answer = alunos[id]
        elif request.method == 'PUT':
            answer = json.loads(request.data)
            alunos[id] = answer
        elif request.method == 'DELETE':
            alunos.pop(id)
            answer = {'status': 'sucesso', 'mensagem': 'Aluno exluido com sucesso'}
    except IndexError:
        answer = {'status': 'erro', 'mensagem': 'Aluno de id {} não existe'.format(id)}
    return jsonify(answer)


if __name__ == '__main__':
    app.run(debug=True)
