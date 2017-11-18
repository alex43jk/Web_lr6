from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from webob import Request, Response
from jinja2 import Environment, FileSystemLoader

assets = [
  'app.js',
  'react.js',
  'leaflet.js',
  'D3.js',
  'moment.js',
  'math.js',
  'main.css',
  'bootstrap.css',
  'normalize.css',
]

STYLES = []
SCRIPTS = []

for item in assets:
  itemsplited = item.split('.')
  if itemsplited[1] == 'js':
    SCRIPTS.append(item)
  elif itemsplited[1] == 'css':
    STYLES.append(item)

class make_wsgi_app(object):
  def __init__(self, app):
    self.app = app

  def __call__(self, environ, start_response):
    response = self.app(environ, start_response).decode()

def app(request):
  response_code = '200 OK'
  response_type = ('Content-Type', 'text/HTML')
  start_response(response_code, [response_type])
  return ''''''

def index(request):
  env = Environment(loader=FileSystemLoader('.'))
  template = env.get_template('index.html').render(javascripts=SCRIPTS, styles=STYLES)
  return Response(template)

def about(request):
  env = Environment(loader=FileSystemLoader('.'))
  template = env.get_template('about/about.html').render(javascripts=SCRIPTS, styles=STYLES)
  return Response(template)

if __name__ == '__main__':
  config = Configurator()

  configure.add_route('index', '/index.html')
  config.add_view(index, route_name="index")

  # configure.add_route('about', '/about/about.html')
  # config.add_view(about, route_name="about")

  app = config.make_wsgi_app()
  make_server('0.0.0.0', 80, app).serve_forever()
