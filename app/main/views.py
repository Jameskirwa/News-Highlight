from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_top_headlines,get_everything
# from ..models import Sources

# Views
@main.route('/')
def index():

   '''
   View root page function that returns the index page and its data
   '''
   sources = get_sources()
   Everything = get_everything()
   print(sources)
   title = 'Top Highlights '
   return render_template('index.html', title = title, sources = sources, Everything = Everything)

@main.route('/sources/<sources>')
def Top_Headlines(sources):
   '''
   View headlines page function that returns the Top-headlines from source
   '''
   sources = get_sources()
   Top_headlines = get_top_headlines(source)
   print(Top_headlines)
  
   return render_template('Top_Headlines.html',sources = sources, Top_headlines = Top_headlines)