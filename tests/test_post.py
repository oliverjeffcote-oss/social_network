from lib.post import Post

def test_post_constructs():

    post = Post(1, 'Between the Bars', 'Short and sweet.', 152, 1)

    assert post.id == 1
    assert post.title == 'Between the Bars'
    assert post.contents == 'Short and sweet.'
    assert post.views == 152
    assert post.account_id == 1

def test_post_equality():

    post1 = Post(1, 'Between the Bars', 'Short and sweet.', 152, 1)
    post2 = Post(1, 'Between the Bars', 'Short and sweet.', 152, 1)

    assert post1 == post2

def test_post_formatting():

    post = Post(1, 'Between the Bars', 'Short and sweet.', 152, 1)

    assert str(post) == "Post(1, Between the Bars, Short and sweet., 152, 1)"