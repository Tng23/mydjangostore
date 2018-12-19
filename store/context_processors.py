from .models import Category


##method to create links to each product category##
def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)
