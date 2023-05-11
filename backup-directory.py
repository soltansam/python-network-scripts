import tarfile
import os
import datetime


def backup_directory(source_dir, backup_dir):
    timestamp = datetime.datetime.now().strftime("%Y%m%d&H%M%S")

    # Create the backup file name
    backup_filename = f"backup_{timestamp}.tar.gz"
    # Create the full path for the backup file
    backup_path = os.path.join(backup_dir, backup_filename)
    try:
        # Create a tarball of the source directory
        with tarfile.open(backup_path, "w:gz") as tar:
            tar.add(source_dir, arcname=os.path.basename(source_dir))
        print(f"Backup created successfully at: {backup_path}")
    except Exception as e:
        print(f"An error occurred while creating the backup: {str(e)}")

# Specify the source directory and backup directory
source_directory = "/path/to/source/directory"
backup_directory = "/path/to/backup/directory"

# Call the backup_directory function
backup_directory(source_directory, backup_directory)
