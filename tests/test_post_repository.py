from lib.post_repository import PostRepository
from lib.post import Post

def test_get_all_posts(db_connection):

    repository = PostRepository(db_connection)

    assert repository.all() == [
        Post(1, 'Between the Bars', 'Short and sweet.', 152, 1),
        Post(2, 'Waltz #2', 'Melancholy melody.', 98, 1),
        Post(3, 'Diamonds & Rust', 'A memory in music.', 201, 2),
        Post(4, 'Gracias a la Vida', 'A cover of hope.', 134, 2),
        Post(5, 'Alright', 'We gon be alright.', 542, 3),
        Post(6, 'HUMBLE.', 'Sit down.', 678, 3),
        Post(7, 'One More Time', 'Celebrate and dance.', 430, 4),
        Post(8, 'Instant Crush', 'Love in disguise.', 319, 4),
    ]
