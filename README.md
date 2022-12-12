# AD_Editor
A Python based tool. Used for bulk Windows Active Directory functions. With a Simple GUI

# SETUP

Edit your group policy with the following:

Set-Executionpolicy -scope "Local-Machine" -Executionpolicy "Bypass" or "Unrestricted" ##Preferably "Bypass"

#This allows running of .ps1 (powershell) scripts

Create a new registry key in the following path with parameters:

New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name "EnableLinkedConnections" -PropertyType "DWord" -Value "1"

#This allows administrator run applications to see and use mapped drives

# USAGE

ALWAYS run the app as administrator.

When selecting a CSV file, the file path must not have any spaces in it. Otherwise it will error
