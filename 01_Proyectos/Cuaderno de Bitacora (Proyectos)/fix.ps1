$file1 = "c:\personal\Proyectos Antigravity\Proyecto Cuaderno de Bitacora\01_Proyectos\Cuaderno de Bitacora (Proyectos)\index.html"
$content = [System.IO.File]::ReadAllText($file1, [System.Text.Encoding]::UTF8)
$content = $content.Replace("Ã¡", "á").Replace("Ã©", "é").Replace("Ã³", "ó").Replace("Ãº", "ú").Replace("Ã±", "ñ").Replace("Ã ", "Á").Replace("Ã‰", "É").Replace("Ã“", "Ó").Replace("Ãš", "Ú").Replace("Ã‘", "Ñ").Replace("Ã­", "í").Replace("Ã³", "ó")
[System.IO.File]::WriteAllText($file1, $content, [System.Text.Encoding]::UTF8)

$file2 = "c:\personal\Proyectos Antigravity\Proyecto Cuaderno de Bitacora\01_Proyectos\Cuaderno de Bitacora (Proyectos)\perfil.html"
$content2 = [System.IO.File]::ReadAllText($file2, [System.Text.Encoding]::UTF8)
$content2 = $content2.Replace("Ã¡", "á").Replace("Ã©", "é").Replace("Ã³", "ó").Replace("Ãº", "ú").Replace("Ã±", "ñ").Replace("Ã ", "Á").Replace("Ã‰", "É").Replace("Ã“", "Ó").Replace("Ãš", "Ú").Replace("Ã‘", "Ñ").Replace("Ã­", "í").Replace("Ã³", "ó")
[System.IO.File]::WriteAllText($file2, $content2, [System.Text.Encoding]::UTF8)
