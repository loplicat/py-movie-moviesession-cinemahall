from datetime import datetime
from typing import Optional

from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie=Movie.objects.get(id=movie_id),
        cinema_hall=CinemaHall.objects.create(id=cinema_hall_id)
    )


def get_movies_sessions(
        session_date: Optional[str] = None
) -> QuerySet[MovieSession]:
    movies_sessions = MovieSession.objects.all()

    if session_date:
        filter_date = datetime.strptime(session_date, "%Y-%m-%d")
        movies_sessions = MovieSession.objects.filter(
            show_time__date=filter_date
        )

    return movies_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[datetime] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> None:
    movies_session = MovieSession.objects.get(id=session_id)

    if show_time:
        movies_session.show_time = show_time

    if movie_id:
        movies_session.movie_id = movie_id

    if cinema_hall_id:
        movies_session.cinema_hall_id = cinema_hall_id

    movies_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
