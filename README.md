## AOO-Conversion-Script

A script to convert the LINUX/UNIX AOO build system (modules) to a Windows based build system.

#### How to use

1. Choose a module to convert.
1. Enter module directory and delete the **wntmsci12.pro** directory.
2. Enter the main directory (contains all modules).
4. Create a text file called *moduleName*.txt in the module's directory.
5. Enter the **instsetoo_native** directory.
6. Execute and pipe the output to text file created in step 4:
  
  ```build --all:[moduleName] > ../[moduleName]/[moduleName].txt```
7. Wait until the module has been built: 
  1. Open the text file created in step 4. 
  2. Wait until the second occurrence of **Building module**. 
  3. Stop the process started in step 6.
  4. Delete everything after the second occurrence of **Building module**
8. Enter the main directory.
9. Run the vcGen.py script (format: ```python vcGen.py [moduleName]```).

Notes: Currently only handles calls to link, lib and cl.exe along with the version patching calls. Everything else will have to be done manually: this can be done by moving the output of the existing build system into a Cygwin script in order to handle parts that cannot be easily done on Windows.

##### Example
For this example assume:

Chosen module: rsc

Main directory path: C:\\steve\TestArea\main
```
cd C:\\steve\TestArea\main
rm -rf rsc/wntmsci12.pro
touch rsc/rsc.txt 
cd instsetoo_native
build --all:rsc > ../rsc/rsc.txt
Ctrl-Z
bg
tail -f ../rsc/rsc.txt
Ctrl-C (when the next Building Module shows)
fg
Ctrl-C
(open rsc.txt in an editor and delete everything after second Building module occurrence)
cd ..
python vcGen.py rsc
```

#### Manual Conversion
1. Open CygWin
2. Navigate to main directory.
3. Execute: ```source winenv.set.sh```
4. Enter the **instsetoo_native** directory.
5. Execute: ```build --all:[moduleName]``` (redirect output to a file, must manually cancel after script has built the module)
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
