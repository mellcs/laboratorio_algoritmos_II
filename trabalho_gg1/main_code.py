import menu_module
import stock_module
import historic_module
import sales_module


def main():
    """ Os módulos são importados, listas e dicionários são abertos e funções são chamadas. """
    stock_data = {"caneta BIC": {"amount": 5, "price": 5.00, "price_historic": [7, 7.50], "category": "Material Escolar"}}
    sales_record = {}
    add_alter_record = []
    value_alter_record = []
    removal_record = []

    while True:
        option = menu_module.show_menu()

        if option == "1":
            stock_module.add_product(stock_data, add_alter_record)

        elif option == "2":
            stock_module.alter_price(stock_data, value_alter_record)
            
        elif option == "3":
            stock_module.remove_product(stock_data, removal_record)
            
        elif option == "4":
            historic_module.alter_report(add_alter_record, value_alter_record, removal_record)
            
        elif option == "5":
            stock_module.search_for_product(stock_data, sales_record) 

        elif option == "6":
            stock_module.search_product_by_category(stock_data)

        elif option == "7":
            stock_module.show_products(stock_data)
    
        elif option == "8":
            sales_module.sell_product(stock_data, sales_record)
        
        elif option == "9":
            historic_module.sales_report(sales_record)
          
        elif option == "10":
            print("Obrigada por usar nossos serviços!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

main()
