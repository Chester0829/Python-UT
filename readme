Install Python and setup
=====
1. Copy \\\\wsafile2\\MWSAShare\\YBI\\Test-Exes\\Chester\\XLA\\python-3.7.0.exe

2. Double Click to install it.

   >Attention: If you have no admin permission, it’s better to install software by way "Run Elevated"

3. Add system variable PYTHON_HOME= C:\Users\[local-user]\AppData\Local\Programs\Python\Python37-32

   >Variable name: PYTHON_HOME
   
   >Variable value: C:\Python37
   
   >Default location: C:\Users\tangqi\AppData\Local\Programs\Python\Python37-32
   
   How to add system variable?

   >Click Windows icon -> Right click Computer -> Select Properties -> Click Advance system settings on the right side → Click Environment Variables.

4. Append this value to existing system variable Path or PATH:

   > ;%PYTHON_HOME%;%PYTHON_HOME%\Scripts;

5. Reopen cmd window, run command to check if installation succeeds.

If view below result, it means success.

Add browser driver to system variable
=======
1.copy browser driver from \\wsafile2\MWSAShare\YBI\Test-Exes\Chester\BrowserDriver to local folder such as C:\Personal\BrowserDriver: 

2.add the folder to system variable

Install IDE and dependency package
=======
* Copy below text to a file, for example: C:\Personal\package.txt

   >certifi==2018.8.24
   
   >chardet==3.0.4
   
   >comtypes==1.1.7
   
   >ddt==1.2.1
   
   >et-xmlfile==1.0.1
   
   >idna==2.7
   
   >jdcal==1.4
   
   >opencv-python==4.1.1.26
   
   >openpyxl==2.5.11
   
   >Pillow==5.2.0
   
   >pyAutoGUI==0.9.47
   
   >pymssql==2.1.4
   
   >pytz==2018.7
   
   >pywin32==224
   
   >pywinauto==0.6.6
   
   >requests==2.19.1
    
   >selenium==3.141.0
   
   >six==1.11.0
   
   >urllib3==1.23
   
   
   

   Open cmd window, run command to install packages. (Note: If you stays in above screen about Python version info, you could press CTRL+Z to exit.)

   note: before running command, please close fiddler and change proxy to SFO

   >cd C:\Personal
   
   >pip install -r package.txt
   
note: if you still occurred errors , try to change the install resource,here I change to china resource
    >pip install -r package.txt -i http://pypi.douban.com/simple  --trusted-host pypi.douban.com

* install pycharm IDE

   >Download from \\\\wsafile2\\MWSAShare\\YBI\\Test-Exes\\Chester\\XLA\\pycharm-community-2018.2.4.exe

How to clone project to local
====
* insatll git 
    copy from :\\\\wsafile2\\MWSAShare\\YBI\\Test-Exes\\Chester\\XLA\\Git-2.19.1-64-bit.exe
* genarate ssh
* upload public ssh to github
  
    >FYI:http://contentwiki.moodys.com/display/SAV/Usage+of+GitHub

* open git bash and do git clone command: ***git clone git@github.com:moodysanalytics/CS-Structured-QA-Profectus-AT.git***
