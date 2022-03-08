import os
import sys

def clr():
    # Enter the command 'cls', the system will clear all the outputs displayed on the screen
	command = 'clear'
	if os.name in ('nt', 'dos'):
		command = 'cls'
	os.system(command)

def changeDirectory():
    # Enter the command 'cd', the system will ask for the path of the new directory
    print("Enter new directory path")
    path = input(r'')
    try:
        os.chdir(path)
        print("Current working directory: {0}".format(os.getcwd()))
    except ValueError:
        print("Current working directory: {0}".format(os.getcwd()))
    except FileNotFoundError:
        print("Directory: {0} does not exist".format(path))
    except OSError:
        print("Current working directory: {0}".format(os.getcwd()))

def ListContent():
    # Enter the command 'dir' and enter the path to display the list of contents of the directory
	print("Enter the directory path")
	path = input(r'')
	contents = os.listdir(path)
	for file in os.listdir(path):
		print(file)
	return contents


def environ():
    # Enter the command 'Environ' to display the environment variables
	env = []
	for key, value in os.environ.items():
		print(f'{key}={value}')
		env.append(f'{key}={value}')
	return env

def echo(comment):
	print(f'{comment}\n')
	return f'{comment}'

def help():
	instructions = ['cd [dir] | change the current default directory to [dir]',
					'clr	| clear the screen',
					'dir [dir]| list the contents of directory [dir]',
					'environ	| list all environment variables',
					'echo [c]	| display the comment [c] followed by a newline',
					'help	| display a list of all commands in format [command] | [utility]',
					'pause	| pause operation of shell until Enter key is pressed',
					'quit	| quit the shell']
	for instruction in instructions:
		print(instruction)
	return instructions

def pause():
	wait = input()
	return

def quit():
	sys.exit()

def write_to_file(data, perm, dest):
	with open(dest, perm) as f:
		for d in data:
			f.write(f'{d}\n')
			
print("Welcome to the Command Line Interface designed by Vivek Satvik\nVivek Satvik Yeddula\nASU ID 122403382\nvyeddul1@asu.edu\n")
cwd = os.getcwd()
while True:
	bash = input(cwd + ">")
	cmds = bash.split()
	cmd = cmds[0]
	data = []
	output = -1
	permission = ''

	if '>' in cmds:
		output = cmds.index('>')
		permission = 'w'
	elif '>>' in cmds:
		output = cmds.index('>>')
		permission = 'a'

	if cmd == 'clr':
		clr()
	elif cmd == 'environ':
		data = environ()
	elif cmd == 'help':
		data = help()
	elif cmd == 'pause':
		pause()
	elif cmd == 'quit':
		break
	elif cmd == 'dir':
		data = ListContent()
	elif cmd == 'cd':
		changeDirectory()
	elif cmd == 'echo':
		comment = ' '.join(cmds[1:])
		if output != -1:
			comment = ' '.join(cmds[1:output])
		data = [echo(comment)]

	if output != -1:
		write_to_file(data, permission, cmds[output+1])
