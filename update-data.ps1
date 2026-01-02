# Read the ID mapping
$idMapping = Import-Csv "d:\codes\certificates\id.csv"

# Read the original data
$oldData = Get-Content "d:\codes\certificates\data.csv" -Encoding UTF8 | ConvertFrom-Csv

# Create new data structure
$newData = @{}

for ($i = 0; $i -lt $idMapping.Count; $i++) {
    $person = $oldData[$i]
    $newId = $idMapping[$i].ID
    
    $newData[$newId] = @{
        name = $person.'1. Full Name (as to be printed on certificate)'
        designation = $person.'2. Designation'
        department = $person.'  3. Department'
        college = $person.'  4. Name of the College'
        grade = $person.'grade obtained'
        course = "Machine Learning & Deep Learning"
        hours = "40"
        from = "06-10-2025"
        to = "27-10-2025"
        file = "assets/$newId.pdf"
    }
}

# Convert to JSON and save
$newData | ConvertTo-Json -Depth 10 | Set-Content "d:\codes\certificates\data.json" -Encoding UTF8

Write-Output "Updated data.json with $($newData.Count) certificates"
