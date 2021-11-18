from django.shortcuts import render

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
}


def calculate_view(request, dish_name):
    quantity = int(request.GET.get('servings', '1'))
    context = {
        'recipe': {}
    }

    for ing, per in DATA[dish_name].items():
        context['recipe'][ing] = quantity * DATA[dish_name][ing]

    return render(request, 'calculator/index.html', context)
