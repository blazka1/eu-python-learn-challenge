from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        valid_movies = filter(
            lambda movie: 'country' in movie and movie.get('rating_kinopoisk') and float(
                movie['rating_kinopoisk']) > 0 and len(movie['country'].split(',')) >= 2,
            list_of_movies
        )

        ratings = list(map(lambda movie: float(movie['rating_kinopoisk']), valid_movies))

        if ratings:
            return sum(ratings) / len(ratings)

        return 0.0

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        valid_movies = []

        for el in list_of_movies:
            if 'rating_kinopoisk' in el and el['rating_kinopoisk']:
                try:
                    rating_kinopoisk = float(el['rating_kinopoisk'])
                    if rating_kinopoisk >= rating:
                        valid_movies.append(el)
                except ValueError:
                    # Обрабатываем случай, когда преобразование не удаётся
                    continue

        return sum(name.count('и') for name in map(lambda x: x['name'], valid_movies))


