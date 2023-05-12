import subprocess
# Define a function to run update and upgrade commands in Ubuntu
def update_system():
    try:
        subprocess.run(['sudo', 'apt', 'update'])

        subprocess.run(['sudo', 'apt', 'upgrade', '-y'])

    except Exception as e:
        print(f"A Error occurred which is: {str(e)}")

# Now call the method above 
update_system()


