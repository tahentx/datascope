import sys
import pandas as pd

program_command = sys.argv[1]

if program_command != "datascope":
    raise SystemExit("{} is not the command to initialize datascope. Please type {} before your other arguments.".format(program_command, "datascope"))

data_file = sys.argv[2]
user_dataframe = pd.read_csv(data_file)
if sys.argv[3] == "--shape":
    print("The dataset has {} rows, and {} columns".format(user_dataframe.shape[0], user_dataframe.shape[1]))

