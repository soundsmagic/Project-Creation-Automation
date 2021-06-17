import sys, os, subprocess, requests, shutil, venv
from github import Github

# Control the number of arguments, exit if wrong number of arguments is given
if len(sys.argv) != 2:
    print("Usage: pca.py [project name]")
    exit()

# Navigate to the main project folder
print("Creating main folder...")
os.chdir("C:\\dev\\Python Projects")

# Create the main folder for the project and navigate into it
os.mkdir(sys.argv[1])
os.chdir("C:\\dev\\Python Projects\\" + sys.argv[1])

# Create local GIT repository
print("Initializing GIT...")
subprocess.run(["git", "init"])

# Fetch the correct .gitignore-file from the gitignore template list
print("Fetching and creating .gitignore for Python...")
with open(".\.gitignore", "w") as f:
    f.write(
        requests.get("https://api.github.com/gitignore/templates/Python").json()[
            "source"
        ]
    )

# Fetch and create Code of Conduct, and insert contact information
print("Fetching and creating Code of Conduct...")
with open(".\CODE_OF_CONDUCT.md", "w") as f:
    f.write(
        requests.get(
            "https://www.contributor-covenant.org/version/2/0/code_of_conduct/code_of_conduct.md"
        ).text.replace("[INSERT CONTACT METHOD]", os.environ["MY_EMAIL"])
    )

# Fetch and create license
print("Fetching and creating license...")
subprocess.run([shutil.which("npx"), "license", "MIT"])

# Create a Readme file, a requirements file, and Python files
print("Creating Readme, requirements, and Python files...")
python_files = [f"{sys.argv[1]}.py", "setup.py", "tests.py", "requirements.txt"]
for filename in python_files:
    open(filename, "w")
with open("README.md", "w") as f:
    f.write(
        "Placeholder for some enthralling and enlightening information about this project"
    )

# Create Github repository
print("Creating GitHub repo...")
g = Github(os.environ["GITHUB_TOKEN"])
user = g.get_user()
repo = user.create_repo(sys.argv[1], private=True)

# Make a first commit
print("Making the first commit...")
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Initial automated commit"])

# Add the Github repository as a remote and make the first push
print("Adding remote and making the first push...")
subprocess.run(["git", "remote", "add", "origin", repo.clone_url])
subprocess.run(["git", "push", "origin", "main"])

# Create a Virtual Environment for the project
print("Creating Virtual Environment...")
venv.create(f"C:\\dev\\Python Virtual Environments\\{sys.argv[1]}_env")

# Starting VS Code from the project folder
print("Starting VS Code...")
subprocess.run([shutil.which("code"), "."])
