from flask import (
    Blueprint, render_template
)

from front.di.presentation.PresentationDi import provide_SearchViewModel

bp = Blueprint('search', __name__)


@bp.route('/')
def index():
    view_model = provide_SearchViewModel()
    players_ui = view_model.start()
    players_ui = list(players_ui)
    print(f"hey - {len(players_ui)}")
    return render_template('search/search.html', players=players_ui)
