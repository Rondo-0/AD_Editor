$date = (get-date -format "yyyy-MM-dd_HHmmss") #date and time variable

$logfile = New-Item -Path ("$PSScriptRoot\..\..\Logs\Bulk_Password_Reset\$date.txt") -ItemType "file" #Creates and assigns a .txt file for logging with the date and time of script run

Import-Module activedirectory # Import active directory module for running AD cmdlets

$CSVname # Import active directory module for running AD cmdlets

$ADUsers = Import-csv -LiteralPath $CSVname #Store the data from the .csv in the $ADUsers variable

#Loop through each row containing user details in the CSV file 
foreach ($User in $ADUsers)
{
    #Read user data from each field in each row and assign the data to a variable as below
    $edID       = $User.edID    
    $Password 	= $User.password

    if (Get-ADUser -filter "EmployeeID -eq '$edID'"){

        Get-ADUser -filter "EmployeeID -eq '$edID'" | Set-ADAccountPassword -Reset -NewPassword (ConvertTo-SecureString -AsPlainText "$Password" -Force)

            "00 - $edID's password has been reset" | Out-file -LiteralPath $logfile -Append
    }   
    else{
            "10 - Error with $edID or user does not exist" | Out-File -LiteralPath $logfile -Append
        }	
}