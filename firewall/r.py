from flask import Flask, request, render_template, flash, redirect, url_for
import shutil
import os
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/backup_form')
def backup_form():
    return render_template('backup_form.html')

@app.route('/backup_file', methods=['POST'])
def backup_file():
    backup_dir = request.form['backup_dir']
    file_to_backup = request.form['file_to_backup']
    
    logging.debug(f"File to backup: {file_to_backup}")
    logging.debug(f"Backup directory: {backup_dir}")
    
    # Normalize paths
    file_to_backup = os.path.normpath(file_to_backup)
    backup_dir = os.path.normpath(backup_dir)
    
    logging.debug(f"Normalized file to backup: {file_to_backup}")
    logging.debug(f"Normalized backup directory: {backup_dir}")
    
    if not os.path.exists(file_to_backup):
        flash(f"File '{file_to_backup}' does not exist.", 'danger')
    elif not os.path.isfile(file_to_backup):
        flash(f"'{file_to_backup}' is not a file.", 'danger')
    elif not os.path.isdir(backup_dir):
        flash(f"Backup directory '{backup_dir}' does not exist.", 'danger')
    else:
        try:
            shutil.copy2(file_to_backup, backup_dir)
            flash(f"File '{file_to_backup}' backed up to '{backup_dir}'.", 'success')
        except Exception as e:
            flash(f"Error occurred while backing up file: {str(e)}", 'danger')
    
    return redirect(url_for('index'))

@app.route('/recovery_form')
def recovery_form():
    return render_template('recovery_form.html')

@app.route('/recover_file', methods=['POST'])
def recover_file():
    backup_file = request.form['backup_file']
    recovery_dir = request.form['recovery_dir']
    original_filename = request.form['original_filename']
    recovery_path = os.path.join(recovery_dir, original_filename)
    
    logging.debug(f"Backup file: {backup_file}")
    logging.debug(f"Recovery directory: {recovery_dir}")
    logging.debug(f"Recovery path: {recovery_path}")
    
    # Normalize paths
    backup_file = os.path.normpath(backup_file)
    recovery_dir = os.path.normpath(recovery_dir)
    recovery_path = os.path.normpath(recovery_path)
    
    logging.debug(f"Normalized backup file: {backup_file}")
    logging.debug(f"Normalized recovery directory: {recovery_dir}")
    logging.debug(f"Normalized recovery path: {recovery_path}")
    
    if not os.path.exists(backup_file):
        flash(f"Backup file '{backup_file}' does not exist.", 'danger')
    elif not os.path.isfile(backup_file):
        flash(f"'{backup_file}' is not a file.", 'danger')
    elif not os.path.isdir(recovery_dir):
        flash(f"Recovery directory '{recovery_dir}' does not exist.", 'danger')
    else:
        try:
            shutil.copy2(backup_file, recovery_path)
            flash(f"Backup file '{backup_file}' recovered to '{recovery_path}'.", 'success')
        except Exception as e:
            flash(f"Error occurred while recovering file: {str(e)}", 'danger')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
