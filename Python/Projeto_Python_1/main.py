from data import users
import pandas as pd
import re


# Verificando se o email está no formato correto
def isValidEmail(email):
    # regex padrão de email
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    # email for padrão correto
    if re.fullmatch(regex, email):
        return True
    # se não incorreto
    else:
        return False
 

# Declaração da função que buscar um usuário pelo ID
def get_by_id(id):
    # verificando se o id enviado é maior que o numero de usuários da base de dados
    if id > len(users):
        # se for maior, retorna mensagem de id inválido
        return f"O id digitado: {id} é inválido, digite outro."
    
    # Criando uma lista (array)
    result = []
    
    # percorrendo a base de dados(array users) 
    for element in users: 
        # se o elemento e seu id for igual ao parametro enviado(1-30)
        if element['id'] == id:
            # adiociono na lista o elemento encontrado
            result.append(element)
            # transformo para tabela
            return pd.DataFrame(result)


def get_all():
    # Criando uma lista
    new_users = []
    
    # Percorrendo a base de dados
    for element in users:
        # Adicioanando na lista, o novo dicionário com apenas name e email
        new_users.append({'name': element['name'], 'email': element['email']})
    
    # Transformando a lista em tabela    
    return pd.DataFrame(new_users)


def create(newUser):
    # Criando o novo ID
    id = users[-1]['id'] + 1
    
    # Criando os campos do usuário
    name = newUser['name'] # name do dado enviado
    email = newUser['email'] # email do dado enviado
    password = newUser['password'] # password do dado enviado
    
    # Verifica se os campos não estão vazios
    if len(name) == 0 or len(email) == 0 or len(password) == 0:
        return 'Campo vazio, confira os dados cadastrados.'
    
    # Verifica se o password tem ao menos 6 caracteres
    if len(password) < 6:
        return 'Digite um password com ao menos 6 caracteres.'
    
    verifyEmail = (isValidEmail(email))
    
    if not verifyEmail:
        return "Formato de email inválido, digite um email válido porfavor."
    
    # Percorre a base de dados
    for element in users:
        # se encontrar algum email já na base de dados
        if element['email'] == email:
            # retorna mensagem de email inválido
            return f'Email já cadastrado {email}, cadastre outro.'
        
    # novo usuario criado
    user = {
        'id': id,
        'name': name,
        'email': email,
        'password': password
    }
    
    # adicionando na base de dados o novo usuário
    users.append(user)
    # retorna mensagem de sucesso!
    return 'Criado com sucesso!'

def update_by_id(newData, id):
    for index, element in enumerate(users):
        if element['id'] == id:
            users[index] = {
                'id': id,
                'name': newData['name'],
                'email': newData['email'],
                'password': newData['password']
            }
             
    return 'Alterado com sucesso!'

 
def delete_by_id(id):
    for index, element in enumerate(users):
        if element['id'] == id:
            users.remove(users[index])
            return 'Removido com sucesso!'
            
        
# print(get_by_id(3))
print(create(
    {
        'name': 'Dela Cruz',
        'email': 'delacruz@email.com',
        'password': 'f123123l',
    }
))

print(update_by_id(
    {
        'name': 'Dela Cruz',
        'email': 'delacruz@email.com',
        'password': 'flamengo100%',
    },
    30
))

# print(delete_by_id(30))

# print(users)
print(get_all())




