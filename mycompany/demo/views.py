
from django.http import HttpResponse
from django.template import Context, Template, loader

def detail(request):
  template_string = "My favorite color is {{ fav_color }}."
  c = Context({ 'fav_color': ['blue','green'] })
  t = loader.get_template('example.html')
  rendered_template = t.render(c)
  return HttpResponse(rendered_template)
