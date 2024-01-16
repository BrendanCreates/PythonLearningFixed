# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy + copies metadata (file's creation and modification times

import shutil

shutil.copyfile("C:\\Users\\Brenb\\Desktop\\track.txt", "copy.txt") #src,dst source, destination
# this copies contents to a new file in the same directory with the specified name
# all of the copy methods use the same arguments