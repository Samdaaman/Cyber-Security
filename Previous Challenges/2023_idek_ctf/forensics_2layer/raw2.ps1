function Encryption {
    [CmdletBinding()]
    [OutputType([string])]
    Param
    (
        [Parameter(Mandatory = $true, ParameterSetName = "CryptFile")]
        [String]$Path
    )

    Begin {
        $shaManaged = New-Object System.Security.Cryptography.SHA256Managed
        $aesManaged = New-Object System.Security.Cryptography.AesManaged
        $aesManaged.Mode = [System.Security.Cryptography.CipherMode]::CBC

        $aesManaged.Padding = [System.Security.Cryptography.PaddingMode]::Zeros
        $aesManaged.BlockSize = 128
        $aesManaged.KeySize = 256
    }

    Process {
        $aesManaged.Key = $shaManaged.ComputeHash([System.Text.Encoding]::UTF8.GetBytes('$encryptedBytes'))
                
        if ($Path) {
            $File = Get-Item -Path $Path -ErrorAction SilentlyContinue
            if (!$File.FullName) {

                Write-Error -Message "File not found!"
                break
            }
            $plainBytes = [System.IO.File]::ReadAllBytes($File.FullName)
            $outPath = $File.FullName + ".SOS"
        }

        $encryptor = $aesManaged.CreateEncryptor()
        $encryptedBytes = $encryptor.TransformFinalBlock($plainBytes, 0, $plainBytes.Length)
        $encryptedBytes = $aesManaged.IV + $encryptedBytes
        $aesManaged.Dispose()
                
        if ($Path) {
            [System.IO.File]::WriteAllBytes($outPath, $encryptedBytes)
            (Get-Item $outPath).LastWriteTime = $File.LastWriteTime
            return "File encrypted to $outPath"
        }
    }


    End {
        $shaManaged.Dispose()
        $aesManaged.Dispose()
    }
}