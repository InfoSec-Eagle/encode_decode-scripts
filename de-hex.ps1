# Ask for user input
$hexInput = Read-Host -Prompt "Drop Hex here"

# Convert hex to bytes
$bytes = $hexInput.Split(' ') | ForEach-Object { [System.Convert]::ToByte($_, 16) }

# Convert bytes to string
$decodedStr = [System.Text.Encoding]::UTF8.GetString($bytes)

# Print the decoded string
Write-Output $decodedStr
