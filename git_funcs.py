import subprocess
import os

INITIAL_PATH = 'C:\\Users\\shaki\\Desktop\\git_test'
os.chdir(INITIAL_PATH)
print(os.getcwd(), '\n')


# TODO remove all shell=True for full string command


def init():
    """
    Initialises local directory for git
    :return:
    """
    cmd = 'git init'
    choice = int(input("Do you want to initialise:\n"
                       "1.Current directory as git\n"
                       "2.Make new directory\n"))
    if choice == 2:
        subdirectory = input("Enter the name of the directory for git to track:").strip()
        cmd += ' ' + subdirectory

    # Command is run here
    subprocess.run(cmd)

    if choice == 2:
        os.chdir(os.path.join(os.getcwd(), subdirectory))


def clone():
    """
    Clones git directory from GitHub using link
    :return: None
    """
    # TODO change remote to personal GitHub link
    # clone_link = 'https://github.com/MitanshuShaBa/email_tutorial.git'
    new_name = ''
    clone_link = input("Enter clone link:\n")
    cmd = f'git clone {clone_link}'
    choice = int(input("Do you want to clone:\n"
                       "1.In directory as same name\n"
                       "2.Make new directory with different name\n"))
    if choice == 2:
        new_name = input("Enter the name of the directory for git to track:").strip()
        cmd += ' ' + new_name

    # Command is run here
    subprocess.run(cmd)

    if choice == 2:
        os.chdir(os.path.join(os.getcwd(), new_name))


def git_help():
    """
    Shows help message
    :return: None
    """
    subprocess.check_call(['git', '--help'])


def status():
    """
    Show the working tree status
    :return:
    """
    subprocess.check_call(['git', 'status'])


def add():
    """
    Add file contents to the index
    :return: None
    """
    files = input("Enter file names to add or . if you want to add all files to staging area\n").strip().split()
    call = ['git', 'add'] + files
    try:
        subprocess.check_call(call)
    except subprocess.CalledProcessError as e:
        print(e)


def unstage():
    """
    Remove files from the working tree and from the index
    :return: None
    """
    files = input("Enter file names to remove or * if you want to remove all files to staging area\n").strip().split()
    call = ['git', 'rm', '--cached'] + files
    try:
        subprocess.check_call(call)
    except subprocess.CalledProcessError as e:
        print(e)


def clean():
    """
    Remove untracked files from the working tree
    :return: None
    """
    # call = ['git', 'clean', '-f', '-n', '-d']
    call = 'git clean -f -n -d'
    try:
        # for later integration with GUI
        # TODO make this kind of output for every function
        print(subprocess.run(call, stdout=subprocess.PIPE).stdout.decode())
    except subprocess.CalledProcessError as e:
        print(e)
        return
    choice = input("Do wish to clean these files from working tree (y/n):").lower()
    if choice == 'y':
        call = 'git clean -f -d'
        try:
            subprocess.run(call)
        except subprocess.CalledProcessError as e:
            print(e)
            return


# clean()
def branch_create():
    """
    Creates a branch
    :return: None
    """
    name = input("Enter name of branch:").strip()
    # case: empty name or name with space
    if name == '' or ' ' in name or not name.isalnum():
        print()
        branch_create()
        return
    cmd = f'git branch {name}'
    branch_exists_msg = f"fatal: A branch named '{name}' already exists."
    try:
        message = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = message.stdout
        err = message.stderr.decode()
        # case: branch name exists
        if err.strip() == branch_exists_msg:
            print(branch_exists_msg.replace('fatal: ', ''))
            print("Try again\n")
            branch_create()
        else:
            print('branch', name, 'created')
    except subprocess.CalledProcessError as e:
        print(e)


# branch_create()

def branch_delete():
    """
    deletes a branch
    :return: None
    """
    name = input("Enter name of branch to be deleted:").strip()
    cmd = f'git branch {name} -d'
    try:
        message = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = message.stdout.decode()
        err = message.stderr.decode()
        if err:
            print(err)
        else:
            print(out)
    except subprocess.CalledProcessError as e:
        print(e)


# branch_delete()
def branch_rename():
    """
    Renames a branch
    :return: None
    """
    name = input("Enter name of branch:").strip()
    new_name = input("Enter name of new branch:").strip()
    # case: empty name or name with space
    if new_name == '' or ' ' in new_name or not new_name.isalnum():
        print('Rename failed: Improper name')
        return
    cmd = f'git branch -m {name} {new_name}'
    branch_exists_msg = f"fatal: A branch named '{new_name}' already exists."
    branch_not_found_msg = f"error: refname refs/heads/side not found\nfatal: Branch rename failed\n"
    try:
        message = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        err = message.stderr.decode()
        # case: branch name exists
        if err.strip() == branch_exists_msg:
            print(branch_exists_msg.replace('fatal: ', ''))
        elif err:
            print(f'branch {name} does not exist')
        else:
            print('branch', name, 'renamed to', new_name)
    except subprocess.CalledProcessError as e:
        print(e)


# branch_rename()
def branch_list():
    """
    Lists all branches
    :return:
    """
    try:
        print('Branches:\n', subprocess.run('git branch', stdout=subprocess.PIPE).stdout.decode())
    except:
        pass
# branch_list()


def commit():
    """
     Record changes to the repository
    :return: None
    """
    message = 'Initial commit'
    choice = input(f'{message} as commit message [y/n]').strip().lower()
    if choice == 'n':
        message = input("Commit message:")
    try:
        subprocess.check_call(['git', 'commit', f'-m"{message}"'])
    except subprocess.CalledProcessError as e:
        print(e)


# git_help()

def git():
    """
    Main function through which every function is handled
    :return: None
    """
    pass


def boot():
    """
    Sets up the directory for git
    :return: None
    """
    choice = int(input("1.If you want to stay in current directory\n"
                       "2.To change directory\n"))
    if choice == 2:
        path = input("Give path to directory\n")
        if not os.path.isdir(path):
            print('Wrong directory path, enter correct directory\n')
            boot()
            return
        os.chdir(path)
        print(os.getcwd())
    is_tracking = (os.path.exists(os.path.join(os.getcwd(), '.git')))
    if not is_tracking:
        start = int(input("1.Init\n"
                          "2.Clone\n"))
        if start == 1:
            init()
        elif start == 2:
            clone()
    git()

# boot()
