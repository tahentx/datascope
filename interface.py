import sys

program_command = sys.argv[0]

if program_command != "datascope":
    raise SystemExit("{} is not the command to initialize datascope. Please type {} before your other arguments.".format(program_command, "datascope"))