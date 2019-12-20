import datetime
from flask import render_template, session, redirect, url_for, abort, flash
from . import main
from .. import db
from ..models import User, Module, User_Module
from .forms import AddModuleForm, EditModuleForm, GiveScoreForm, EditUserForm
from flask_login import current_user


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/user/<name>')
def user(name):
    user = User.query.filter_by(name=name).first_or_404()
    return render_template('user.html', user=user)


@main.route('/add_module', methods=['GET', 'POST'])
def add_module():
    form = AddModuleForm()
    if form.validate_on_submit():
        m = Module(module_code=form.module_code.data,
                   title=form.title.data,
                   staff=form.staff.data,
                   exam_date=form.exam_date.data)
        db.session.add(m)
        db.session.commit()
        flash('Create a Module Successfully')
        return redirect(url_for('main.index'))

    return render_template('add_module.html',
                           form=form)


@main.route('/list_modules')
def list_modules():
    modules = Module.query.all()
    n = len(modules)
    for i in range(0, n):
        minn = i
        for j in range(i + 1, n):
            if modules[j].exam_date < modules[minn].exam_date:
                minn = j
        modules[minn], modules[i] = modules[i], modules[minn]
    return render_template('list_module.html',
                           modules=modules)


@main.route('/edit_modules/<id>', methods=['GET', 'POST'])
def edit_module(id):
    module = Module.query.get_or_404(id)
    form = EditModuleForm(obj=module)
    if form.validate_on_submit():
        m = module
        m.module_code = form.module_code.data
        m.title = form.title.data
        m.staff = form.staff.data
        m.exam_date = form.exam_date.data
        db.session.commit()
        flash('Edit a Module Successfully')
        return redirect(url_for('main.list_modules'))

    return render_template('edit_module.html',
                           form=form)


@main.route('/delete_module/<id>', methods=['GET', 'POST'])
def delete_module(id):
    module = Module.query.get_or_404(id)
    db.session.delete(module)
    db.session.commit()
    flash('Delete a Module Successfully')
    return redirect(url_for('main.list_modules'))


@main.route('/choose_module/', methods=['GET', 'POST'])
def choose_module():
    modules = Module.query.all()
    user_module = User_Module.query.all()
    user_modules = []
    for u in user_module:
        if u.user_id == current_user.id:
            idd = u.module_id
            module = Module.query.get_or_404(idd)
            user_modules.append(module)

    return render_template('choose_module.html',
                           modules=modules,
                           user_modules=user_modules)


@main.route('/choose_this/<id>', methods=['GET', 'POST'])
def choose_this(id):
    user_module = User_Module(user_id=current_user.id,
                              module_id=id,
                              grade=0)
    db.session.add(user_module)
    db.session.commit()
    flash('Take a Module Successfully')
    return redirect(url_for('main.choose_module'))


@main.route('/check_module', methods=['GET', 'POST'])
def check_module():
    user_module = User_Module.query.all()
    modules = []
    for u in user_module:
        if u.user_id == current_user.id:
            idd = u.module_id
            module = Module.query.get_or_404(idd)
            modules.append(module)
    n = len(modules)
    for i in range(0, n):
        minn = i
        for j in range(i + 1, n):
            if modules[j].exam_date < modules[minn].exam_date:
                minn = j
        modules[minn], modules[i] = modules[i], modules[minn]
    return render_template('check_module.html',
                           modules=modules)


@main.route('/give_up_module/<id>', methods=['GET', 'POST'])
def give_up_module(id):
    user_module = User_Module.query.all()
    module = Module.query.get_or_404(id)
    for u in user_module:
        if u.user_id == current_user.id and u.module_id == module.id:
            db.session.delete(u)
            db.session.commit()
            flash('Give up a Module Successfully')
    return redirect(url_for('main.check_module'))


@main.route('/module_user/<id>', methods=['GET', 'POST'])
def module_user(id):
    user_module = User_Module.query.all()
    module = Module.query.get_or_404(id)
    users = []
    for u in user_module:
        if u.module_id == module.id:
            idd = u.user_id
            userr = User.query.get_or_404(idd)
            users.append(userr)
    return render_template('module_user.html',
                           users=users,
                           module=module)


@main.route('/delete_student_from_module/<id>/<idd>', methods=['GET', 'POST'])
def delete_student_from_module(id, idd):
    module = Module.query.get_or_404(idd)
    userr = User.query.get_or_404(id)
    user_module = User_Module.query.all()
    for u in user_module:
        if u.user_id == userr.id and u.module_id == module.id:
            db.session.delete(u)
            db.session.commit()
            flash('Remove the student Successfully')
    return redirect(url_for('main.module_user', id=module.id))


@main.route('/give_score/<id>/<idd>', methods=['GET', 'POST'])
def give_score(id, idd):
    module = Module.query.get_or_404(idd)
    userr = User.query.get_or_404(id)
    user_module = User_Module.query.all()
    for u in user_module:
        if u.module_id == module.id and u.user_id == userr.id:
            uu = u
    form = GiveScoreForm(obj=uu)
    if form.validate_on_submit():
        uuu = uu
        uuu.grade = form.score.data
        db.session.commit()
        return redirect(url_for('main.module_user', id=module.id))

    return render_template('give_score.html',
                           form=form)


@main.route('/check_score', methods=['GET', 'POST'])
def check_score():
    idd = current_user.id
    name = current_user.name
    modules = Module.query.all()
    user_module = User_Module.query.all()
    a = []
    for u in user_module:
        if u.user_id == idd and u.grade != 0:
            a.append(u)
    return render_template('check_score.html',
                           name=name,
                           user_modulee=a,
                           modules=modules)


@main.route('/check_users', methods=['GET'])
def check_users():
    userss = User.query.all()
    users = []
    for u in userss:
        if u.email != '978633302@qq.com':
            users.append(u)
    return render_template('check_users.html',
                           users=users)


@main.route('/edit_user/<id>', methods=['GET', 'POST'])
def edit_user(id):
    userr = User.query.get_or_404(id)
    form = EditUserForm(obj=userr)
    if form.validate_on_submit():
        m = userr
        m.name = form.name.data
        m.department = form.department.data
        m.gender = form.gender.data
        m.student_id = form.student_id.data
        m.phone_number = form.phone_number.data
        db.session.commit()
        flash('Edit a User Successfully')
        return redirect(url_for('main.check_users'))

    return render_template('edit_user.html',
                           form=form)


