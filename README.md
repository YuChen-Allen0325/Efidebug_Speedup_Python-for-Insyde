# User's Guide

The purpose of project is list all GUID and name in work directory and compare with "putty.log" to get real output. This saves a lot of time on searching

"putty.log = your_log_file_name"

".exe file is in the dist directory"

"work directory = root directory of Insyde code base"

"Some special GUID defined in c file are not listed and not replaced"

1. Path is your work directory (need absolute path)
2. You have to input your_log_file_name and extension, then you should put the file in your work directory
3. It may requires a few minute to execute
4. The new files created are called "ClearlyDocument", "Conflict_GUID", "new_your_log_file_name"
5. If the executed program is canceled suddenly. You may input error or you should rename your log file

In ClearlyDocument, If the line have both of GUID and name that you can find out in the your_log_file_name. If not, the GUID doesn't exist in the your_log_file_name

In ClearlyDocument, all of GUID in Insyde code base are listed


In Conflict_GUID, the file lists all that different name have same GUID

In new_your_log_file_name,all of GUID existed in the code base are replace correspond name 

Don't name your file to "ClearlyDocument" or "Conflict_GUID" before running "Efidebug_Speedup.exe", or there will be overlayed
