from flask import Flask, render_template, url_for, flash, redirect, request
from werkzeug import secure_filename
from forms import RegistrationForm, LoginForm
from saveregistration import SaveRegistration

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/upload")
def uploadfile():
    return render_template('uploadfile.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      flash(f'Uploaded {f.filename} succefully.', 'success')
      return redirect(url_for('uploadfile'))

@app.route("/trainmodel", methods = ['POST'])
def trainmodel():
    flash(f'The model is trained succefully.', 'success')
    return render_template('uploadfile.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        fileName = "userform.txt"
        save = SaveRegistration(email, password, fileName)
        if save.doesUserExist() == 1:
            flash(f'Account already exist for {form.email.data}!', 'danger')
            return redirect(url_for('register'))
        else:
            save.appendToFile()
            flash(f'Account created for {form.username.data}!', 'success')
            return redirect(url_for('home'))
        
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        fileName = "userform.txt"
        save = SaveRegistration(email, password, fileName)
        if save.isValidUser() == 1:
            flash('You have been logged in!', 'success')
            return redirect(url_for('uploadfile'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)