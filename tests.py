import pytest

books = [
    ['Понедельник начинается в субботу', 'Фантастика'],
    ['2001: Космическая одиссея', 'Фантастика'],
    ['Кладбище домашних животных', 'Ужасы'],
    ['Сияние', 'Ужасы'],
    ['Убийство в восточном экспрессе', 'Детективы'],
    ['Маугли', 'Мультфильмы'],
    ['Трое в лодке, не считая собаки', 'Комедии'],
    ['Приключения бравого солдата Швейка', 'Комедии']
]


class TestBooksCollector:

    def test_genres_are_same_as_in_init(self, collector):
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_genre_age_rating_are_same_as_in_init(self, collector):
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize('name, genre', books)
    def test_set_book_genre_to_added_book(self, name, genre, collector):
        collector.books_genre[name] = ''
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

    @pytest.mark.parametrize('name, genre', books)
    def test_get_book_genre_for_every_in_books(self, name, genre, collector):
        collector.books_genre[name] = genre
        assert collector.get_book_genre(name) == genre

    def test_get_books_with_specific_genre_comedy(self, collector):
        genre = 'Комедии'
        names = list()
        for i in range(len(books)):
            collector.books_genre[books[i][0]] = books[i][1]
            if books[i][1] == genre:
                names.append(books[i][0])
        assert collector.get_books_with_specific_genre(genre) == names

    def test_get_books_genre_return_collection(self, collector):
        for i in range(len(books)):
            collector.books_genre[books[i][0]] = books[i][1]
        assert len(collector.get_books_genre()) != 0

    def test_get_books_for_children(self, collector):
        books_for_kids = list()
        for i in range(len(books)):
            collector.books_genre[books[i][0]] = books[i][1]
            if books[i][1] not in collector.genre_age_rating:
                books_for_kids.append(books[i][0])
        assert collector.get_books_for_children() == books_for_kids

    @pytest.mark.parametrize('name', ['Понедельник начинается в субботу', 'Убийство в восточном экспрессе'])
    def test_add_book_in_favorites(self, name, collector):
        for i in range(len(books)):
            collector.books_genre[books[i][0]] = books[i][1]
        collector.add_book_in_favorites(name)
        assert collector.favorites[0] == name

    def test_delete_book_from_favorites(self, collector):
        deleted_book = '10 негритят'
        collector.favorites = ['Убийство в восточном экспрессе', '10 негритят', 'Смерть на Ниле']
        collector.delete_book_from_favorites(deleted_book)
        assert deleted_book not in collector.favorites

    def test_get_list_of_favorites_books(self, collector):
        collector.favorites = ['Убийство в восточном экспрессе', '10 негритят', 'Смерть на Ниле']
        assert collector.get_list_of_favorites_books() == ['Убийство в восточном экспрессе', '10 негритят',
                                                           'Смерть на Ниле']
