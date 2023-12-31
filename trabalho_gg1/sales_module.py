from datetime import datetime

def sell_product(stock_data, sales_record):
    """ Permite a venda de um produto, fazendo a verificação de quantidade previamente no estoque, o cálculo do total da compra, envia as informações da venda para um local separado e registra a data e a hora da mesma. Ela também mantém o usuário ciente da falta de produtos ou quantidade de produtos no estoque. """

    product_name = input("Insira o nome do produto desejado: ")
    product_name = product_name.capitalize()

    if product_name in stock_data:
        desired_amount = int(input("Insira a quantidade desejada do produto: "))
        product_info = stock_data[product_name]

        if product_info["amount"] >= desired_amount:
            product_info["amount"] -= desired_amount
            total_value = product_info["price"] * desired_amount
            print("Valor total da venda:", total_value)

            if product_name not in sales_record:
                sales_record[product_name] = [] 
            
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            
            sales_record[product_name].append(f"{formatted_datetime}: {desired_amount} unidades do produto {product_name} foram vendidas pelo valor de {total_value}")

        else:
            print("A quantidade de produto desejado não está disponível no momento.")
    else:
        print("Produto não disponível no estoque.")
