from lib.post import Post

class PostRepository:

    def __init__(self, connection):

        self._connection = connection

    def all(self):

        rows = self._connection.execute('SELECT * FROM posts')
        print(rows)
        posts = []
        for row in rows:
            item = Post(row['id'], row['title'], row['contents'], row['views'], row['account_id']) 
            posts.append(item)
        return posts



