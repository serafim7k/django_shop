from django.shortcuts import render
from django.http import HttpResponse
from goods.models import Products

def catalog(request):
    
    goods = Products.objects.all()
    
    context = {
        'title': 'Home',
        'goods': goods,
    }
    return render(request, 'goods/catalog.html', context)

def product(request):
    # context = {
    #     'title': 'Home++',
    #     'content': 'Main shop page - Home++',
    #     'some_text_about': 'About lorem ipsum dolor.',
    # }
    return render(request, 'goods/product.html')


# [
#             {
#                 "image": "deps/images/goods/table_and_three_chairs.jpg",
#                 "name": "Чайный столик и три стула",
#                 "description": "Комплект из трёх стульев и дизайнерский столик для гостинной комнаты.",
#                 "price": 90.00,
#             },
#             {
#                 "image": "deps/images/goods/table_and_two_chairs.jpg",
#                 "name": "Чайный столик и два стула",
#                 "description": "Комплект из двух стульев и дизайнерский столик для гостинной комнаты.",
#                 "price": 90.00,
#             },
#             {
#                 "image": "deps/images/goods/double_bed.jpg",
#                 "name": "Двухспальная кровать",
#                 "description": "Кровать двухспальная с надголовником и вообще очень ортопедичная.",
#                 "price": 90.00,
#             },
#             {
#                 "image": "deps/images/goods/kitchen_table.jpg",
#                 "name": "Кухонный стол с раковиной",
#                 "description": "Кухонныйй стол для обеда с встроенной раковиной и стульями.",
#                 "price": 90.00,
#             },
#             {
#                 "image": "deps/images/goods/kitchen_table 2.jpg",
#                 "name": "Кухонный стол с встройкой",
#                 "description": "Кухонный стол со встроенной плитой и раковиной. Много полок и вообще красивый.",
#                 "price": 90.00,
#             },
#             {
#                 "image": "deps/images/goods/corner_sofa.jpg",
#                 "name": "Угловой диван для гостинной",
#                 "description": "Угловой диван, раскладывается в двухспальную кровать, для гостинной и приема гостей самое то!",
#                 "price": 90.00,
#             },
#             {
#                 "image": "deps/images/goods/bedside_table.jpg",
#                 "name": "Прикроватный столик",
#                 "description": "Прикроватный столик с двумявыдвижными ящиками (цветок не входит в комплект).",
#                 "price": 90.00,
#             },
#             {
#                 "image": "deps/images/goods/sofa.jpg",
#                 "name": "Диван обыкновенный",
#                 "description": "Диван, он же софа обыкновенная, ничего примечательного для описания.",
#                 "price": 90.00,
#             },
#             {
#                 "image": "deps/images/goods/office_chair.jpg",
#                 "name": "Стул офисный",
#                 "description": "Описание товара, про то какой он классный, но это стул, что тут сказать...",
#                 "price": 90.00,
#             },
#             {
#                 "image": "deps/images/goods/plants.jpg",
#                 "name": "Растение",
#                 "description": "Растение для украшения вашего интерьера подарит свежесть и безмятежность обстановке.",
#                 "price": 90.00,
#             },
#             {
#                 "image": "deps/images/goods/flower.jpg",
#                 "name": "Цветок стилизированный",
#                 "description": "Дизайнерский цветок (возможно искусственный) для украшения интерьера.",
#                 "price": 90.00,
#             },
#             {
#                 "image": "deps/images/goods/strange_table.jpg",
#                 "name": "Прикроватный столик",
#                 "description": "Столик, довольно странный на вид, но подходит для размещения рядом с кроватью.",
#                 "price": 90.00,
#             },
#         ]