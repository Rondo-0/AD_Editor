import PySimpleGUI as sg
import pandas as pd
import os, subprocess, sys
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()

sg.theme('BrownBlue')

########################################################################################################################### Welcome Window
Welcome  = [    

    [sg.Text("Please read the READ_ME.txt file for, setup information, using this tool and troubleshooting")],
    [sg.Text("Close this window to continue")]

            ]

########################################################################################################################### Column of cmds
Default_cmds =(
    sg.Column(  [
        
                [sg.Text("Please select a command")]
                
                ],
                vertical_alignment="bottom",justification="bottom",element_justification="left",key="default-cmds")
    )

Bulk_User_Add = (
    sg.Frame("Bulk User Add",
                [
                
                [sg.Button("Select CSV",key=("BUA-SELECT-CSV"), size=(20,1))],
                [sg.Button("Run",key=("BUA-RUN"), size=(20,1))]
                
                ],vertical_alignment="top",title_location = "n",element_justification="left",key="BUA-WINDOW",visible=False)
    )
    
Bulk_Pass =( 
    sg.Frame("Bulk Password Reset",  [
                
                [sg.Button("Select CSV",key=("BPR-SELECT-CSV"), size=(20,1))],
                [sg.Button("Run",key=("BPR-RUN"), size=(20,1))]
                
                ],vertical_alignment="top",title_location = "n",element_justification="left",key="BPR-WINDOW",visible=False)
    )

Bulk_CP =(
    sg.Frame("Bulk Computer Add",  [
        
                [sg.Button("Select CSV",key=("BCA-SELECT-CSV"), size=(20,1))],
                [sg.Button("Run",key=("BCA-RUN"), size=(20,1))]
                
                ],vertical_alignment="top",title_location = "n",element_justification="left",key="BCA-WINDOW",visible=False)
    )

Email_Append =( 
    sg.Frame("Bulk Email Append",  [
                
                [sg.Button("Select CSV",key=("BEA-SELECT-CSV"), size=(20,1))],
                [sg.Button("Run",key=("BEA-RUN"), size=(20,1))]
                
                ],vertical_alignment="top",title_location = "n",element_justification="left",key="BEA-WINDOW",visible=False)
    )

########################################################################################################################### Column of buttons
Left_List = [
    sg.Column(      [
                    
                    [sg.Button("Bulk User Add",key="BUA-OPEN", size =(20,1))],
                    [sg.Button("Bulk Password Reset",key="BPR", size =(20,1))],
                    [sg.Button("Bulk Computer Add",key="BCA", size =(20,1))],
                    [sg.Button("Email Append",key="EA", size =(20,1))]
                    
                    ],
                    vertical_alignment='top',justification="left",scrollable=True,vertical_scroll_only=True,size=(180,380))
]

########################################################################################################################### Creating the main window layout

Left_List_2 = [Default_cmds,Bulk_User_Add,Bulk_Pass,Bulk_CP,Email_Append]

Combine_Columns = sg.Column([Left_List,Left_List_2])

Layout = [ [Combine_Columns,sg.VSeperator()] ]


# sg.Button("Edit Script",key=("ES"), size=(21,1)),
# sg.Button('Exit',key=("Close_Main"))]


def main():
    global Left_List_2
    window = sg.Window("READ_ME", Welcome, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window = sg.Window('AD Editor',Layout,size = (700, 500))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit' or event == "Close_Main":
            break
        
        ################################################################################################################### Edit Script cmds
        if event == ("ES"):
            ESvar = askopenfilename(filetypes=[("","*.ps1")])
            if ESvar == "":
                nfs_window()
            else:
                os.system('start /D ' + ESvar +' powershell_ise')

        ################################################################################################################### Bulk User Add cmds
        if event == ("BUA-OPEN"):
            window[f'default-cmds'].update(visible=False)
            window[f'BUA-WINDOW'].update(visible=True)
            window[f'BPR-WINDOW'].update(visible=False)
            window[f'BCA-WINDOW'].update(visible=False)
            window[f'BEA-WINDOW'].update(visible=False)
            

        if event == ("BUA-SELECT-CSV"):
            try: 
                df,data, header_list,fn=read_table()
            except:
                continue
            show_prompt = sg.popup_yes_no('Show the dataset?')
            if show_prompt=='Yes':
                show_table(data,header_list,fn)
            fnbua = fn
            print("'"+fnbua+"'")
                                                                                #FIXING THIS THING
        if event == ("BUA-RUN"):
                try:
                    if getattr(sys, 'frozen', False):
                        absolute_path = os.path.dirname(sys.executable)
                    elif __file__:
                        absolute_path = os.path.dirname(__file__)

                    relative_path = "Scripts\Bulk_Add\Buffer_BUA.ps1"
                    full_path = os.path.join(absolute_path, relative_path)
                    full_path2 = "" + full_path +""
                    subprocess.call([ 'powershell.exe', '-File', "{0}".format(full_path2), (fnbua)])
                    
                except:
                    nfs_window()
                    continue
        ################################################################################################################### Bulk Password Reset cmds
        if event ==("BPR"):
            window[f'default-cmds'].update(visible=False)
            window[f'BUA-WINDOW'].update(visible=False)
            window[f'BPR-WINDOW'].update(visible=True)
            window[f'BCA-WINDOW'].update(visible=False)
            window[f'BEA-WINDOW'].update(visible=False)
          
        if event == ("BPR-SELECT-CSV"):
            try: 
                df,data, header_list,fn=read_table()
            except:
                continue
            show_prompt = sg.popup_yes_no('Show the dataset?')
            if show_prompt=='Yes':
                show_table(data,header_list,fn)
            fnbpr = fn
            print ("'"+fnbpr+"'")

        if event == ("BPR-RUN"):
                try:
                    if getattr(sys, 'frozen', False):
                        absolute_path = os.path.dirname(sys.executable)
                    elif __file__:
                        absolute_path = os.path.dirname(__file__)

                    relative_path = "Scripts\Password_Reset\Buffer_BPR.ps1"
                    full_path = os.path.join(absolute_path, relative_path)
                    full_path2 = "" + full_path +""
                    subprocess.call([ 'powershell.exe', '-File', "{0}".format(full_path2), (fnbpr)])
                except:
                    nfs_window()
                    continue
        ################################################################################################################### Bulk Computer Add cmds
        if event ==("BCA"):
            window[f'default-cmds'].update(visible=False)
            window[f'BUA-WINDOW'].update(visible=False)
            window[f'BPR-WINDOW'].update(visible=False)
            window[f'BCA-WINDOW'].update(visible=True)
            window[f'BEA-WINDOW'].update(visible=False)
          
        if event == ("BCA-SELECT-CSV"):
            try: 
                df,data, header_list,fn=read_table()
            except:
                continue
            show_prompt = sg.popup_yes_no('Show the dataset?')
            if show_prompt=='Yes':
                show_table(data,header_list,fn)
            fnbca = fn
            print ("'"+fnbca+"'")

        if event == ("BCA-RUN"):
                try:
                    if getattr(sys, 'frozen', False):
                        absolute_path = os.path.dirname(sys.executable)
                    elif __file__:
                        absolute_path = os.path.dirname(__file__)

                    relative_path = "Scripts\Bulk_Computer_add\Buffer_BCA.ps1"
                    full_path = os.path.join(absolute_path, relative_path)
                    full_path2 = "" + full_path +""
                    subprocess.call([ 'powershell.exe', '-File', "{0}".format(full_path2), (fnbca)])
                except:
                    nfs_window()
                    continue
        ################################################################################################################### Bulk Email Append cmds
        if event ==("EA"):
            window[f'default-cmds'].update(visible=False)
            window[f'BUA-WINDOW'].update(visible=False)
            window[f'BPR-WINDOW'].update(visible=False)
            window[f'BCA-WINDOW'].update(visible=False)
            window[f'BEA-WINDOW'].update(visible=True)
          
        if event == ("BEA-SELECT-CSV"):
            try: 
                df,data, header_list,fn=read_table()
            except:
                continue
            show_prompt = sg.popup_yes_no('Show the dataset?')
            if show_prompt=='Yes':
                show_table(data,header_list,fn)
            fnbea = fn
            print ("'"+fnbea+"'")

        if event == ("BEA-RUN"):
                try:
                    if getattr(sys, 'frozen', False):
                        absolute_path = os.path.dirname(sys.executable)
                    elif __file__:
                        absolute_path = os.path.dirname(__file__)

                    relative_path = "Scripts\Email_Append\Buffer_BEA.ps1"
                    full_path = os.path.join(absolute_path, relative_path)
                    full_path2 = "" + full_path +""
                    subprocess.call([ 'powershell.exe', '-File', "{0}".format(full_path2), (fnbea)])
                except:
                    nfs_window()
                    continue
        ###################################################################################################################
    
    window.close()

def read_table():

    sg.set_options(auto_size_buttons=True)
    filename = askopenfilename(filetypes=[("","*.csv")])
    print(filename)
    # --- populate table with file contents --- #
    if filename == '':
        nfs_window()
        return
    else:
        data = []
        header_list = []
        colnames_prompt = sg.popup_yes_no('Does this file have column headers?')

        if filename is not None:
            fn = filename
            try:                     
                if colnames_prompt == 'Yes':
                    df = pd.read_csv(filename, sep=',', engine='python')
                    # Uses the first row (which should be column names) as columns names
                    header_list = list(df.columns)
                    # Drops the first row in the table (otherwise the header names and the first row will be the same)
                    data = df[0:].values.tolist()
                else:
                    df = pd.read_csv(filename, sep=',', engine='python', header=None)
                    # Creates columns names for each column ('column0', 'column1', etc)
                    header_list = ['column' + str(x) for x in range(len(df.iloc[0]))]
                    df.columns = header_list
                    # read everything else into a list of rows
                    data = df.values.tolist()

                return (df,data, header_list,fn)
            except:
                sg.popup_error('Error reading file')          

def show_table(data, header_list, fn):
    layout = [
        [sg.Table(values=data,
                  headings=header_list,
                  font='Helvetica',
                  pad=(25,25),
                  display_row_numbers=False,
                  auto_size_columns=True,
                  num_rows=min(25, len(data)))]
    ]

    window = sg.Window(fn, layout, grab_anywhere=False, modal=True)
    event, values = window.read()
    window.close()

def nfs_window():
    error_nofile = [ [sg.Text("No File Selected")],
                        [sg.Button("Ok", key= "Close NFS Window")]
                    ]
    window = sg.Window("No File Selected", error_nofile, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED or event == "Close NFS Window":
            break

    window.close()

if __name__ == "__main__":
    main()