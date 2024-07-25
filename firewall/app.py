from flask import Flask, request, render_template, flash, redirect, url_for
import shutil
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/backup_form')
def backup_form():
    return render_template('backup_form.html')

@app.route('/backup_file', methods=['POST'])
def backup_file():
    backup_dir = request.form['backup_dir']
    file_to_backup = request.form['file_to_backup']
    
    if not os.path.exists(file_to_backup):
        flash(f"File '{file_to_backup}' does not exist.", 'danger')
    elif not os.path.isfile(file_to_backup):
        flash(f"'{file_to_backup}' is not a file.", 'danger')
    else:
        try:
            shutil.copy2(file_to_backup, backup_dir)
            flash(f"File '{file_to_backup}' backed up to '{backup_dir}'.", 'success')
        except Exception as e:
            flash(f"Error occurred while backing up file: {str(e)}", 'danger')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
h