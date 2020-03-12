import os
import sys
file_name = sys.argv[1]

stream = os.popen('spatch --debug /home/keyur/PatchNetTool/preprocessing/extract_all_function.cocci --very-quiet ' + file_name)
output = stream.readlines()
if len(output) > 0:
    for line in output:
        if "," in line:
            data = line.rstrip()
            os.system("sed -i " + file_name + " -re '" + data + "{s/.*/ /}'")