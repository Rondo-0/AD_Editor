#The fuction is called in the AD-EDITOR.exe app, the fnbpr varible is passed from the .exe file, and is then assigned to the variable $CSVName
param($fnbpr) 
    $CSVname = $fnbpr

    copy-item -LiteralPath "$fnbpr"  -Destination "$PSScriptRoot\savedCSVs" # Copy the CSV to the savedCSVs folder 

    .$PSScriptRoot\BPR.ps1 $CSVname #Run the main script and push the $CSVname variable to it
