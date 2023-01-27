from django.shortcuts import render
from django.urls import reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def home_view(request):
    template_name = 'calculator/home.html'

    pages = {
        'Omlet': reverse('omlet'),
        'Pasta': reverse('pasta'),
        'Buter': reverse('buter')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def calc(request, dish=None):
    if dish is None:
        dish = request.GET.get('dish', 'buter')
    servings = request.GET.get('servings', 1)
    print(DATA[dish])
    recipe = { ingredient: round(amount*int(servings), 2) for ingredient, amount in DATA[dish].items() }
    context = {
        'recipe': recipe,
        'range': range(1, 11),
        'dish': dish
    }
    return render(request, 'calculator/index.html', context)
