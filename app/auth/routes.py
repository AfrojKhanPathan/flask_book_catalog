from flask import render_template,request, flash, redirect, url_for
from app.auth.forms import RegistrationForm
from app.auth import authentication as at
from flask_login import login_required, logout_user

@at.route('/register', methods=['GET','POST'])
def register_user():
    name = None
    email = None
    form = RegistrationForm()
    if request.method == 'POST':
        name = form.name.data
        email = form.email.data

    return render_template('registration.html',form=form)

@at.route('/logout')
@login_required
def log_out_user():
    logout_user()
    return redirect(url_for('main.display_book'))

@at.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404