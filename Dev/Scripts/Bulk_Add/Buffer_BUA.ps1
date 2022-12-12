#The fuction is called in the AD-EDITOR.exe app, the fnbua varible is passed from the .exe file, and is then assigned to the variable $CSVName
param($fnbua) 
    $CSVname = $fnbua

    copy-item -LiteralPath "$fnbua"  -Destination "$PSScriptRoot\savedCSVs" # Copy the CSV to the savedCSVs folder 

    .$PSScriptRoot\BUA.ps1 $CSVname #Run the main script and push the $CSVname variable to it
