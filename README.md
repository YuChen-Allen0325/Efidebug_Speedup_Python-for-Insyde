# User's Guide

The purpose of project is list all GUID and name in work directory and compare with "putty.log" to get real output. This saves a lot of time on searching

".exe file is in the dist directory"

"work directory = root directory of Insyde code base"

1. Your "putty.log" cannot be renamed as another name ,and then you should put the file in your work directory
2. It may require a few minute to execute
3. Path is your work directory (need absolute path)
4. The new files created are called "ClearlyDocument", "Complict_GUID"

In ClearlyDocument, If the line have both of GUID and name that you can find out in the "putty.log". If not, the GUID doesn't exist in the "putty.log"
In the "putty.log" ,all of GUID existed in the code base are replace correspond name 
In Complict_GUID, the file lists all that different name have same GUID
