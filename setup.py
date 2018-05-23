import shutil
import os
import backup

try:
    input = raw_input
except NameError:
    pass

USER = os.path.expanduser('~')
ROOT_DIR = os.path.dirname(os.path.realpath(__file__))


def append_bashrc():
    with open('{}/bashrc_append.txt'.format(ROOT_DIR), 'r') as content_file:
        content = content_file.read()

    with open('{}/.bashrc'.format(USER), "ab+") as file:
        if content in file.read():
            print("\n~/.bashrc already contains .bash_bindings loader.")
        else:
            print("\nAppending ~/.bashrc with .bash_bindings loader.")
            file.write(content)


def update_inputrc():
    if os.path.isfile('{}/.inputrc'.format(USER)):
        print("\nReplacing existing ~/.inputrc")
    else:
        print("\nCreating ~/.inputrc")
    shutil.copy2('{}/inputrc_config'.format(ROOT_DIR),
                 '{}/.inputrc'.format(USER))


def update_bash_bindings():
    if os.path.isfile('{}/.bash_bindings'.format(USER)):
        print("\nReplacing existing ~/.bash_bindings")
    else:
        print("\nCreating ~/.bash_bindings")
    shutil.copy2('{}/bash_bindings_config'.format(ROOT_DIR),
                 '{}/.bash_bindings'.format(USER))


if __name__ == '__main__':

    print("Creating a backup in case anything goes wrong.\n")
    backup.main()

    append_bashrc()
    update_inputrc()
    update_bash_bindings()

    print("\nSetup complete. Restart terminal to make changes take effect.")
