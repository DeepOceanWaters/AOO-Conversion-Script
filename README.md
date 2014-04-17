## AOO-Conversion-Script

A script to convert the LINUX/UNIX AOO build system (modules) to a Windows based build system.

#### How to use

1. Enter module directory and delete the wntmsci12.pro directory.
2. Enter the main directory (contains all modules).
2. Run the vcprojGen.py script (format: python vcprojGen.py [moduleName]).
3. Run the vcGen.py script (format: python vcGen.py [moduleName]).

#### Git Intro

- Set up git: git config --global [user.name||user.email] "name/email in quotation marks"
- Clone repository: git clone https://github.com/Z3rp/AOO-Conversion-Script.git
- Update to latest version: git pull
- Making changes: git add [filename], then: git commit
- Update origin repository: git push
