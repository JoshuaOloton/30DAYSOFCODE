from flask import render_template, redirect, url_for, session, flash, request
from main.post import post
from main.post.forms import NewPostForm
from main.models import User, Post
from main import db
from decorators import login_required

@post.route('/new/post', methods = ['GET','POST'])
@login_required
def new_post():
    form = NewPostForm()
    user = User.query.get(session['id'])
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.body.data, author=user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been successfully created', 'success')
        return redirect(url_for('user.dashboard'))
    return render_template('new_post.html', form=form)