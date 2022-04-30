from flask import render_template, redirect, url_for, session, flash, request, abort
from main.post import post
from main.post.forms import PostForm
from main.models import User, Post
from main import db
from decorators import login_required

@post.route('/new/post', methods = ['GET','POST'])
@login_required
def new_post():
    form = PostForm()
    user = User.query.get(session['id'])
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.body.data, author=user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been successfully created', 'success')
        return redirect(url_for('user.dashboard'))
    return render_template('new_post.html', form=form,  title = 'New Post')

@post.route('/edit/post/<int:id>', methods = ['GET','POST'])
@login_required
def edit_post(id):
    form = PostForm()
    user = User.query.get(session['id'])
    post = Post.query.get(id)
    # abort operation if a user attempts to edit another user's post
    if user != post.author:
        return abort(403)
    if request.method == 'GET':
        form.title.data = post.title
        form.body.data = post.body
    elif form.validate_on_submit():
        post.title = form.title.data 
        post.body = form.body.data 
        db.session.commit()
        flash('Edit Successful', 'success')
        return redirect(url_for('user.dashboard'))
    return render_template('new_post.html', form=form, title = 'Edit Post')

@post.route('/delete/post/<int:id>')
@login_required
def delete_post(id):
    post = Post.query.get(id)
    user = User.query.get(session['id'])
    # abort operation if a user attempts to edit another user's postif user != post.author:
    if user != post.author:
        return abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted', 'danger')
    return redirect(url_for('user.dashboard'))