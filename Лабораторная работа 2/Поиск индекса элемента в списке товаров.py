def func_find_item (list_of_items, item_of_interest):
    for index, item in enumerate (list_of_items):
        if item == item_of_interest:
            return index
#список товаров
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
for item in ['банан', 'груша', 'персик']:
    # функция для получения индекса товара
    index_item = func_find_item(items_list, item)
    if index_item is not None:
        print(f"Первое вхождение товара '{item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{item}' не найден в списке.")
