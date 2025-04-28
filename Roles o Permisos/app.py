from flask import Flask, redirect, url_for, render_template
from flask_principal import Principal, Permission, RoleNeed, Identity, AnonymousIdentity, identity_changed, identity_loaded
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.secret_key = 'secretkey'

login_manager = LoginManager(app)
login_manager.init_app(app)

Principal(app)

admin_permission = Permission(RoleNeed('admin'))
user_permission = Permission(RoleNeed('user'))

class User(UserMixin):
    def __init__(self,id, username, role):
        self.id = id
        self.username = username
        self.role = role

users ={
   "Kaleb": User(1, "Kaleb", role=["user"]),
   "Laura": User(2, "Laura", role=["admin"])
}

@login_manager.user_loader
def load_user(user_id):
    for user in users.values():
        if str(user.id) == str(user_id):
            return user
    return None

@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    if hasattr(current_user, 'role'):
        for role in current_user.role:
            identity.provides.add(RoleNeed(role))

@app.route('/')
def index():
    return render_template('index.html')

@app.route ('/login/<username>')
def login(username):
    user = users.get(username)
    if user:
        login_user(user)
        identity_changed.send(app, identity=Identity(user.id))
        return redirect(url_for('index'))
    return 'Usuario no encontrado', 404

@app.route('/logout')
@login_required
def logout():
    logout_user()
    identity_changed.send(app, identity=AnonymousIdentity())
    return redirect(url_for('index'))

@app.route('/admin')
@login_required
@admin_permission.require(http_exception=403)
def admin():
    return 'Bienvenido Administrador'

@app.route('/profile')
@login_required
@user_permission.require(http_exception=403)
def profile():
    return f'Bienvenido {current_user.username}'

if __name__ == "__main__":
    app.run(debug=True)


