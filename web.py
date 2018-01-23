from flask import Flask, render_template, redirect, request, url_for
import os
import subprocess
app = Flask(__name__)

@app.route('/')
def index():
    query = subprocess.check_output("awk -F':' '{ print $1}' /etc/passwd", shell = True)
    users = query.split()
    return render_template('index.html', value = users)


@app.route('/adduser', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['user']
        os.system("sudo useradd " +username)
        return redirect(url_for('index'))


    return render_template('add.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'POST':
        username = request.form['user']
        os.system("sudo userdel " +username)
        return redirect(url_for('index'))


    return render_template('add.html')

@app.route('/advance', methods=['GET', 'POST'])
def advanced_access():
    if request.method == 'POST':
        username = request.form['user']
        os.system("sudo usermod -a -G sudo " +username)
        return redirect(url_for('index'))


    return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)
