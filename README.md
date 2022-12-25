This goal of this project is to do some automatic function tests on Windows calculator function.

Python unittest library and WinAppDriver are tools used in this project.

test_converter.py is for testing converter function in the calculator.
test_programmer.py is for testing programmer calculator function in the calculator.
test_strandard.py is for testing standard calculator in the calculator.

Target testing calculator is in a Windows 10 virtual machine with WinAppDriver installed. The IP address and port number for WinAppDriver is 192.168.1.157 4723. 

System and tool	version: 
Windows 10 Enterprise 20H2
Calculator 10.2103.8.0
WinAppDriver	1.2.1

There are 4-5 test cases for each function.
There are 500 test cases in total.

Test cases give input values and read output values automatically. Then it determines the result is correct or not. 
