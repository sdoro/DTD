
from django.http import HttpResponse
from django.template import Context, Template, loader

def detail(request):
  dict_values = {'fav_color': 'blue'}
  template_string = "My favorite color is {{ fav_color }}."
  c = Context(dict_values)
  t = loader.get_template('example.html')
  rendered_template = t.render(c)
  return HttpResponse(rendered_template)
