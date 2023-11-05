# Makefile for Python Library

## Variable/Ingredients
LIB_SRC_PATH = src/lib
LIB_SRC_FILES = src/lib/sqlite_lib.py
LIB_DST_PATH = /usr/lib/thanatisia/sqlite_lib

APP_ROOT_PATH = src/app
APP_TARGET_PROJECT = src/app/sqlite/db_create
APP_TARGET_PROJECT_FILES = main.py setup.py env.py configs.py

APP_SWITCHER_DIR = src
APP_SWITCHER_EXEC = run.py
APP_SWITCHER_ARGS = 0

.PHONY := help, install
.DEFAULT_RULES := help
PATH := "$(PATH):src:${LIB_SRC_PATH}:${APP_ROOT_PATH}:${APP_TARGET_PROJECT}:"
SHELL := bash
EDITOR := nvim

## Recipe/Target/Rule
help:
	## Display help
	@echo -e "help      : Display help menu"
	@echo -e "edit      :  Open the source file in editor"
	@echo -e "install   : Install the library into the system"
	@echo -e "uninstall : Uninstall/Remove the library from the system"
	@echo -e "start     : Begin/Start running the application switcher"

edit:
	## Open the source file in editor
	${EDITOR} ${APP_TARGET_PROJECT}/main.py

install:
	## Install library to system
	@mkdir -p ${LIB_DST_PATH}
	@cp -r ${LIB_SRC_FILES} ${LIB_DST_PATH}

uninstall:
	## Uninstall/remove library from system
	@rm -r ${LIB_DST_PATH}

start:
	## Run the application switcher project launcher
	@echo -e "${PATH}"

	@cd ${APP_SWITCHER_DIR} && \
		python ./${APP_SWITCHER_EXEC} ${APP_SWITCHER_ARGS}


