import re, json, subprocess
from mrglib import Experiment, Project

class Manager:
    def __init__(self):
        pass

    def find_project(self, name):
        proc = subprocess.run(['mrg', 'show', 'project', name, '-j'], capture_output=True)
        if proc.returncode == 0:
            data=json.loads(proc.stdout.decode())
            description=None
            creator=None
            if "description" in data["project"]:
                description=data["project"]["description"]
            for m in data["project"]["members"]:
                if "role" in data["project"]["members"][m]:
                    if data["project"]["members"][m]["role"] == "Creator":
                        creator=m
            p = Project.Project(name, description, creator)
            return p
        else:
            return None

    def find_experiment(self, name, project):
        proc = subprocess.run(['mrg', 'show', 'experiment', name + "." + project], capture_output=True)
        if proc.returncode == 0:
            lines = proc.stdout.decode().splitlines()
            flag = False
            real = None
            revision = 0
            for l in lines:
                if re.search(r'Realizations', l) != None:
                    index = lines.index(l)
                    nextline = lines[index+3]
                    revision = nextline.split()[0]                    
                    fullname = nextline.split()[1]
                    real = fullname.split('.')[0]
                    break
            ex = Experiment.Experiment(name, project, 0)
            ex.realization = real
            ex.revision = revision
            return ex
                
        else:
            return None

    def create_project(self, name, description, creator, organization=None, category='Research', mode='Public'):
        cmd = ['mrg', 'new', 'project', name, description]
        if organization != None:
            cmd.extend(['--organization', organization])
        if category != None:
            cmd.extend(['--category', category])
        if mode != None:
            cmd.extend(['--mode', mode])
        print("Cmd is ", cmd)
        proc = subprocess.run(cmd, check=True)
        if (proc.returncode == 0):
            proj=Project.Project(name, description, creator, organization, category, mode)
            return proj
        else:
            return None

    def create_experiment(self, name, project, description=None):
        if (self.find_project(project) == 0):
            proc = subprocess.run(['mrg', 'new', 'experiment', name + '.' + project, description], check=True)
        return proc.returncode


    


    