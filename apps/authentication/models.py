from flask_login import UserMixin

from apps import db, login_manager

from apps.authentication.util import hash_pass

class Admin(db.Model, UserMixin):

    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    no_identitas = db.Column(db.String(15), unique=True)
    nama = db.Column(db.String(100))
    gender = db.Column(db.String(1))
    no_hp = db.Column(db.String(14))
    email = db.Column(db.String(64), unique=True)
    tanggal_lahir = db.Column(db.Date)
    alamat = db.Column(db.String(100))
    tanggal_masuk = db.Column(db.Date)
    password = db.Column(db.String(60))

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == 'password':
                value = hash_pass(value)  # we need bytes here (not plain str)

            setattr(self, property, value)

    def __repr__(self):
        return str(self.username)


@login_manager.user_loader
def user_loader(id):
    return Admin.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = Admin.query.filter_by(username=username).first()
    return user if user else None

class User(db.Model, UserMixin):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True)
    no_identitas = db.Column(db.String(15), unique=True)
    nama = db.Column(db.String(100))
    gender = db.Column(db.String(1))
    status = db.Column(db.String(20))
    no_hp = db.Column(db.String(14))
    email = db.Column(db.String(64), unique=True)
    alamat = db.Column(db.String(100))
    no_plat = db.Column(db.String(10))
    # stnk = db.Column(db.String(20))
    tanggal_masuk = db.Column(db.Date)
    password = db.Column(db.String(60))

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == 'password':
                value = hash_pass(value)  # we need bytes here (not plain str)

            setattr(self, property, value)

    def __repr__(self):
        return str(self.username)


@login_manager.user_loader
def user_loader(id):
    return User.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = User.query.filter_by(username=username).first()
    return user if user else None


class Keluar(db.Model, UserMixin):

    __tablename__ = 'data_keluar'

    id = db.Column(db.Integer, primary_key=True)
    no_identitas = db.Column(db.String(15))
    nama = db.Column(db.String(100))
    status = db.Column(db.String(20))
    no_hp = db.Column(db.String(14))
    alamat = db.Column(db.String(100))
    no_plat = db.Column(db.String(10))
    waktu_keluar = db.Column(db.Date)
    
    
class Masuk(db.Model, UserMixin):

    __tablename__ = 'data_masuk'

    id = db.Column(db.Integer, primary_key=True)
    no_identitas = db.Column(db.String(15))
    nama = db.Column(db.String(100))
    status = db.Column(db.String(20))
    no_hp = db.Column(db.String(14))
    alamat = db.Column(db.String(100))
    no_plat = db.Column(db.String(10))
    waktu_masuk = db.Column(db.Date)
