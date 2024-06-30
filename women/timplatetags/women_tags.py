from django import  template
import women.views as views
from women.models import Category

register = template.library()


@register.inclusion_tag('includs/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}

