from apps.home import blueprint
from flask import render_template, request, url_for, redirect
from flask_login import login_required
from jinja2 import TemplateNotFound
from apps.authentication.models import Admin, User, Keluar, Masuk 
from apps.authentication.forms import UpdateUserAccount, UpdateAdminAccount
from apps import db

@blueprint.route('/index')
# @login_required
def index():
    
    return render_template('home/index.html', segment='index')


@blueprint.route('/<template>')
# @login_required
def route_template(template):
    
    admin = Admin.query.all()
    user = User.query.all()
    keluar = Keluar.query.all()
    masuk = Masuk.query.all()

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment, admin=admin, user=user, keluar=keluar, masuk=masuk)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None


#update

@blueprint.route('/user/<int:id>/update', methods = ['GET', 'POST'])
# @login_required
def updateuser(id):
    user = User.query.get_or_404(id)
    form = UpdateUserAccount()
    if form.validate_on_submit():
        user.username = form.username.data
        user.no_identitas = form.no_identitas.data
        user.nama = form.nama.data
        user.gender = form.gender.data
        user.status = form.status.data
        user.no_hp = form.no_hp.data
        user.email = form.email.data
        user.alamat = form.alamat.data
        user.no_plat = form.no_plat.data
        user.tanggal_masuk = form.tanggal_masuk.data
        user.password = form.password.data
        
        db.session.commit()
        return render_template('accounts/updateuser.html',
                               msg='User updated successfully <br> <a href="/user.html">User Page</a>',
                               success=True, id=user.id)
    form.username.data = user.username
    form.no_identitas.data = user.no_identitas
    form.nama.data = user.nama
    form.gender.data = user.gender
    form.status.data = user.status
    form.no_hp.data = user.no_hp
    form.email.data = user.email
    form.alamat.data = user.alamat
    form.no_plat.data = user.no_plat
    form.tanggal_masuk.data = user.tanggal_masuk
    form.password.data = user.password
    return render_template('accounts/updateuser.html', form=form)

@blueprint.route('/admin/<int:id>/update', methods = ['GET', 'POST'])
# @login_required
def updateadmin(id):
    admin = Admin.query.get_or_404(id)
    form = UpdateAdminAccount()
    if form.validate_on_submit():
        admin.username = form.username.data
        admin.no_identitas = form.no_identitas.data
        admin.nama = form.nama.data
        admin.gender = form.gender.data
        admin.no_hp = form.no_hp.data
        admin.email = form.email.data
        admin.tanggal_lahir = form.tanggal_lahir.data
        admin.alamat = form.alamat.data
        admin.tanggal_masuk = form.tanggal_masuk.data
        admin.password = form.password.data
        
        db.session.commit()
        return render_template('accounts/updateadmin.html',
                               msg='Admin updated successfully <br> <a href="/admin.html">Admin Page</a>',
                               success=True, id=admin.id)
    form.username.data = admin.username
    form.no_identitas.data = admin.no_identitas
    form.nama.data = admin.nama
    form.gender.data = admin.gender
    form.no_hp.data = admin.no_hp
    form.email.data = admin.email
    form.tanggal_lahir.data = admin.tanggal_lahir
    form.alamat.data = admin.alamat
    form.tanggal_masuk.data = admin.tanggal_masuk
    form.password.data = admin.password
    return render_template('accounts/updateadmin.html', form=form)
 
        
#delete
@blueprint.route('/deleteadmin/<int:id>')
def deleteadmin(id):
    admin = Admin.query.get_or_404(id)
    
    try:
        db.session.delete(admin)
        db.session.commit()
        return redirect(url_for('home_blueprint.index'))
    except:
        return redirect(url_for('home_blueprint.index'))
    
@blueprint.route('/deleteuser/<int:id>')
def deleteuser(id):
    user = User.query.get_or_404(id)
    
    try:
        db.session.delete(user)
        db.session.commit()
        return render_template('home/user.html')
    except:
        return redirect(url_for('home_blueprint.index'))
    
@blueprint.route('/deletekeluar/<int:id>')
def deletekeluar(id):
    keluar = Keluar.query.get_or_404(id)
    
    try:
        db.session.delete(keluar)
        db.session.commit()
        return render_template('home/keluar.html')
    except:
        return redirect(url_for('home_blueprint.index'))
    
@blueprint.route('/deletemasuk/<int:id>')
def deletemasuk(id):
    masuk = Masuk.query.get_or_404(id)
    
    try:
        db.session.delete(masuk)
        db.session.commit()
        return render_template('home/masuk.html')
    except:
        return redirect(url_for('home_blueprint.index'))
    