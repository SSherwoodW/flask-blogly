"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash, session
from models import db, connect_db
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post
from sqlalchemy import text

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.debug=True
app.config['SECRET_KEY'] = 'secretive'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def red_users():
    """Redirect to list of all users in db."""
    return redirect('/users')

@app.route('/users')
def show_users():
    """Show list of all users in db."""
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/users', methods=['POST'])
def add_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>')
def show_user(user_id):
    """Show details on pet."""
    user = User.query.get_or_404(user_id)
    posts = Post.query.all()
    return render_template('details.html', user=user, posts=posts)

@app.route('/users/new')
def create_user():
    return render_template('adduser.html')

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('edit.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=['POST'])
def save_edit_user(user_id):

    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>/delete', methods=["POST"])
def users_destroy(user_id):
    """Handle form submission for deleting an existing user"""

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")

#######################################################################
#Posts

@app.route('/posts/<int:post_id>')
def show_post(post_id):
    """Show a specific post."""
    post = Post.query.get_or_404(post_id)
    return render_template('posts/show.html', post=post)

@app.route('/users/<int:user_id>/posts/new')
def show_post_form(user_id):
    """Show form to add a post for user."""
    user = User.query.get_or_404(user_id)
    return render_template('posts/new.html', user=user)

@app.route('/users/<int:user_id>/posts/new', methods=["POST"])
def add_post(user_id):
    """Show form to add a post for user."""
    user = User.query.get_or_404(user_id)
    new_post = Post(title = request.form['title'],
                    content = request.form['content'],
                    user = user)
    db.session.add(new_post)
    db.session.commit()
    flash(f"Added '{new_post.title}' to your page.")
    return redirect(f'/users/{user_id}')

@app.route('/posts/<int:post_id>/edit')
def edit_post(post_id):

    post = Post.query.get_or_404(post_id)
    return render_template('/posts/edit.html', post = post)

@app.route('/posts/<int:post_id>/edit', methods=["POST"])
def submit_edit(post_id):
    post = Post.query.get_or_404(post_id)
    post.title = request.form['title']
    post.content = request.form['content']

    db.session.add(post)
    db.session.commit()
    flash(f"Successfully edited {post.title}.")

    return redirect(f"/users/{post.user_id}")

@app.route('/posts/<int:post_id>/delete', methods=["POST"])
def delete_post(post_id):
    """Delete post."""

    post = Post.query.get_or_404(post_id)

    db.session.delete(post)
    db.session.commit()
    flash(f"Post '{post.title}' deleted.")

    return redirect(f'/users/{post.user_id}')








