from flask import Blueprint, render_template
from app.models.movie_model import MovieModel

movie_bp = Blueprint("movie_bp", __name__)


@movie_bp.route("/")
def index():
    movies = MovieModel.get_all_movies()
    total_count = MovieModel.get_movie_count()
    avg_duration = MovieModel.get_average_duration()

    return render_template(
        "index.html",
        movies=movies,
        total_count=total_count,
        avg_duration=avg_duration
    )
