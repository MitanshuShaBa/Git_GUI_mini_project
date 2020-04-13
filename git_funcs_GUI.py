import subprocess
#import os

#print(os.getcwd(), '\n')



# TODO remove all shell=True for full string command *backend*

def cmd_call(cmd):
    """
    runs any git command then returns its output and error
    :param cmd: string
    :return: out: string, err: string
    """
    msg = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    out = msg.stdout.decode()
    err = msg.stderr.decode()
    return out, err


def init(new_name):
    """
    Initialises local directory for git
    :return: None
    """
    cmd = 'git init ' + new_name.strip()

    out, err = cmd_call(cmd)  # todo *GUI* take this out and err to display
    if out:
        print(out)
    if err:
        print(err)

def clone(link):
    var = False
    """
    Clones git directory from GitHub using link
    :return: None
    """


    clone_link = link
    cmd = f'git clone {clone_link}'


    # Command is run here
    out, err = cmd_call(cmd)  # todo *GUI* take this out and err to display

    if out:
        return out
    if err:
        return err




def status():
    """
    Show the working tree status
    :return:
    """
    out, err = cmd_call('git status')  # todo *GUI* take this out and err to display
    if out:
        return out
    if err:
        return err


def add():
    """
    Add file contents to the index
    :return: None
    """
    # todo get file names from *GUI*
    #files = input("Enter file names to add or . if you want to add all files to staging area\n").strip().split()
    call = ['git', 'add'] + ['.']
    cmd = ' '.join(map(str, call))
    out, err = cmd_call(cmd)  # todo *GUI* take this out and err to display
    if out:
        return out
    if err:
        return out


def unstage():
    """
    Remove files from the working tree and from the index
    :return: None
    """
    # todo get file names from *GUI*
    # files with spaces have to be surrounded with "" todo give this warning to *GUI*
    files = input("Enter file names to remove or * if you want to remove all files from staging area\n").strip()
    cmd = 'git reset ' + files
    out, err = cmd_call(cmd)  # todo *GUI* take this out and err to display
    if out:
        print(out)
    if err:
        print(err)


def clean():
    """
    Remove untracked files from the working tree
    :return: None
    """
    # call = ['git', 'clean', '-f', '-n', '-d']
    cmd = 'git clean -f -n -d'
    out, err = cmd_call(cmd)  # todo *GUI* take this out and err to display
    if out:
        print(out)
    if err:
        print(err)

    choice = input("Do wish to clean these files from working tree (y/n):").lower()  # todo get y/n from *GUI*
    if choice == 'y':
        cmd = 'git clean -f -d'
        out, err = cmd_call(cmd)  # todo *GUI* take this out and err to display
        if out:
            print(out)
        if err:
            print(err)


def commit(msg):
    """
     Record changes to the repository
    :return: None
    """
    #message = 'Initial commit'
    #choice = input(f'{message} as commit message [y/n]').strip().lower()  # todo get y/n from *GUI*
    #if choice == 'n':
        #message = msg#input("Commit message:")  # todo get commit message from *GUI*

    cmd = f'git commit -m"{msg}"'
    out, err = cmd_call(cmd)  # todo *GUI* take this out and err to display
    if out:
        return out
    if err:
        return err


def add_remote(name ='rName', url =''):
    cmd = f'git remote add {name} {url}'  # todo *gui* name, url
    out, err = cmd_call(cmd)  # todo *GUI* take this out and err to display
    ''''if out:
        return out
    if err:
        return err'''


# add_remote('origin2', 'https://github.com/MitanshuShaBa/Git-test2.git')
def rename_remote(old, new):
    cmd = f'git remote rename {old} {new}'  # todo *gui* old, new
    out, err = cmd_call(cmd)  # todo *GUI* take this out and err to display
    if out:
        print(out)
    if err:
        print(err)


def show_remotes():
    cmd = 'git remote show'
    out, err = cmd_call(cmd)  # todo *GUI* take this out and err to display
    if out:
        print(out)
    if err:
        print(err)


def push_branch(remote, branch):
    cmd = f'git push {remote} {branch}'  # todo *GUI* input remote, branch
    out, err = cmd_call(cmd)  # todo *GUI* take this out and err to display
    if out:
        print(out)
    if err:
        print(err)


def push_all(remote='rName'):
    cmd = f'git push {remote} --all'  # todo *GUI* input remote
    out, err = cmd_call(cmd)  # todo *GUI* take this out and err to display
    if out:
        return out
    if err:
        return err


def pull(remote, branch):
    cmd = f'git pull {remote} {branch}'  # todo *GUI* input remote, branch
    out, err = cmd_call(cmd)  # todo *GUI* take this out and err to display
    if out:
        print(out)
    if err:
        print(err)


def branch_create():
    """
    Creates a branch
    :return: None
    """
    name = input("Enter name of branch:").strip()  # todo *GUI* input branch
    # case: empty name or name with space
    if name == '' or ' ' in name or not name.isalnum():  # todo *GUI* warning for empty name or name with spaces
        branch_create()
        return
    cmd = f'git branch {name}'
    out, err = cmd_call(cmd)  # todo *GUI* take this out and err to display
    if out:
        print(out)
    if err:
        print(err)


def branch_delete(branch):
    """
    deletes a branch
    :return: None
    """
    name = branch
    # name = input("Enter name of branch to be deleted:").strip()
    cmd = f'git branch {name} -d'  # todo *GUI* input name
    out, err = cmd_call(cmd)  # todo *GUI* take this out and err to display
    if out:
        print(out)
    if err:
        print(err)


def branch_rename():
    """
    Renames a branch
    :return: None
    """
    # todo *GUI* imput
    name = input("Enter name of branch:").strip()
    new_name = input("Enter name of new branch:").strip()
    # case: empty name or name with space
    if new_name == '' or ' ' in new_name or not new_name.isalnum():  # todo *GUI* warning for empty name or name with spaces
        print('Rename failed: Improper name')
        return
    cmd = f'git branch -m {name} {new_name}'
    out, err = cmd_call(cmd)  # todo *GUI* take this out and err to display
    if out:
        print(out)
    if err:
        print(err)


# branch_rename()
def branch_list():
    """
    Lists all branches
    :return:
    """
    cmd = 'git branch --list'
    out, err = cmd_call(cmd)  # todo *GUI* take this out and err to display
    if out:
        print(out)
    if err:
        print(err)


def checkout_branch(branch: str) -> None:
    """
    Checks out to a branch
    :parameter branch
    :type str
    :return None
    """
    cmd = f'git checkout {branch}'  # TODO *GUI* GET BRANCH
    out, err = cmd_call(cmd)  # todo *GUI* take this out and err to display
    if out:
        print(out)
    if err:
        print(err)


def checkout_commit(commit_addr: str) -> None:
    """
    Checks out to a branch
    :parameter commit_addr
    :type str
    :return None
    """
    cmd = f'git checkout {commit_addr}'  # TODO *GUI* GET commit
    out, err = cmd_call(cmd)  # todo *GUI* take this out and err to display
    if out:
        print(out)
    if err:
        print(err)


def merge(branch1, branch2):
    """
    Merges 2 branches together
    :parameter: branch1
    :type: str
    :parameter: branch2
    :type: str
    :return: None
    """
    checkout_branch(branch1)  # todo *gui* imput branch1 branch2
    cmd = f'git merge {branch2}'
    out, err = cmd_call(cmd)  # todo *GUI* take this out and err to display
    if out:
        print(out)
    if err:
        print(err)

    branch_delete(branch2)
