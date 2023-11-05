"""
Application Switcher
- Switch between project folder source files based on index/choice
"""
import os
import sys
from subprocess import Popen, PIPE

def run(cmd_str):
    status_code = os.system(cmd_str)
    return status_code

def run_pipe(cmd_list, shell=False):
    # Initialize Variables
    stdout = ""
    stderr = ""
    status_code = -1

    # Open process instance
    print(cmd_list)
    with Popen(cmd_list, stdin=PIPE, stdout=PIPE, shell=shell) as proc:
        # Open Process to execute command
        res = proc.communicate()
        stdout = res[0]
        stderr = res[1]
        status_code = proc.returncode

        if stdout != None:
            stdout = stdout.decode("utf-8")

        if stderr != None:
            stderr = stderr.decode("utf-8")

    return [status_code, stdout, stderr]

def begin_app(cmd_list):
    # Formatting
    cmd_str = " ".join(cmd_list).strip()

    # Run without standard output pipe
    print("Executing: {}".format(cmd_str))
    status_code = run(cmd_str)
    print("")
    print("Status Code: {}".format(status_code))

    print("")

    # Run with piping standard output
    print("Executing: {}".format(cmd_list))
    status_code,stdout,stderr = run_pipe(cmd_list,True)
    print("Status Code: {}".format(status_code))
    print("Standard Output: {}".format(stdout))

def main():
    # Initialize Variables
    project_env = ""
    project_fldr = ""
    project_runner = ""
    project_args = ""
    cmd_str = ""
    cmd_list = []
    app_Map = {
        # Application ID variable mapping dictionary
        0 : {
            "project_env" : [
                # "DATABASE_PATH=.", 
                # "DATABASE_NAME=test.db"
            ],
            "project_fldr" : "app/sqlite/db_create",
            "project_runner" : "main.py",
            "project_args" : "",
        }
    }

    # Get CLI arguments
    exec = sys.argv[0]
    argv = sys.argv[1:]
    argc = len(argv)

    if argc > 0:
        # Get application ID
        app_id = int(argv[0])

        # Default if application ID not in list of applications
        if not(app_id in app_Map.keys()):
            # Application ID not in app_Map
            project_env = ""
            project_fldr = ""
            project_runner = ""
            project_args = ""
        else:
            project_env = app_Map[app_id]["project_env"]
            project_fldr = app_Map[app_id]["project_fldr"]
            project_runner = app_Map[app_id]["project_runner"]
            project_args = app_Map[app_id]["project_args"]

        # Check for null values
        if (project_fldr != "") and (project_runner != ""):
            # Execute application
            # cmd_str += "{} python {}/{} {}".format(project_env, project_fldr, project_runner, project_args)

            # Append environment variables if provided
            if len(project_env) > 0:
                # Loop through environment list
                for i in range(len(project_env)):
                    # Get current environment variable 
                    curr_env = project_env[i]

                    # Append into list
                    cmd_list.append(curr_env)

            # Append executable
            cmd_list.append("python")

            # Append script
            cmd_list.append("{}/{}".format(project_fldr, project_runner))

            # Append arguments if provided
            if project_args != "":
                cmd_list.append(project_args)

            """
            Place your code to execute here
            """
            begin_app(cmd_list)
        else:
            print("No projects specified.")
    else:
        print("No arguments provided.")

if __name__ == "__main__":
    main()


