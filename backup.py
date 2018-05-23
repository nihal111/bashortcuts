import shutil
import os
import datetime

try:
    input = raw_input
except NameError:
    pass

USER = os.path.expanduser('~')
ROOT_DIR = os.path.dirname(os.path.realpath(__file__))


def custom_folder():
    FOLDER = input("Enter desired folder name: ")
    if os.path.exists('{}/backups/{}'.format(ROOT_DIR, FOLDER)):
        print("Folder {} already exists.".format(
            '{}/backups/{}'.format(ROOT_DIR, FOLDER)))
        return custom_folder()
    return FOLDER


def main():
    if not os.path.exists('{}/backups/'.format(ROOT_DIR)):
        os.mkdir('{}/backups/'.format(ROOT_DIR))

    BACKUP_FOLDER = "BACKUP_{:%Y-%m-%d}".format(datetime.datetime.now())

    if os.path.exists('{}/backups/{}'.format(ROOT_DIR, BACKUP_FOLDER)):
        BACKUP_FOLDER = "BACKUP_{:%Y-%m-%d-%H%M}".format(
            datetime.datetime.now())

    ans = input("Backing up to folder " +
                "{}/backups/{}.\n".format(ROOT_DIR, BACKUP_FOLDER) +
                "Press y/Y to continue. Press n/N to change folder name: ")

    if ans.lower() == "n":
        BACKUP_FOLDER = custom_folder()
    else:
        if os.path.exists('{}/backups/{}'.format(ROOT_DIR, BACKUP_FOLDER)):
            print("Folder {} already exists.".format(
                '{}/backups/{}'.format(ROOT_DIR, BACKUP_FOLDER)))
            BACKUP_FOLDER = custom_folder()

    BACKUP_DIR = '{}/backups/{}/'.format(ROOT_DIR, BACKUP_FOLDER)
    os.mkdir(BACKUP_DIR)

    if os.path.isfile('{}/.bashrc'.format(USER)):
        shutil.copy2('{}/.bashrc'.format(USER), BACKUP_DIR)
    if os.path.isfile('{}/.inputrc'.format(USER)):
        shutil.copy2('{}/.inputrc'.format(USER), BACKUP_DIR)

    print("\nBackup complete.")


if __name__ == '__main__':
    main()
