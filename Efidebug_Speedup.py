import os
from InfWriteLog import InfWriteLog as InfWL
from DecWriteLog import DecWriteLog as DecWL


        
        
# ------------------------ Create ClearlyDocument --------------------        

directory = input("please input your work directory path (ex: C:\ADL_N_Setup): ")
directory = str(directory)
Make_Sure_Execute_Flag = True
Change_ClrDoc_Flag = True        
Change_Line_Counter = 0
Change_Line_List = []
Change_Line_List_Contents = []
extension_inf = ".inf"
extension_dec = ".dec"
exclude_dirs = ["Conf","BaseTools"]
Compare_with_Putty = ''


try:
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for filename in files:
            if filename.endswith(extension_inf):
                InfWL.InfWriteLog(os.path.join(root, filename), directory)
            if filename.endswith(extension_dec):
                DecWL.DecWriteLog(os.path.join(root, filename), directory)

except:
    Make_Sure_Execute_Flag = False            
            
# ------------------------ Compare Putty log ------------------------

try:
    if (Make_Sure_Execute_Flag == True):
        with open((directory + "\ClearlyDocument.txt"), 'r') as ClrDoc:
            for ClrDoc_line_by_line in ClrDoc:
                
                Change_ClrDoc_Flag = True
                ClrDoc_line_by_line_Str = str(ClrDoc_line_by_line)
                Compare_with_Putty = ClrDoc_line_by_line_Str[0:36]
                Compare_with_Putty = Compare_with_Putty.replace(' ', '')
                Compare_with_Putty = Compare_with_Putty.replace('#', '')

                
                with open((directory + "\putty.log"), 'r') as Putty:
                    for Putty_line_by_line in Putty:
                        if Compare_with_Putty in Putty_line_by_line:
                            Change_ClrDoc_Flag = False
                            break
                        
                        else:
                            Change_ClrDoc_Flag = True
                
                if Change_ClrDoc_Flag == True:
                    Change_Line_List.append(Change_Line_Counter)
                    Change_Line_List_Contents.append((Compare_with_Putty + '\n'))

                Change_Line_Counter += 1


        with open((directory + "\ClearlyDocument.txt"), 'r') as ClrDoc:
            lines = ClrDoc.readlines()

        modified_lines = {Change_Line_List[i]: Change_Line_List_Contents[i] for i in range(len(Change_Line_List))}
        
        for line_number, new_content in modified_lines.items():
            lines[line_number] = new_content        

        with open((directory + "\ClearlyDocument.txt"), 'w') as file:
            file.writelines(lines)
            
except:
    pass

