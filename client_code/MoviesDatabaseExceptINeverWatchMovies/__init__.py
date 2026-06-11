from ._anvil_designer import MoviesDatabaseExceptINeverWatchMoviesTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class MoviesDatabaseExceptINeverWatchMovies(MoviesDatabaseExceptINeverWatchMoviesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.
