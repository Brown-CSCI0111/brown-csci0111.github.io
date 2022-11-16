from dataclasses import dataclass

@dataclass
class Post:
    poster: str # the username
    content: str
    likes: list # of usernames

@dataclass
class User:
    username: str
    posts: list # of posts
    liked_posts: list # of posts

# initial data: 3 users and 2 posts
post1 = Post("dez", "gret new album", [])
post2 = Post("jing", "best coffee shop?", [])

user1 = User("rishi", [], [])
user2 = User("jing", [post2], [])
user3 = User("dez", [post1], [])

all_users = [user1, user2, user3]

# Some functions
def new_post(by_user: User, content: str):
    """create a new post by given user with given content"""
    np = Post(by_user.username, content, [])
    by_user.posts.append(np)

def edit_post(which_post: Post, new_content: str):
    """update the content of a post"""
    which_post.content = new_content

def like_post(by_user: User, which_post: Post):
    """register that the given user likes the given post"""
    # add the user's username to the list of likers in the post
    which_post.likes.append(by_user.username)
    # MEMORY POINT 3
    # add the post to the list of posts that the user likes
    by_user.liked_posts.append(which_post)

# MEMORY POINT 1

new_post(user3, "any study groups?")
edit_post(post1, "great new album")
like_post(user3, post2)

# MEMORY POINT 2

# ---------------------
def test_like_post():
    # SETUP SCENARIO
    testp = Post("kathi", "hi", [])
    testu = User("kathi", [testp], [])

    # RUN THE FUNCTION TO TEST
    like_post(testu, testp) # kathi is going to like her own post (weird)

    # ASSERTIONS TO CHECK RESULT
    assert "kathi" in testp.likes
    assert testp in testu.liked_posts
    
    # print something to show the tests are done
    print("like post tests finished")

# actually run the tests
test_like_post()