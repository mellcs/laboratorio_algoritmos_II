def add_product(stock_data, add_alter_record):
    """ Adiciona produtos ao estoque, possibilitando o cadastro do produto incluindo quantidade, preço unitário e categoria. A função checa a existência prévia do produto e atualiza a quantidade disponível no estoque, além de registrar os dados iniciais do produto."""

    product_name = input("Insira o nome do produto: ")
    product_name = product_name.capitalize()
    stock_amount = int(input("Insira a quantidade de estoque: "))
    unitary_price = float(input("Insira o preço unitário do produto: "))
    product_category = input("Insira a categoria do produto: ")
    product_category = product_category.capitalize()

    if product_name in stock_data:
        stock_data[product_name]["amount"] += stock_amount
    else:
        stock_data[product_name] = {
        "amount": stock_amount,
        "price": unitary_price,
        "category" : product_category
    }
        
    add_alter_record.append(f"{product_name} foi adicionado ao estoque. {stock_amount} unidades estão disponíveis, e cada unidade custa {unitary_price}. A categoria do produto é {product_category}.")
        
def search_for_product(stock_data, sales_record):
    """ Possibilita a pesquisa por um produto específico, exibindo em seguida toda a informação disponível previamente disponibilizada e o histórico de venda do produto em questão."""

    product_name = input("Insira o nome do produto desejado: ")
    product_name = product_name.capitalize()

    if product_name in stock_data:
        product_info = stock_data[product_name]
        print("Informações do produto:")
        print(f"Produto: {product_name}")
        print(f"Quantidade: {product_info['amount']}")
        print(f"Preço: ${product_info['price']:.2f}")
        print(f"Categoria: {product_info.get('category', 'Categoria não definida')}")
        
        if product_name in sales_record:
            print("\nHistórico de Vendas:")
            for sale in sales_record[product_name]:
                print(sale)
        else:
            print("\nNenhuma venda registrada para este produto.")
    else:
        print("Produto não disponível no estoque.")


def search_product_by_category(stock_data):
    """ Permite que o usuário procure por uma categoria específica e que veja todos os produtos inseridos nela, incluindo seus atributos. """

    category_search = input("Que categoria de produtos gostaria de ver? ").strip()

    found_products = []

    for product, details in stock_data.items():
        if 'category' in details and details['category'].lower() == category_search.lower():
            found_products.append((product, details['amount'], details['price']))

    if found_products:
        print(f"Produtos na categoria '{category_search}':")
        for product, amount, price in found_products:
            print(f"Produto: {product}")
            print(f"Quantidade: {amount}")
            print(f"Preço: ${price:.2f}\n")
    else:
        print(f"Nenhum produto encontrado na categoria '{category_search}'.")



def show_products(stock_data):
    """ Mostra todos os produtos disponíveis no estoque, incluindo seus atributos. """

    print("\tProdutos diponíveis em estoque:")
            
    for product, details in stock_data.items():
        print(f"Produto: {product}")
        print(f"Quantidade: {details['amount']}")
        print(f"Preço: ${details['price']:.2f}")
        print(f"Categoria: {details.get('category', 'Categoria não definida')}")

def alter_price(stock_data, value_alter_record):
   """ Permite que o usuário ajuste o preço de um produto, e registra as mudanças em um local separado. O preço novo é utilizado em novas vendas. """

    product_name = input("Insira o nome do produto: ")
    product_name = product_name.capitalize()


    if product_name in stock_data:
        new_price = float(input("Insira o novo preço do produto: "))

        old_price = stock_data[product_name]["price"]

        stock_data[product_name]["price"] = new_price

        value_alter_record.append(f"{product_name} teve o preço alterado de {old_price} para {new_price}.")
        print("Preço atualizado com sucesso!")

    else:
        print("Produto não disponível no estoque.")

def remove_product(stock_data, removal_product):
    """ Dá ao usuário a opção de remover um produto do estoque por completo, e registra as remoções em um local separado. """
    
    product_name = input("Insira o nome do produto que deseja deletar: ")
    product_name = product_name.capitalize()

    
    if product_name in stock_data:
        stock_data.pop(product_name)
        
        removal_product.append(f"{product_name} foi retirado do estoque.")
        print("Produto deletado com sucesso!")

    else:
        print("Produto não disponível no estoque.")
    
    print()
