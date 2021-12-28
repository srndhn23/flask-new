from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import Email, DataRequired

# login and registration


class LoginForm(FlaskForm):
    username = TextField('Username',
                         id='username_login',
                         validators=[DataRequired()])
    password = PasswordField('Password',
                             id='pwd_login',
                             validators=[DataRequired()])

class CreateAccountForm(FlaskForm):
    username = TextField('Username',
                         id='username_create',
                         validators=[DataRequired()])
    no_identitas = TextField('Nomor Identitas',
                         id='no_identitas_create',
                         validators=[DataRequired()])
    nama = TextField('Nama',
                         id='nama_create',
                         validators=[DataRequired()])
    gender = TextField('Jenis Kelamin',
                         id='gender_create',
                         validators=[DataRequired()])
    no_hp = TextField('Nomor HP',
                         id='no_hp_create',
                         validators=[DataRequired()])
    email = TextField('Email',
                      id='email_create',
                      validators=[DataRequired(), Email()])
    tanggal_lahir = TextField('Tanggal Lahir',
                         id='tanggal_lahir_create',
                         validators=[DataRequired()])
    alamat = TextField('Username',
                         id='alamat_create',
                         validators=[DataRequired()])
    tanggal_masuk = TextField('Username',
                         id='tanggal_masuk_create',
                         validators=[DataRequired()])
    password = PasswordField('Password',
                             id='pwd_create',
                             validators=[DataRequired()])

class CreateUserAccount(FlaskForm):
    username = TextField('Username',
                         id='username_create',
                         validators=[DataRequired()])
    no_identitas = TextField('Nomor Identitas',
                         id='no_identitas_create',
                         validators=[DataRequired()])
    nama = TextField('Nama',
                         id='nama_create',
                         validators=[DataRequired()])
    gender = TextField('Jenis Kelamin',
                         id='gender_create',
                         validators=[DataRequired()])
    status = TextField('Status',
                         id='status_create',
                         validators=[DataRequired()])
    no_hp = TextField('Nomor HP',
                         id='no_hp_create',
                         validators=[DataRequired()])
    email = TextField('Email',
                      id='email_create',
                      validators=[DataRequired(), Email()])
    alamat = TextField('Alamat',
                         id='alamat_create',
                         validators=[DataRequired()])
    no_plat = TextField('Nomor Plat',
                         id='no_plat_create',
                         validators=[DataRequired()])
    # stnk = TextField('STNK',
    #                      id='stnk_create',
    #                      validators=[DataRequired()])
    tanggal_masuk = TextField('Tanggal Masuk',
                         id='tanggal_masuk_create',
                         validators=[DataRequired()])
    password = PasswordField('Password',
                             id='pwd_create',
                             validators=[DataRequired()])
    

class UpdateUserAccount(FlaskForm):
    username = TextField('Username',
                         id='username_update',
                         validators=[DataRequired()])
    no_identitas = TextField('Nomor Identitas',
                         id='no_identitas_update',
                         validators=[DataRequired()])
    nama = TextField('Nama',
                         id='nama_update',
                         validators=[DataRequired()])
    gender = TextField('Jenis Kelamin',
                         id='gender_update',
                         validators=[DataRequired()])
    status = TextField('Status',
                         id='status_update',
                         validators=[DataRequired()])
    no_hp = TextField('Nomor HP',
                         id='no_hp_update',
                         validators=[DataRequired()])
    email = TextField('Email',
                      id='email_update',
                      validators=[DataRequired(), Email()])
    alamat = TextField('Alamat',
                         id='alamat_update',
                         validators=[DataRequired()])
    no_plat = TextField('Nomor Plat',
                         id='no_plat_update',
                         validators=[DataRequired()])
    # stnk = TextField('STNK',
    #                      id='stnk_update',
    #                      validators=[DataRequired()])
    tanggal_masuk = TextField('Tanggal Masuk',
                         id='tanggal_masuk_update',
                         validators=[DataRequired()])
    password = PasswordField('Password',
                             id='pwd_update',
                             validators=[DataRequired()])
    
class UpdateAdminAccount(FlaskForm):
    username = TextField('Username',
                         id='username_update',
                         validators=[DataRequired()])
    no_identitas = TextField('Nomor Identitas',
                         id='no_identitas_update',
                         validators=[DataRequired()])
    nama = TextField('Nama',
                         id='nama_update',
                         validators=[DataRequired()])
    gender = TextField('Jenis Kelamin',
                         id='gender_update',
                         validators=[DataRequired()])
    no_hp = TextField('Nomor HP',
                         id='no_hp_update',
                         validators=[DataRequired()])
    email = TextField('Email',
                      id='email_update',
                      validators=[DataRequired(), Email()])
    tanggal_lahir = TextField('Tanggal Lahir',
                         id='tanggal_lahir_update',
                         validators=[DataRequired()])
    alamat = TextField('Username',
                         id='alamat_update',
                         validators=[DataRequired()])
    tanggal_masuk = TextField('Username',
                         id='tanggal_masuk_update',
                         validators=[DataRequired()])
    password = PasswordField('Password',
                             id='pwd_update',
                             validators=[DataRequired()])