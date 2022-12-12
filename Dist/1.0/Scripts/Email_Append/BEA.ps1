$date = (get-date -format "yyyy-MM-dd_HHmmss") #date and time variable

$logfile = New-Item -Path ("$PSScriptRoot\..\..\Logs\Bulk_Email_Append\$date.txt") -ItemType "file" #Creates and assigns a .txt file for logging with the date and time of script run

Import-Module activedirectory # Import active directory module for running AD cmdlets

$CSVname # Import active directory module for running AD cmdlets

$ADUsers = Import-csv -LiteralPath $CSVname #Store the data from the .csv in the $ADUsers variable

#Loop through each row containing user details in the CSV file 
foreach ($User in $ADUsers)
{
    #Read user data from each field in each row and assign the data to a variable as below
    $edID       = $User.edID
    $email      = $User.email

    if (Get-ADUser -Filter "EmployeeID -eq '$edID'"){

        Get-ADUser -Filter "EmployeeID -eq '$edID'" | Set-ADUser -Replace @{mail="$email"} 

            "00 - $edID's email successfully Replaced" | out-file -LiteralPath $logfile -Append
	}
	else{
            "10 - A user account with employeeID $edID does not exist in Active Directory." | out-file -LiteralPath $logfile -Append    
        }
}