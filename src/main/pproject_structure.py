import os
import subprocess

def create_project_structure(project_name,short_desc,remote_url):
    # Define project structure
    structure = {
        'src': {
            'main': {},
            'resources':{}
        },
        'test': {},
        'documentation':{},
        'README.md':''
    }
    
    # Create project directory
    os.makedirs(project_name)
    os.chdir(project_name)
    
    # Create project structure
    for folder, contents in structure.items():
        if folder == 'README.md':
            with open(folder, 'w') as f:
                f.write(f'# {project_name} \n')
                f.write(f'{short_desc} \n')
                f.write('## Table of Contents \n')
                f.write('- [Installation](#installation) \n')
                f.write('- [Usage](#usage) \n')
                f.write('- [Contributing](#contributing) \n')
                f.write('## Installation \n')
                f.write('1. Clone the repository: \n')
                f.write(' ```bash \n')
                f.write(f' git clone [text](url){remote_url} \n')
                f.write(' ``` \n')
                f.write('2. Install dependencies: \n')
                f.write('```bash \n')
                f.write('npm install \n')
                f.write(' ``` \n\n')
                f.write('## Contributing \n')
                f.write('1. Fork the repository.\n')
                f.write('2. Create a new branch: `git checkout -b feature-name`. \n')
                f.write('3. Make your changes. \n')
                f.write('4. Push your branch: `git push origin feature-name`. \n')
                f.write('5. Create a pull request. \n\n')
                f.write('## License \n')
                f.write('This project is licensed under the [MIT License](LICENSE) .\n')
        else:
            os.makedirs(folder)
            os.chdir(folder)
            for item, content in contents.items():
                if isinstance(content, dict):
                    os.makedirs(item)
                else:
                    with open(item, 'w') as f:
                        f.write(content)
            os.chdir('..')
            
def initialize_git(commit_msg):
    # Initialize Git repository
    subprocess.run(['git', 'init'])
    subprocess.run(['git', 'add', '*'])
    subprocess.run(['git', 'commit', '-m', commit_msg])
    subprocess.run(['git', 'branch', '-M', 'main'])
    
def link_remote_repo(remote_url):
    # Link local and remote repositories
    subprocess.run(['git', 'remote', 'add', 'origin', remote_url])
    subprocess.run(['git', 'push', '-u', 'origin', 'main'])
    print("Local and remote repositories linked successfully.")

def main():
    project_name = input("Enter the name of your project: ")
    remote_url = input("Enter the URL of the remote repository: ")
    short_desc = input("in one short sentence what is your project about?: ")
    commit_msg = input("what is your initial commit message for git? : ")
    create_project_structure(project_name,short_desc,remote_url)
    initialize_git(commit_msg)
    link_remote_repo(remote_url)

if __name__ == "__main__":
    main()