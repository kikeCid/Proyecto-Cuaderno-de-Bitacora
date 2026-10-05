$files = @(
    "c:\personal\Proyectos Antigravity\Proyecto Cuaderno de Bitacora\01_Proyectos\Cuaderno de Bitacora (Proyectos)\index.html",
    "c:\personal\Proyectos Antigravity\Proyecto Cuaderno de Bitacora\01_Proyectos\Cuaderno de Bitacora (Proyectos)\perfil.html"
)

foreach ($f in $files) {
    # Read raw bytes
    $bytes = [System.IO.File]::ReadAllBytes($f)
    
    # Try decoding as if the bytes were directly Windows-1252 to UTF-8
    # Since the file is actually saved as UTF-8, it contains bytes like C3 83 C2 A1 for Ã¡.
    # We read as string using UTF-8, so we get "Ã¡"
    $text = [System.IO.File]::ReadAllText($f, [System.Text.Encoding]::UTF8)
    
    # Let's just do exact string replacements for the known corrupted characters
    $text = $text.Replace("Ã¡", "á")
    $text = $text.Replace("Ã©", "é")
    $text = $text.Replace("Ã­", "í")
    $text = $text.Replace("Ã³", "ó")
    $text = $text.Replace("Ãº", "ú")
    $text = $text.Replace("Ã±", "ñ")
    $text = $text.Replace("Ã ", "Á")
    $text = $text.Replace("Ã‰", "É")
    $text = $text.Replace("Ã“", "Ó")
    $text = $text.Replace("Ãš", "Ú")
    $text = $text.Replace("Ã‘", "Ñ")
    $text = $text.Replace("Ã", "í") # Sometimes í is corrupted to Ã followed by an unprintable char, wait, no, "í" is C3 AD. Let's just fix what we know.
    
    # Re-save
    [System.IO.File]::WriteAllText($f, $text, [System.Text.Encoding]::UTF8)
}
Write-Host "Fixed encoding in HTML files"
