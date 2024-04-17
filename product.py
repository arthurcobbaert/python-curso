from data import products
import pandas as pd 


def get_product_by_id(id):
    result = []
    for element in products:
        if element['id'] == id:
            result.append(element)
            return pd.DataFrame(result)


def update_product_by_id(id,data):
    name = data['name']
    price = data['price']
    quantidade = data['quantidade']

    product = {
        'id': id,
        'name': name,
        'price': price,
        'quantidade': quantidade
    }


    for index, element in enumerate(products):
        if element['id'] == id:
            products[index] = product
            return 'Produto alterado com sucesso.'

            




def get_all_product():
    result = []
    for element in products:
        result.append({'name': element['name'], 'price': element['price'] })
    return pd.DataFrame(result)



def create(Newproduct):
    Newid = products[-1]['id'] + 1
    name = Newproduct['name']
    price = Newproduct['price']
    quantidade = Newproduct['quantidade']
    new_price = price
    if not name or not price or not quantidade:
        return 'Os campos estao vazios'
    if type(price) == int:
        new_price = float(price)
    if type(new_price) != float:
        return 'O valor inserido nao eh um numero' 
    if type(quantidade) != int:
        return 'A quantidade inserida nao eh um inteiro'  
    if type(name) != str:
        return 'O nome inserido nao eh um texto'
    
    for element in products:
        if element['name'] == name:
            return 'O produto ja esta cadastrado'

   
    data = {
        'id': Newid,
        'name': name,
        'price': price,
        'quantidade': quantidade,
    }
    products.append(data)
    
    return 'Criado com sucesso!'






print(create({
        "name": 'BodyBoard Genesis 2',
        "price": 1230,
        "quantidade": 4,
    }))  





print(update_product_by_id(3,{
        "name": 'BodyBoard Genesis 2W',
        "price": 1230,
        "quantidade": 7
}))
print(get_all_product())
print(get_product_by_id(8))    