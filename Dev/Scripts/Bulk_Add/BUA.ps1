$date = (get-date -format "yyyy-MM-dd_HHmmss") #date and time variable

$logfile = New-Item -Path ("$PSScriptRoot\..\..\Logs\Bulk_User_Add\$date.txt") -ItemType "file" #Creates and assigns a .txt file for logging with the date and time of script run

Import-Module activedirectory # Import active directory module for running AD cmdlets

$CSVname

$ADUsers = Import-csv -LiteralPath $CSVname #Store the data from the .csv in the $ADUsers variable

#Loop through each row containing user details in the CSV file 
foreach ($User in $ADUsers)
{
	#Read user data from each field in each row and assign the data to a variable as below
	$Firstname 	 = $User.Firstname
	$Lastname 	 = $User.Lastname
	$Username 	 = $Firstname + $Lastname -replace '[\W]', ''
	$Password 	 = $User.Password
	$OU 		 = $User.Path
    $Description = $User.Description
    $employeeID  = $User.edID
    $Group1      = $User.Group1
    $Group2      = $User.YearLevel #Group2
    $Group3      = $User.Group3
    $Group4      = $User.Group4
    $MemArr      = @($Username)
    $YL          = $User.YearLevel -replace 'Year ',''
    $driveLetter = $User.homeDrive
    $drivePath   = $User.homeDirectory -replace '%USERNAME%', $Username -replace '%X%', $YL

	#Check to see if the user already exists in AD
	if (Get-ADUser -F {SamAccountName -eq $Username}){
		#If user does exist, give a warning
		"10 - A user account with username $Username already exists in Active Directory." | Out-File -LiteralPath $logfile -Append
	}
	else{
		#User does not exist then proceed to create the new user account
		
        #Account will be created in the OU provided by the $OU variable read from the CSV file
		New-ADUser `
            -SamAccountName $Username `
            -UserPrincipalName "$Username@bps.internal" `
            -Name "$Firstname $Lastname" `
            -GivenName $Firstname `
            -Surname $Lastname `
            -Enabled $True `
            -DisplayName "$Firstname $Lastname " `
            -Path $OU `
            -Description $Description `
            -employeeID $employeeID `
            -AccountPassword (convertto-securestring $Password -AsPlainText -Force) -ChangePasswordAtLogon $False `
            -HomeDrive $driveLetter `
            -HomeDirectory $drivePath `

            "00 - $Username's Account succsesfully created" | Out-File -LiteralPath $logfile -Append

        #And add the new user to the Groups also read from the csv file
        if($Group1 -eq ''){
            "11 - No Supplied Group for Group1 of $Username" | Out-File -LiteralPath $logfile -Append
        }
        else{
            Add-AdGroupMember -Identity $Group1 -Members $MemArr[0] 
        }

        if($Group2 -eq ''){
            "11 - No Supplied Group for Group2 of $Username" | Out-File -LiteralPath $logfile -Append
        }
        else{
            Add-AdGroupMember -Identity $Group2 -Members $MemArr[0] 
        }

        if($Group3 -eq ''){
            "11 - No Supplied Group for Group3 of $Username" | Out-File -LiteralPath $logfile -Append
        }
        else{
            Add-AdGroupMember -Identity $Group3 -Members $MemArr[0] 
        }

        if($Group4 -eq ''){
            "11 - No Supplied Group for Group4 of $Username" | Out-File -LiteralPath $logfile -Append
        }
        else{
            Add-AdGroupMember -Identity $Group4 -Members $MemArr[0]
        }

	}
    
}