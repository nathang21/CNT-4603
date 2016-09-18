$HostName = $env:computername
$ScanInput = $args
Write-Host "`nThe following $ScanInput* services are currently running on: " -f red -nonewline; Write-Host "$HostName" -f darkblue 
get-service $ScanInput | format-table Name, DisplayName
Write-Host "List of Running Services Complete" -foregroundcolor "green"
Write-Host "Script terminating... " -foregroundcolor "red"