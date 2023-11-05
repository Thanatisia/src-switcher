#!/bin/env bash
: "
Application Switcher
- Switch between project folder source files based on index/choice
"
main()
{
    # Initialize Variables
    project_env=""
    project_fldr=""
    project_runner=""
    project_args=""

    # Get CLI arguments
    argv=("$@")
    argc="${#argv[@]}"

    # Get application ID
    app_id="${argv[0]}"

    # Switch-case through application
    case "$app_id" in
        0)
            # Project 1 : SQLite - db_create
            project_env="DATABASE_PATH=. DATABASE_NAME=test.db"
            project_fldr="app/sqlite/db_create"
            project_runner="main.py"
            project_args=()
            ;;
        *)
            project_env=""
            project_fldr=""
            project_runner=""
            project_args=""
            ;;
    esac

    if [[ "$project_fldr" != "" ]] && [[ "$project_runner" != "" ]]; then
        # Execute application
        cmd_str+="$project_env python $project_fldr/$project_runner ${project_args[@]}"

        # Execute command
        env $cmd_str
    else
        echo -e "No projects specified."
    fi
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
