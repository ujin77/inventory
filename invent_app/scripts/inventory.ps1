###
$SERVER = 'localhost:5000'
###
$REG_KEY = 'HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*'
$O_REG = (Get-ItemProperty $REG_KEY | select @{Name='Name'; Expression={$_.DisplayName}}, @{Name='Version'; Expression={$_.DisplayVersion}}, @{Name='Vendor'; Expression={$_.Publisher}})
$O_WMI = (Get-WmiObject -Class Win32_Product | select Name, Version, Vendor)
$SOFT = ($O_REG + $O_WMI | Sort-Object -Property Name | Select-Object -Property Name, Version, Vendor -Unique)
$INFO = (Get-ComputerInfo | Select  @{Label='Hostname'; Expression={$env:COMPUTERNAME}}, CsDNSHostName, CsDomain, WindowsProductName, WindowsInstallationType, WindowsEditionId, WindowsCurrentVersion, WindowsBuildLabEx)
$INFO | Add-Member -Name "PowerShell" -Value (Get-Host).Version -MemberType NoteProperty
$INFO | Add-Member -Name "Software" -Value $SOFT -MemberType NoteProperty
$JSON = ($INFO | ConvertTo-Json)

$uri = 'http://'+ $SERVER +'/inventory/api/v1.0/host'
$contentType = "application/json; charset=utf-8"
Invoke-RestMethod -Uri $uri -Method Post -ContentType $contentType -Body $JSON
