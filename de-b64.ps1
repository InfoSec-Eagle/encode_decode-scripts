param (
    [string]$filePath
)

# Read the file content
$fileContent = Get-Content -Path $filePath

# Convert to bytes
$bytes = [System.Convert]::FromBase64String($fileContent)

# Convert bytes to string
$decodedStr = [System.Text.Encoding]::UTF8.GetString($bytes)

# Print the decoded string
Write-Output $decodedStr