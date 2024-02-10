from flask import Flask, jsonify, request
import os
import git
import shutil

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    return jsonify(hello="world")

@app.route("/push_boilerplate", methods=['POST'])
def push_boilerplate_2():
    if request.method == 'POST':
        request_data = request.get_json()
        git_source_url = request_data['git_source_url']
        git_destination_url = request_data['git_destination_url']

        cwd = os.getcwd()
        print('cwd: %s', cwd)
        path_to_clone = cwd + "/gitcloneboilerplates/"
        os.mkdir(path_to_clone)

        try:
            boilerplate_name = git_source_url.split("/")[-1]
            repo_path = path_to_clone + boilerplate_name
            print('repo cloned path: %s', repo_path)
            source_repo = git.Repo.clone_from(url=git_source_url, to_path=repo_path, bare=True, mirror=True)
            os.chdir(repo_path)
            print('repo_path: %s cwd: %s files_inside_cwd: %s', repo_path, os.getcwd(), os.listdir())
            # g = git.Git(os.path.expanduser("usr/git/GitPython"))
            # g.execute(["git", "push", "--mirror", git_destination_url])
        except OSError as error:
            print("%s", error)
        except Exception as exception:
            print('Some error occurred while pushing the code %s', exception)

        os.chdir(cwd)
        # shutil.rmtree(path_to_clone)
        # os.system('rmdir /S /Q "{}"'.format(path_to_clone))
        print("reset cwd to: %s", cwd)

        return {'status_code': 200, 'description': 'push success'}
