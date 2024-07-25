from flask import Flask, request, render_template, redirect, url_for, flash
from flask_socketio import SocketIO, emit
import os
import shutil
import hashlib
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
socketio = SocketIO(app)

class MyHandler(FileSystemEventHandler):
    def __init__(self, socketio):
        super().__init__()
        self.socketio = socketio

    def on_modified(self, event):
        print(f'File modified: {event.src_path}')
        self.socketio.emit('file_modified', {'path': event.src_path})

def calculate_hash(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
        return hashlib.sha256(data).hexdigest()

def backup_data(source_dir, backup_dir):
    backup_folder = os.path.join(backup_dir, "backup")
    if os.path.exists(backup_folder):
        shutil.rmtree(backup_folder)
    shutil.copytree(source_dir, backup_folder)

def recover_data(backup_dir, target_dir):
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    shutil.copytree(backup_dir, target_dir)

def backup_file(source_file, backup_dir):
    shutil.copy2(source_file, backup_dir)

def verify_integrity(original_hash, recovered_file_path):
    recovered_hash = calculate_hash(recovered_file_path)
    return original_hash == recovered_hash

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_monitor', methods=['POST'])
def start_monitor():
    monitor_path = request.form['monitor_path'].strip('"')
    try:
        if not os.path.exists(monitor_path):
            flash(f"Path to monitor '{monitor_path}' does not exist.", 'danger')
        else:
            event_handler = MyHandler(socketio)
            observer = Observer()
            if os.path.isdir(monitor_path):
                observer.schedule(event_handler, path=monitor_path, recursive=True)
            else:
                observer.schedule(event_handler, path=os.path.dirname(monitor_path), recursive=False)
            observer.start()
            flash(f'Started monitoring: {monitor_path}', 'success')
            return redirect(url_for('index'))
    except Exception as e:
        flash(f"Error starting monitor: {str(e)}", 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    socketio.run(app, debug=True)
