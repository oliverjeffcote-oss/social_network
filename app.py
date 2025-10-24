from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.post_repository import PostRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/social_network.sql")

# Retrieve all artists
artist_repository = ArtistRepository(connection)
artists = artist_repository.all()

# List them out
for artist in artists:
    print(artist)

post_repository = PostRepository(connection)
posts = post_repository.all()

for post in posts:
    print(post)
