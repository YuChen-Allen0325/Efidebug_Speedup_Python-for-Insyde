import os
import linecache
from InfWriteLog import InfWriteLog as InfWL
from DecWriteLog import DecWriteLog as DecWL


        
        
# ------------------------ Create ClearlyDocument --------------------        

directory = input("please input your work directory path (ex: C:\ADL_N_Setup): ")
directory = str(directory)
Make_Sure_Execute_Flag = True
Change_ClrDoc_Flag = True        
Change_Line_Counter = 0
Repeat_GUID_Counter = 0
Change_Line_List = []
Change_Line_List_Contents = []
New_Putty_Str_list = []
Putty_Counter_list = []
Repeat_GUID_list = []
GUID_Occur_Dic = dict()
Repeat_GUID_Dic = dict()
extension_inf = ".inf"
extension_dec = ".dec"
exclude_dirs = ["Conf","BaseTools"]
Compare_with_Putty = ''
Compare_with_Putty_Left_Name = ''
New_Putty_Str = ''
Pure_GUID = ''
Confilt_GUID_Str = ''
Repeat_Specific_Line_Read = ''

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
                
                Change_Line_Counter_Putty = 0
                Change_ClrDoc_Flag = True
                ClrDoc_line_by_line_Str = str(ClrDoc_line_by_line)
                Compare_with_Putty = ClrDoc_line_by_line_Str[0:36]
                Compare_with_Putty_Left_Name = ClrDoc_line_by_line_Str[50:]
                
                with open((directory + "\putty.log"), 'r') as Putty:
                    for Putty_line_by_line in Putty:
                        if Compare_with_Putty in Putty_line_by_line:
                            Change_ClrDoc_Flag = False
                            New_Putty_Str = Putty_line_by_line[:]
                            Compare_with_Putty_Left_Name = Compare_with_Putty_Left_Name.replace(' ','')
                            New_Putty_Str = New_Putty_Str.replace(Compare_with_Putty, Compare_with_Putty_Left_Name)
                            New_Putty_Str = New_Putty_Str.replace('\n','')
                            Putty_Counter_list.append(Change_Line_Counter_Putty)
                            New_Putty_Str_list.append((New_Putty_Str+ '\n'))
                            
                        
                        Change_Line_Counter_Putty += 1
                
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
            
#------------------------- Conflict GUID Log --------------------------------

        with open((directory + "\ClearlyDocument.txt"), 'r') as ClrDoc:
            for ClrDoc_anyline in ClrDoc:
                
                ClrDoc_anyline = str(ClrDoc_anyline)
                
                if len(ClrDoc_anyline) > 37:
                    
                    Pure_GUID = ClrDoc_anyline[0:36]
                    
                    if Pure_GUID not in GUID_Occur_Dic.keys():
                        GUID_Occur_Dic[Pure_GUID] = []
                        GUID_Occur_Dic[Pure_GUID].append(Repeat_GUID_Counter)
                    else:
                        GUID_Occur_Dic[Pure_GUID].append(Repeat_GUID_Counter)
                        
                Repeat_GUID_Counter += 1

        Repeat_GUID_list = [Repeat_GUID for Repeat_GUID, occurtimes in GUID_Occur_Dic.items() if len(occurtimes) > 1]
        
        for All_GUID, occurtimes in GUID_Occur_Dic.items():
            for Repeat_GUID in Repeat_GUID_list:
                if All_GUID == Repeat_GUID:
                    Repeat_GUID_Dic[All_GUID] = occurtimes        
                

        for Repeat_GUID, Occurline in Repeat_GUID_Dic.items():
            
            Occurline_Counter = 1
            Repeat_GUID_Compare_Str = ''
            Last_Time_Compare_Str = ''
            
            for Unit_Occurline in Occurline:
                
                Repeat_Specific_Line_Read = linecache.getline((directory + "\ClearlyDocument.txt"), (Unit_Occurline + 1))
                Repeat_GUID_Compare_Str = str(Repeat_Specific_Line_Read[50:])
                Repeat_GUID_Compare_Str = Repeat_GUID_Compare_Str.replace(' ', '')
                Confilt_GUID_Str = str(Repeat_Specific_Line_Read[0:36])

                
                if (Occurline_Counter >= 2) and (Last_Time_Compare_Str != Repeat_GUID_Compare_Str):
                    with open((directory + "\Complict_GUID.txt"), 'a') as Cmplt_GUID:
                        Cmplt_GUID.write((Confilt_GUID_Str + '\n' + '\n'))
                    break
                
                Last_Time_Compare_Str = Repeat_GUID_Compare_Str
                
                Occurline_Counter += 1   
            
#------------------------- Putty Log Replace Word ----------------------------            

        with open((directory + "\putty.log"), 'r') as Putty:
            lines_putty = Putty.readlines()
        
        modified_lines_putty = {Putty_Counter_list[j]: New_Putty_Str_list[j] for j in range(len(Putty_Counter_list))}
        
        for line_number_putty, new_content_putty in modified_lines_putty.items():
            lines_putty[line_number_putty] = new_content_putty
            
        with open((directory + "\putty.log"), 'w') as Putty_Write:
            Putty_Write.writelines(lines_putty)    
            
except:
    pass

