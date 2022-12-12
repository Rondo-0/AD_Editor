$date = (get-date -format "yyyy-MM-dd_HHmmss") #date and time variable

$logfile = New-Item -Path ("$PSScriptRoot\..\..\Logs\Bulk_Computer_Add\$date.txt") -ItemType "file" #Creates and assigns a .txt file for logging with the date and time of script run

Import-Module activedirectory # Import active directory module for running AD cmdlets

$CSVname # Import active directory module for running AD cmdlets

$Computers = Import-csv -LiteralPath $CSVname #Store the data from the .csv in the $ADUsers variable

#Loop through each row containing computer details in the CSV file 
foreach ($Comp in $Computers)
{
	$name = $Comp.name
    $path = $Comp.path

	if (Get-ADcomputer -F {Name -eq $name}){

		"10 - A computer named $name already exists in Active Directory." | Out-File -LiteralPath $logfile -Append
	}
	else{

		New-ADcomputer -name "$name" -SAMAccountName "$name" -path $path
        "00 - Computer '$name' has been created in the path of $path." | Out-File -LiteralPath $logfile -Append
}
}
