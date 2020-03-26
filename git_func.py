import subprocess
import os

os.chdir('C:\\Users\\shaki\\Desktop\\git_test')
print(os.getcwd())


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
    # clone_link = 'https://github.com/MitanshuShaBa/email_tutorial.git'
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


def help():
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


# status()
# add()


# help()


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
