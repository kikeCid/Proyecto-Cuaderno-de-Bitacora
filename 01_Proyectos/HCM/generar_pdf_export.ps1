# ============================================================
# Generador de PDF Export Inteligente (Paginacion JS + Analisis)
# ============================================================
$ErrorActionPreference = 'Stop'
$base = $PSScriptRoot
$fecha = (Get-Date).ToString('dd/MM/yyyy')

# ── 1. REGLA DE ANALISIS DE CONTENIDO ──
# Esta funcion analiza si un HTML tiene informacion real o es solo una pasarela web (ej. hub/roadmap)
function Test-IsContentPage {
    param([string]$html)
    
    $m = [regex]::Match($html, '(?si)<main[^>]*>(.*?)</main>')
    if (!$m.Success) { return $false }
    $main = $m.Groups[1].Value
    
    # 1. Indicadores directos de bloques de contenido pesado
    if ($main -match 'class="[^"]*content-block[^"]*"') { return $true }
    if ($main -match 'class="[^"]*vendor-grid[^"]*"') { return $true }
    if ($main -match '(id|class)="[^"]*rfi-container[^"]*"') { return $true }
    if ($main -match '<table[^>]*>') { return $true } # Tablas grandes son contenido
    
    # 2. Heuristica para paginas de puro texto: contar parrafos que NO esten en hitos/tarjetas
    # Eliminamos virtualmente los roadmaps y carruseles para el conteo de parrafos
    $cleanMain = $main -replace '(?si)<div[^>]*class="[^"]*roadmap-container[^"]*"[\s\S]*', '' # Al ser lo ultimo de la pagina
    $cleanMain = $cleanMain -replace '(?si)<div[^>]*class="[^"]*carousel-track[^"]*"[^>]*>[\s\S]*?</div>', ''
    
    $pCount = ([regex]::Matches($cleanMain, '(?si)<p[> \n]')).Count
    if ($pCount -ge 3) { return $true }
    
    return $false
}

# Diccionario de Metadatos conocidos para el Indice
$dicMeta = @{
    'levantamiento_necesidad.html' = @{ t = 'Levantamiento de Necesidad'; s = 'Fase 1'; d = 'Analisis de obsolescencia PeopleSoft' }
    'estrategia_ecosistema.html'   = @{ t = 'Arquitectura y Ecosistema'; s = 'Fase 1'; d = 'Unificado vs Best-of-Breed' }
    'evaluacion_mercado.html'      = @{ t = 'Evaluacion de Mercado'; s = 'Fase 2'; d = 'Comparativa SAP, Oracle, Workday' }
    'vision_general.html'          = @{ t = 'Business Case'; s = 'Fase 2'; d = 'Analisis TCO y viabilidad' }
    'rfi_productos.html'           = @{ t = 'RFI Funcional'; s = 'Fase 3'; d = 'Alcance funcional y licencias' }
    'rfi_implantacion.html'        = @{ t = 'RFI Implantacion'; s = 'Fase 3'; d = 'Estrategia de despliegue' }
}

# ── 2. ESCANEO Y SELECCION DE PAGINAS ──
Write-Host "Analizando el directorio para descartar paginas de navegacion..." -ForegroundColor Cyan
$archivos = Get-ChildItem -Path $base -Filter "*.html" | Where-Object { $_.Name -notmatch "export_" -and $_.Name -ne "index.html" }
$paginasSelect = @()

foreach ($arch in $archivos) {
    if ($arch.Name -match "carrusel|mockup") { continue }
    $htmlRaw = [System.IO.File]::ReadAllText($arch.FullName, [System.Text.Encoding]::UTF8)
    
    if (Test-IsContentPage $htmlRaw) {
        $meta = if ($dicMeta.ContainsKey($arch.Name)) { $dicMeta[$arch.Name] } else { @{ t = $arch.Name.Replace('.html', ''); s = 'Documento'; d = 'Exportacion documental' } }
        $paginasSelect += @{ f = $arch.Name; t = $meta.t; s = $meta.s; d = $meta.d; html = $htmlRaw }
        Write-Host "  [X] INCLUIDA: $($arch.Name)" -ForegroundColor Green
    }
    else {
        Write-Host "  [-] EXCLUIDA (Solo Navegacion): $($arch.Name)" -ForegroundColor DarkGray
    }
}

$cssPath = Join-Path $base 'styles_hcm.css'
$originalCss = if (Test-Path $cssPath) { [System.IO.File]::ReadAllText($cssPath, [System.Text.Encoding]::UTF8) } else { '' }

# ── 3. CONSTRUCCION DE SECCIONES ──
$sectionsHtml = ''
for ($i = 0; $i -lt $paginasSelect.Count; $i++) {
    $p = $paginasSelect[$i]
    $html = $p.html
    
    # Extraer main
    $m = [regex]::Match($html, '<main[^>]*>([\s\S]*?)</main>', 'IgnoreCase,Singleline')
    $c = if ($m.Success) { $m.Groups[1].Value } else { '' }

    # Extraer estilos internos para no perder formato
    $sMs = [regex]::Matches($html, '<style[^>]*>([\s\S]*?)</style>', 'IgnoreCase,Singleline')
    $pageStyle = ''
    foreach ($sm in $sMs) { $pageStyle += $sm.Groups[1].Value }

    # LIMPIEZA ELEMENTOS UI WEB
    $c = $c -replace '(?si)<nav[\s\S]*?</nav>', ''
    $c = $c -replace '(?si)<footer[\s\S]*?</footer>', ''
    $c = $c -replace '(?si)<script[\s\S]*?</script>', ''
    $c = $c -replace '(?si)<div[^>]*class="[^"]*bg-mesh[^"]*"[^>]*>[^<]*</div>', ''
    $c = $c -replace '(?si)<div[^>]*class="[^"]*theme-toggle[^"]*"[^>]*>[\s\S]*?</div>', ''
    $c = $c -replace '(?si)<div[^>]*class="[^"]*export-fab[^"]*"[^>]*>[\s\S]*?</div>', ''

    # INYECCION PARA EL MOTOR JS (Marcar elementos atomicos protegidos)
    $c = $c -replace '(?i)<(p|h2|h3|h4|li|tr|th)( [^>]*)?>', '<$1 data-print="protect" $2>'
    $c = $c -replace 'class="([^"]*info-card[^"]*)"', 'class="$1" data-print="protect"'
    $c = $c -replace 'class="([^"]*alert-box[^"]*)"', 'class="$1" data-print="protect"'
    $c = $c -replace 'class="([^"]*metric[^"]*)"', 'class="$1" data-print="protect"'
    $c = $c -replace 'class="([^"]*vendor-header[^"]*)"', 'class="$1" data-print="protect"'
    $c = $c -replace 'class="([^"]*vendor-footer[^"]*)"', 'class="$1" data-print="protect"'
    $c = $c -replace 'class="([^"]*comparison-side[^"]*)"', 'class="$1" data-print="protect"'

    $num = $i + 1
    $sectionsHtml += '<div class="section-break"></div><div class="section-wrapper"><style>' + $pageStyle + '</style><div class="section-head" data-print="protect"><table class="section-head-table"><tr><td class="section-head-left"><div class="section-kicker">' + $p.s + ' &middot; Documento ' + $num + ' de ' + $paginasSelect.Count + '</div><div class="section-title">' + $p.t + '</div></td><td class="section-head-right"><div class="section-desc">' + $p.d + '</div></td></tr></table></div><div class="section-content">' + $c + '</div></div>'
}

# ── INDICE ──
$idxRows = ''
for ($i = 0; $i -lt $paginasSelect.Count; $i++) {
    $bgColor = if ($i % 2 -eq 0) { '#f8fafc' } else { 'white' }
    $idxRows += '<tr style="background:' + $bgColor + '"><td class="idx-num">' + ($i + 1) + '</td><td class="idx-title">' + $paginasSelect[$i].t + '</td><td class="idx-fase">' + $paginasSelect[$i].s + '</td><td class="idx-desc">' + $paginasSelect[$i].d + '</td></tr>'
}

# ── CLASES CSS DINAMICAS + MOTOR LÓGICO JS ──
$htmlOut = @"
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Dossier Evolucion HCM Cloud 2026</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800;900&display=swap" rel="stylesheet">
<style>
/* ================================================================
   ESTILOS DE DOCUMENTO PDF - FLOTANTES Y BLOQUES 100%
   ================================================================ */
@page { size: A4 landscape; margin: 18mm 20mm; }

*, *::before, *::after { box-sizing: border-box; }
body { font-family: 'Inter', sans-serif; color: #1e293b; line-height: 1.5; font-size: 10pt; background: white; -webkit-print-color-adjust: exact; print-color-adjust: exact; }

/* ── PORTADA ── */
.cover { height: 100vh; background: #0f172a; color: white; padding: 60px 70px; position: relative; }
.cover-top { margin-bottom: 50px; }
.cover-top-line { color: #E4002B; font-weight: 800; letter-spacing: 4px; font-size: 8pt; text-transform: uppercase; }
.cover-main h1 { font-size: 42pt; font-weight: 900; line-height: 1; letter-spacing: -2px; margin-bottom: 16px; }
.cover-main h1 span { color: #10B981; }
.cover-main p { font-size: 13pt; color: #94a3b8; max-width: 520px; line-height: 1.6; margin-bottom: 50px; }
.cover-meta-table td { padding-right: 50px; vertical-align: top; }
.cml { font-size: 7pt; color: #475569; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; display: block; margin-bottom: 3px; }
.cmv { font-size: 10pt; color: #e2e8f0; font-weight: 700; }
.cover-logo { position: absolute; bottom: 50px; right: 70px; font-size: 72pt; font-weight: 900; color: rgba(255,255,255,0.06); letter-spacing: -3px; }
.cover-logo span { color: rgba(228,0,43,0.2); }

/* ── INDICE ── */
.index-page { padding: 40px 0; }
.index-page h2 { font-size: 20pt; font-weight: 900; color: #0f172a; margin-bottom: 20px; }
.index-table { width: 100%; border-collapse: collapse; }
.index-table th { text-align: left; padding: 8px 12px; font-size: 7pt; color: #64748b; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; border-bottom: 2px solid #E4002B; }
.idx-num { width: 40px; text-align: center; font-weight: 900; color: #10B981; font-size: 11pt; padding: 14px 8px; }
.idx-title { font-weight: 800; color: #0f172a; font-size: 10pt; padding: 14px 12px; }

/* ── CABECERAS Y SALTOS ── */
.section-break { page-break-before: always; height: 1px; }
.section-head { border-bottom: 3px solid #E4002B; padding-bottom: 14px; margin-top: 40px; margin-bottom: 24px; }
.section-head-table { width: 100%; border-collapse: collapse; }
.section-head-right { text-align: right; vertical-align: bottom; width: 35%; }
.section-kicker { font-size: 7pt; font-weight: 800; letter-spacing: 2px; text-transform: uppercase; color: #10B981; margin-bottom: 4px; }
.section-title { font-size: 20pt; font-weight: 900; color: #0f172a; letter-spacing: -1px; margin: 0; }
.section-desc { font-size: 8.5pt; color: #94a3b8; font-style: italic; }

/* ── COMPONENTES WEB -> BLOQUES Y FLOTANTES (PRINT-SAFE) ── */
.container, .article-container { display: block !important; width: 100% !important; max-width: none !important; margin: 0 !important; padding: 0 !important; overflow: hidden !important; }

/* Formato general */
h1 { font-size: 16pt !important; font-weight: 900 !important; margin: 16px 0 8px !important; color: #0f172a !important; }
h2 { font-size: 14pt !important; font-weight: 800 !important; margin: 24px 0 10px !important; color: #0f172a !important; }
h3 { font-size: 11pt !important; font-weight: 700 !important; margin: 18px 0 6px !important; color: #334155 !important; }
p { margin-bottom: 10px !important; line-height: 1.6 !important; font-size: 9.5pt !important; }
ul, ol { margin: 6px 0 12px 20px !important; }
li { margin-bottom: 4px !important; font-size: 9.5pt !important; }

/* Tarjetas y Split Views con FLOAT */
.grid-cards, .comparison-split { display: block !important; width: 100% !important; overflow: hidden !important; margin-bottom: 20px !important; }
.info-card, .comparison-side {
    display: block !important; float: left !important;
    width: 48% !important; margin-right: 2% !important; margin-bottom: 20px !important;
    background: #f8fafc !important; border: 1px solid #e2e8f0 !important; padding: 16px !important;
}
.info-card h4 { font-size: 10pt !important; margin: 0 0 6px 0 !important; }
.comparison-side.unified { background: #f0fdf4 !important; border-color: #bbf7d0 !important; }
.comparison-side.niche { background: #fff1f2 !important; border-color: #fecdd3 !important; }
.comparison-side h3 { margin-top: 0 !important; font-size: 11pt !important; }

/* Vendor Cards = Bloques completos */
.vendor-grid { display: block !important; margin-bottom: 40px !important; }
.vendor-card {
    display: block !important; width: 100% !important;
    background: white !important; border: 2px solid #e2e8f0 !important;
    border-radius: 12px !important; padding: 25px !important; margin-bottom: 30px !important;
    position: static !important;
}
.vendor-header { border-bottom: 1px solid #e2e8f0 !important; padding-bottom: 15px !important; margin-bottom: 20px !important; }
.vendor-title { font-size: 16pt !important; font-weight: 900 !important; margin-left: 15px !important; display: inline-block !important; }
.metric-group { display: block !important; width: 100% !important; overflow: hidden !important; }
.metric { display: block !important; width: 33% !important; float: left !important; padding-right: 15px !important; margin-bottom: 15px !important; }
.vendor-footer { clear: both !important; background: #f8fafc !important; padding: 15px !important; border-top: 1px solid #e2e8f0 !important; margin-top: 20px !important; }

/* Alertas */
.alert-box { display: block !important; border-left: 4px solid #E4002B !important; background: #fff5f5 !important; border-radius: 4px !important; padding: 16px !important; margin-bottom: 16px !important; }
.alert-box h4 { margin: 0 0 6px 0 !important; color: #991b1b !important; font-size: 10pt !important; }

/* Ocultar redundantes (Hero banners ya estan en title) */
.hero, nav, footer, .bg-mesh, button { display: none !important; }

/* Limpiar flotantes global */
.clearfix::after, .doc-body::after, .section-content::after { content: ""; display: table; clear: both; }

/* ── CONTROLES WEB ── */
.toolbar { position: fixed; top: 0; left: 0; right: 0; height: 60px; background: #0f172a; display: flex; align-items: center; justify-content: space-between; padding: 0 30px; z-index: 9999; }
.toolbar-title { color: white; font-weight: 800; font-size: 11pt; }
.toolbar-title small { display: block; color: #64748b; font-size: 7.5pt; font-weight: 600; }
.btn-pdf { background: #E4002B; color: white; border: none; padding: 10px 24px; border-radius: 50px; font-weight: 900; cursor: pointer; font-family: inherit; }
.btn-back { background: transparent; color: #94a3b8; border: 1px solid #334155; padding: 10px 20px; border-radius: 50px; font-weight: 600; font-size: 9pt; cursor: pointer; font-family: inherit; }
.doc-body { max-width: 297mm; margin: 80px auto 40px; background: white; padding: 0; box-shadow: 0 0 40px rgba(0,0,0,0.15); }

@media print {
    body { margin: 0; }
    .toolbar { display: none !important; }
    .doc-body { max-width: none; margin: 0; box-shadow: none; }
}
</style>
</head>
<body>

<div class="toolbar no-print">
    <div><div class="toolbar-title">Dossier HCM Cloud <small>Generado Automaticamente</small></div></div>
    <div style="display:flex;gap:15px;"><button class="btn-back" onclick="window.history.back()">Volver</button><button class="btn-pdf" onclick="iniciarGuardadoPDF()">GUARDAR PDF PROTEGIDO</button></div>
</div>

<div class="doc-body">
    <div class="cover">
        <div class="cover-top"><div class="cover-top-line">MEMORIA CORPORATIVA 2026</div></div>
        <div class="cover-main"><h1>Evolucion<br><span>HCM Cloud</span></h1><p>Documento inteligente. Solo incorpora informacion de valor, descartando portales de navegacion web.</p></div>
        <table class="cover-meta-table"><tr><td><span class="cml">Proyecto</span><span class="cmv">HCM Cloud Evolution</span></td><td><span class="cml">Emision</span><span class="cmv">$fecha</span></td><td><span class="cml">Analizador</span><span class="cmv" style="color:#10B981;">Activo (Info Seleccionada)</span></td></tr></table>
        <div class="cover-logo">L<span>D</span>A</div>
    </div>
    
    <div class="index-page">
        <div class="section-kicker" style="margin-bottom:6px;">INDICE DE DOCUMENTOS SELECCIONADOS</div>
        <h2>Contenidos del Dossier</h2>
        <table class="index-table">
            <thead><tr><th style="width:40px">#</th><th>Documento Evaluado</th><th style="width:80px">Fase</th><th>Descripcion</th></tr></thead>
            <tbody>$idxRows</tbody>
        </table>
    </div>

    $sectionsHtml
</div>

<!-- ====================================================
     MOTOR JS DE PROTECCION CONTRA CORTES (PAGINACION)
     ==================================================== -->
<script>
function iniciarGuardadoPDF() {
    // Limpiar espaciadores viejos si hubieran
    document.querySelectorAll('.js-page-break').forEach(e => e.remove());
    
    // Configuracion
    const MM_A_PX = 3.7795275591;
    // A4 Landscape = 210mm alto. Margenes 18mm superior e inferior = 36mm
    // Area util = 174mm = ~657px
    const PAGE_HEIGHT = 657; 

    const bloques = document.querySelectorAll('[data-print="protect"]');
    
    bloques.forEach(bloque => {
        // Obtenemos su posicion vertical absoluta
        const rect = bloque.getBoundingClientRect();
        const top = rect.top + window.scrollY;
        const bottom = top + rect.height;
        
        const startPage = Math.floor(top / PAGE_HEIGHT);
        const endPage = Math.floor(bottom / PAGE_HEIGHT);
        
        // Si el bloque empieza en una pagina y termina en otra, Y cabe entero en una hoja:
        if (endPage > startPage && rect.height < (PAGE_HEIGHT * 0.9)) {
            const spacer = document.createElement('div');
            spacer.className = 'js-page-break';
            spacer.style.cssText = 'clear: both; display: block; height: 1px; width: 100%; page-break-before: always; break-before: page; margin:0; padding:0; background: transparent;';
            bloque.parentNode.insertBefore(spacer, bloque);
        }
    });

    // Pequeño retardo para dejar que el DOM se repinte con los saltos antes de imprimir
    setTimeout(() => {
        window.print();
    }, 300);
}
</script>

</body>
</html>
"@

$salida = Join-Path $base 'export_estatico.html'
[System.IO.File]::WriteAllText($salida, $htmlOut, [System.Text.Encoding]::UTF8)

Write-Host "✅ LOGICA DE FILTRADO COMPLETADA" -ForegroundColor Green
