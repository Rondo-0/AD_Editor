#The fuction is called in the AD-EDITOR.exe app, the fnbea varible is passed from the .exe file, and is then assigned to the variable $CSVName
param($fnbea) 
    $CSVname = $fnbea

    copy-item -LiteralPath "$fnbea"  -Destination "$PSScriptRoot\savedCSVs" # Copy the CSV to the savedCSVs folder 

    .$PSScriptRoot\BEA.ps1 $CSVname #Run the main script and push the $CSVname variable to it
