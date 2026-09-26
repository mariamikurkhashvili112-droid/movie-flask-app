from pymongo import MongoClient
from config import MONGO_URI, DB_NAME, COLLECTION_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
movies_collection = db[COLLECTION_NAME]


class MovieModel:

    @staticmethod
    def get_all_movies():
        return list(movies_collection.find())

    @staticmethod
    def get_movie_count():
        return movies_collection.count_documents({})

    @staticmethod
    def get_average_duration():
        movies = MovieModel.get_all_movies()
        if not movies:
            return 0
        total_duration = sum(movie["duration"] for movie in movies)
        return round(total_duration / len(movies), 2)
