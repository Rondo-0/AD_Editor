#The fuction is called in the AD-EDITOR.exe app, the fnbca varible is passed from the .exe file, and is then assigned to the variable $CSVName
param($fnbca) 
    $CSVname = $fnbca

    copy-item -LiteralPath "$fnbca"  -Destination "$PSScriptRoot\savedCSVs" # Copy the CSV to the savedCSVs folder 

    .$PSScriptRoot\BCA.ps1 $CSVname #Run the main script and push the $CSVname variable to it
