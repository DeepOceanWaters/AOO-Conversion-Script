## AOO-Conversion-Script

A script to convert the LINUX/UNIX AOO build system (modules) to a Windows based build system.

#### How to use

1. Enter module directory and delete the **wntmsci12.pro** directory.
2. Enter the main directory (contains all modules).
2. Run the vcprojGen.py script (format: ```python vcprojGen.py [moduleName]```).
3. Run the vcGen.py script (format: ```python vcGen.py [moduleName]```).

#### Manual Conversion
1. Open CygWin
2. Navigate to main directory.
3. Execute: ```source winenv.set.sh```
4. Enter the **instsetoo_native** directory.
5. Execute: ```build -all:[moduleName]``` (redirect output to a file, must manually cancel after script has built the module)
6. Open file made in step 5, and delete everything after the second occurrence of **Building module**.
7. Each portion of the module should begin with **Entering directory xxx** and then calls to cl.exe; copy one of these commands and make the following changes:
  - Replace "C:\steve\TestArea\main" with ".."
  - Remove occurrences of "../.."
  - Remove the last 2 arguments (should be "-F[pathname]" and the filename of the file being compiled)
  - Remove include paths like "C:\Program Files..."

#### Git Intro

- Set up git: git config --global [user.name||user.email] "name/email in quotation marks"
- Clone repository: git clone https://github.com/Z3rp/AOO-Conversion-Script.git
- Update to latest version: git pull
- Making changes: git add [filename], then: git commit
- Update origin repository: git push
