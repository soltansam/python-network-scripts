import subprocess

def update_system():
    try:
        subprocess.run(['sudo', 'apt', 'update'])

        subprocess.run(['sudo', 'apt', 'upgrade'])

    except Exception as e:


