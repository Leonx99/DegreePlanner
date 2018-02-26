# to execute this file from the interactive python shell use command 'exec(open('filepath').read())'
# note you will have to change the path variable below based on where it is located on your computer.
# I'm sorry it's hard coded, but the VS python interactive shell would always return the current directory and not the one I actually needed...
# despite working at the command line. If anyone can figure it out great.

import csv
import os
path = "C:\\Users\\parsh\\Documents\\DegreePlanner"
os.chdir(path)
from planner.models import Class
with open('CS_deg.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		p= Class(name=row['Name'], code=row['Code'], pre_req1=row['Pre1'], pre_req2=row['Pre2'], pre_req3=row['Pre3'], co_req=row['Co'])
		p.save()
		
exit()