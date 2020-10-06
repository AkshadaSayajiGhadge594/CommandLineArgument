import sys

print("-----Python Programming Language--------");

print("Demonstration of Command Line Argument");

print("Application Name:"+sys.argv[0]);

x=int(sys.argv[1]);
print(x);

y=int(sys.argv[2]);
print(y);

z=x+y;

print(z);

##/////////////////////////////////////////////////
##  Command => python3 CommandLineArg.py 30 22
## OUTPUT :
##	-----Python Programming Language--------
##	Demonstration of Command Line Argument
##	Application Name:CommandLineArg.py
##	52
##////////////////////////////////////////////////
