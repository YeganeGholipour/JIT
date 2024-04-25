# Import libraries for working with files and command-line
# We need to check which command it's been asked to run
# If the command equals to 'init', it runs the initialisation code, 
# otherwise print an error
# We need to figure out where to put the new repository
# If the first element of arguments in the command-line exists, we use it
# Otherwise we use the default value, which is the current working directory
# We need To convert the relative path to absolute path
#  Wee need to wrap this path into Pathname for manipulating str (here is path)
# Then we create to directory: objects and refs
# $ python jit.py init path/to/repository




import os
import sys
import errno
from datetime import datetime

from workspace import Workspace
from database import Database
from blob import Blob
from entry import Entry
from tree import Tree
from author import Author
from commit import Commit

# python jit.py init path/to/repository
# the 0 argument is 'jit.py'

arguments = sys.argv[1:] # init path/to/repository

command = arguments.pop(0) # init/commit/...

if command == "init":
    if arguments: # if there is a path specified pop it and use it
        path = arguments.pop(0) 
    else:
        path = os.getcwd() # if not, the path is the current working directory

    root_path = os.path.abspath(path) # create the absulote path
    git_path = os.path.join(root_path, ".git") # create a .git directory

    for directory in ["objects", "refs"]: # create two directories
        try:
            os.makedirs(os.path.join(git_path, directory))
        except OSError as e:
            if e.errno != errno.EACCES:
                sys.stderr.write(f"fatal: {e.strerror}\n")
                sys.exit(1)
    sys.stdout.write(f"Initialized empty Jit repository in {git_path}")
    sys.exit(0)


# we just assume the current working directory is the location of the repo.
# The Workspace class is responsible for the files in the working tree — all the files you edit directly, rather than those stored in .git.
# Database object, which will be responsible for managing the files in .git/objects
# For each file in the workspace, we’ll create a Blob object that contains the file’s contents
# n we’ll tell the database to store that blob object.
    
elif command == "commit":
    root_path = os.getcwd()
    git_path = os.path.join(root_path, ".git")
    db_path = os.path.join(git_path, "objects")

    workspace = Workspace(root_path)
    database = Database(db_path)

    entries = []
    for path in workspace.list_files():
        data = workspace.read_file(path)
        blob = Blob(data)

        database.store(blob)

        entry = Entry(path, blob.oid)  # Create Entry object with name and oid
        entries.append(entry)

    # print(workspace.list_files())
    
    tree = Tree(entries)
    database.store(tree)

    name = os.environ.get("GIT_AUTHOR_NAME")
    email = os.environ.get("GIT_AUTHOR_EMAIL")
    author = Author(name, email, datetime.now())
    message = sys.stdin.read()

    commit = Commit(tree.oid, author, message)
    database.store(commit)

    head_path = os.path.join(git_path, "HEAD")

    with open(head_path, 'w+') as file:
        file.write(commit.oid + "\n")

    print(f"[(root-commit) {commit.oid}] {message.splitlines()[0]}")
    
    exit(0)


    # print(f"tree: {tree.oid}")

else:
    sys.stderr.write(f"jit: '{command}' is not a jit command.\n")
    sys.exit(1)

