# -*- coding: utf-8 -*-
"""
Script maestro para aplicar la identidad de marketing de Línea Directa (coches.lineadirecta.com):
1. Logo oficial de Línea Directa en la cabecera (Executive Island) y en el Footer.
2. Iconos vectoriales de trazo fino idéntico a Perseo (fill-rule='evenodd' oficial de Línea Directa):
   - Perseo: poliza-coche.svg (coche oficial Línea Directa).
   - Reingeniería de Siniestros: taller.svg (llave inglesa de taller, siniestros y reparaciones oficial de Línea Directa).
   - Telefonía Genesys CX: contacto-telefonico-alt.svg (teléfono icónico oficial de Línea Directa).
   - Eficiencia RRHH & Asistente IA: asistencias-informatica.svg (pantalla e innovación digital de Línea Directa).
   - Evolución HCM Cloud: silueta de personas corporativas en trazo fino.
   - CRM Operacional: ficha 360° del asegurado en trazo fino.
   - Gestión de Usuarios: poliza-otros-seguros-1.svg (escudo oficial de seguridad y garantía de Línea Directa).
   - Gestión de la Información: libro/wiki funcional de conocimiento en trazo fino.
3. Paleta oficial coches.lineadirecta.com:
   - Rojo corporativo: #CC3333
   - Superficies: #1A1A1A (texto) y #F7F7F7 (fondo página)
   - Tarjetas: #FFFFFF con borde 1px rgba(26,26,26,0.08) y sombra sutil
   - Tipografía: 'CircularXX', 'Inter', -apple-system, sans-serif
4. Sincronización en bitacora-core.css y styles_bitacora.css.
"""

import os
import re
import subprocess

BASE_DIR = r"C:\Proyectos_Claude\Proyecto Cuaderno de Bitacora"
INDEX_HTML = os.path.join(BASE_DIR, "01_Proyectos", "Cuaderno de Bitacora (Proyectos)", "index.html")
CORE_BUILDER = os.path.join(BASE_DIR, "scratch", "build_unified_core_css.py")
ASSETS_IMG = os.path.join(BASE_DIR, "01_Proyectos", "assets", "img")

# ==============================================================================
# 1. ICONOS OFICIALES DE LÍNEA DIRECTA CON TRAZO FINO Y RELACIÓN PRECISA
# ==============================================================================

# PERSEO: Silueta oficial del coche Línea Directa (poliza-coche.svg)
svg_perseo = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M23.3028 10.4393C24.0192 11.1306 24.1525 12.0989 23.842 13.1148C23.8346 13.1391 23.8272 13.1632 23.82 13.187C23.4558 14.379 23.2649 15.0039 22.6436 15.6816C22.3129 16.0423 21.971 16.2336 21.6974 16.3331C21.5618 16.3824 21.445 16.4084 21.3569 16.4222C21.3128 16.429 21.2758 16.4328 21.2471 16.4349C21.2327 16.436 21.2203 16.4366 21.2102 16.437L21.1966 16.4373L21.191 16.4374L21.1886 16.4374L21.1874 16.4374C21.1874 16.4374 21.1863 16.4374 21.1863 15.9374V16.4374H20.4999C20.2238 16.4374 19.9999 16.2136 19.9999 15.9374C19.9999 15.6613 20.2238 15.4374 20.4999 15.4374H21.1765C21.1809 15.437 21.1899 15.4361 21.2029 15.4341C21.2339 15.4293 21.2872 15.4182 21.3557 15.3933C21.4904 15.3443 21.6929 15.2388 21.9066 15.0058C22.3616 14.5095 22.4945 14.1024 22.8857 12.8225C23.1196 12.0571 22.9807 11.5182 22.6084 11.1589C22.203 10.7678 21.4111 10.4778 20.106 10.4998L20.0976 10.5L12.4763 10.4999C12.2001 10.4999 11.9763 10.2761 11.9763 9.99991C11.9763 9.72377 12.2001 9.49991 12.4763 9.49991H20.0934C21.5082 9.4767 22.6201 9.78057 23.3028 10.4393Z" fill="currentColor"/>
    <path fill-rule="evenodd" clip-rule="evenodd" d="M8.48496 6C8.48815 6 8.49133 6 8.49449 6H11.5188C12.76 6 13.9695 6.40098 14.9945 7.14631L17.4252 8.91371C17.43 8.91726 17.4349 8.9209 17.4396 8.92463L17.4426 8.92689C17.4467 8.92998 17.4539 8.93534 17.4639 8.94265C17.4841 8.95728 17.5158 8.9796 17.5575 9.00707C17.6413 9.06224 17.7636 9.13687 17.9135 9.21151C18.2197 9.36407 18.6074 9.5 18.9999 9.5C19.276 9.5 19.4999 9.72386 19.4999 10C19.4999 10.2761 19.276 10.5 18.9999 10.5C18.3923 10.5 17.8457 10.295 17.4675 10.1066C17.2752 10.0108 17.1179 9.91492 17.0075 9.84223C16.9521 9.80577 16.9081 9.77481 16.8768 9.75215C16.8612 9.74082 16.8487 9.73152 16.8396 9.72463L16.8318 9.71865L14.4064 7.95511C13.547 7.33021 12.5423 7 11.5188 7H8.49987C8.09239 7 7.53365 7.00117 6.84163 7.22561C6.15143 7.44946 5.3018 7.90518 4.35343 8.85355L4 8.50012C4.35343 8.85355 4.35343 8.85355 4.35343 8.85355L4.35271 8.85427L4.35195 8.85502L4.35029 8.85667L4.34638 8.86048L4.33623 8.87016C4.32841 8.87751 4.31846 8.88662 4.30627 8.89738C4.28188 8.9189 4.24854 8.94697 4.20528 8.98061C4.11874 9.04793 3.99272 9.13739 3.81962 9.24125C3.47333 9.44902 2.93983 9.73943 2.15812 10C1.43268 10.2418 1.20712 10.444 1.11625 10.5954C1.01426 10.7654 1.00001 10.984 1.00001 11.5257C1.00001 11.8477 1.14586 12.5322 1.35786 13.3209C1.5631 14.0844 1.81007 14.8747 1.97435 15.3675C2.06167 15.6295 1.92009 15.9127 1.65812 16C1.39615 16.0873 1.11299 15.9457 1.02566 15.6838C0.856605 15.1766 0.603573 14.367 0.392147 13.5805C0.18748 12.8191 5.34415e-06 12.0036 5.34415e-06 11.5257C5.34415e-06 11.5041 -2.60675e-05 11.4825 -5.77176e-05 11.4606C-0.000699898 11.0176 -0.00142887 10.5146 0.258759 10.0809C0.542886 9.60736 1.06733 9.30951 1.84189 9.05132C2.56018 8.81189 3.02642 8.55098 3.30513 8.38375C3.44452 8.30011 3.53726 8.23332 3.59134 8.19126C3.6184 8.17022 3.63583 8.15532 3.64465 8.14754L3.65055 8.14222C4.70059 7.09336 5.6828 6.55017 6.53312 6.27439C7.29567 6.02707 7.93065 6.00267 8.36067 6.00026C8.3661 6.00009 8.37155 6 8.37703 6H8.48496Z" fill="currentColor"/>
    <path fill-rule="evenodd" clip-rule="evenodd" d="M8.49994 16C8.49994 15.7239 8.7238 15.5 8.99994 15.5H14.9999C15.2761 15.5 15.4999 15.7239 15.4999 16C15.4999 16.2762 15.2761 16.5 14.9999 16.5H8.99994C8.7238 16.5 8.49994 16.2762 8.49994 16Z" fill="currentColor"/>
    <path fill-rule="evenodd" clip-rule="evenodd" d="M6.24994 13.5C5.0073 13.5 3.99994 14.5074 3.99994 15.75C3.99994 16.9926 5.0073 18 6.24994 18C7.49258 18 8.49994 16.9926 8.49994 15.75C8.49994 14.5074 7.49258 13.5 6.24994 13.5ZM2.99994 15.75C2.99994 13.9551 4.45502 12.5 6.24994 12.5C8.04487 12.5 9.49994 13.9551 9.49994 15.75C9.49994 17.5449 8.04487 19 6.24994 19C4.45502 19 2.99994 17.5449 2.99994 15.75Z" fill="currentColor"/>
    <path fill-rule="evenodd" clip-rule="evenodd" d="M17.7499 13.5C16.5073 13.5 15.4999 14.5074 15.4999 15.75C15.4999 16.9926 16.5073 18 17.7499 18C18.9926 18 19.9999 16.9926 19.9999 15.75C19.9999 14.5074 18.9926 13.5 17.7499 13.5ZM14.4999 15.75C14.4999 13.9551 15.955 12.5 17.7499 12.5C19.5449 12.5 20.9999 13.9551 20.9999 15.75C20.9999 17.5449 19.5449 19 17.7499 19C15.955 19 14.4999 17.5449 14.4999 15.75Z" fill="currentColor"/>
</svg>"""

# REINGENIERÍA DE SINIESTROS: Llave de taller, reparación y peritación oficial (taller.svg de coches.lineadirecta.com)
svg_siniestros = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M11.5257 3.21912C10.0457 1.73837 7.98611 1.2216 6.09131 1.64016L6.07779 1.64315L6.07783 1.64334C5.45913 1.7981 5.27829 2.5687 5.7102 3.00085L8.43236 5.72455L8.10143 8.10508L5.7228 8.43612L3.0008 5.71258C2.56837 5.2799 1.79788 5.46173 1.64335 6.08022L1.63999 6.09365L1.64018 6.09369C1.22192 7.98923 1.73827 10.0498 3.21814 11.5305C3.23966 11.5521 3.26295 11.5714 3.28765 11.5885C4.54142 12.8188 6.23891 13.366 7.84194 13.2323C9.15172 13.1231 10.4687 13.7193 11.4498 14.7009L18.5623 21.8174C18.5628 21.8179 18.5633 21.8184 18.5638 21.8189C19.46 22.7285 20.9157 22.7244 21.8195 21.8217C22.7271 20.9263 22.7243 19.375 21.8263 18.4702L20.5457 17.1115C20.3563 16.9106 20.0398 16.9012 19.8389 17.0906C19.6379 17.28 19.6286 17.5965 19.818 17.7974L21.1033 19.1611L21.1135 19.1716C21.6304 19.6887 21.6263 20.6085 21.1164 21.1106L21.1136 21.1134C20.5969 21.6304 19.7769 21.6263 19.2753 21.1162L19.2725 21.1134L19.2724 21.1134L12.1571 13.994C11.0183 12.8545 9.42601 12.0968 7.75885 12.2358C6.41064 12.3482 4.97954 11.8772 3.93845 10.8253C3.91755 10.8042 3.89497 10.7852 3.87102 10.7683C2.77896 9.64112 2.34267 8.12508 2.55003 6.67617L5.19149 9.31912C5.30233 9.43002 5.45877 9.48251 5.61407 9.4609L8.61355 9.04344C8.83501 9.01262 9.00908 8.83852 9.03987 8.61706L9.45709 5.61588C9.47866 5.4607 9.42625 5.30439 9.31551 5.19358L6.67341 2.54999C8.14515 2.33902 9.68633 2.79337 10.8183 3.92602C11.871 4.97926 12.3321 6.37971 12.2295 7.75509C12.1038 9.44091 12.8465 11.01 13.987 12.1511L13.9972 12.161L16.4185 14.449C16.6192 14.6387 16.9357 14.6297 17.1253 14.429C17.315 14.2283 17.306 13.9118 17.1053 13.7222L14.6893 11.4392C13.7128 10.4598 13.1271 9.16514 13.2267 7.82946C13.3497 6.18109 12.7959 4.4901 11.5257 3.21912Z" fill="currentColor"/>
</svg>"""

# TELEFONÍA GENESYS CX: Teléfono oficial de contacto de Línea Directa (contacto-telefonico-alt.svg)
svg_telefonia = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M19.988 22.5C19.8876 22.5 19.7871 22.5 19.7871 22.5C16.6722 22.1986 13.5574 21.0933 10.8445 19.3852C8.33254 17.7775 6.22249 15.6675 4.71531 13.1555C2.9067 10.5431 1.90191 7.42823 1.5 4.21292C1.5 3.61005 1.70096 2.9067 2.10287 2.40431C2.50479 1.90191 3.10765 1.60048 3.811 1.5C3.91148 1.5 3.91148 1.5 4.01196 1.5H7.02632C8.23206 1.5 9.33732 2.40431 9.53828 3.71053C9.63876 4.61483 9.83971 5.51914 10.2416 6.42345C10.5431 7.32775 10.3421 8.33254 9.63876 9.03589L8.63397 10.0407C9.94019 12.2512 11.7488 14.0598 13.9593 15.366L14.9641 14.3612C15.6675 13.6579 16.6722 13.4569 17.5766 13.7584C18.4809 14.0598 19.3852 14.3612 20.2895 14.4617C21.5957 14.6627 22.5 15.7679 22.5 16.9737V19.988C22.5 20.6914 22.1986 21.2943 21.7966 21.7967C21.2943 22.299 20.6914 22.5 19.988 22.5ZM7.02632 2.50478H4.01196H3.91148C3.50957 2.50478 3.10766 2.70574 2.9067 3.00718C2.60526 3.30861 2.50478 3.71053 2.50478 4.11244C2.80622 7.12679 3.91148 10.0407 5.51914 12.5526C7.02632 14.8636 9.03588 16.9737 11.3469 18.4809C13.8589 20.0885 16.7727 21.1938 19.7871 21.4952H19.8876C20.2895 21.4952 20.6914 21.2943 20.9928 21.0933C21.2943 20.7919 21.3947 20.39 21.3947 19.988V16.9737C21.3947 16.1699 20.8923 15.567 20.0885 15.4665C19.0837 15.366 18.0789 15.0646 17.1746 14.7632C16.6722 14.5622 15.9689 14.6627 15.567 15.0646L14.2608 16.3708C14.0598 16.5718 13.8589 16.5718 13.6579 16.4713C11.0455 14.9641 8.93541 12.8541 7.42823 10.2416C7.42823 10.0407 7.52871 9.73923 7.62919 9.63876L8.93541 8.33254C9.33732 7.93062 9.4378 7.32775 9.23684 6.72488C8.93541 5.82057 8.63397 4.81579 8.53349 3.81101C8.43301 3.10766 7.83014 2.50478 7.02632 2.50478Z" fill="currentColor"/>
</svg>"""

# EFICIENCIA RRHH & IA (LidIA): Asistencia informática e innovación inteligente (asistencias-informatica.svg)
svg_ia = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M5.64733 2.49976C4.57577 2.49976 3.71762 3.3562 3.71762 4.39976V13.723C3.73469 13.7223 3.75182 13.722 3.76901 13.722H20.5355V8.11086C20.5355 7.83472 20.7593 7.61086 21.0355 7.61086C21.3116 7.61086 21.5355 7.83472 21.5355 8.11086V14.1518L22.8691 18.8089C23.4015 20.6681 21.9859 22.4997 20.0504 22.4997H4.20274C2.26724 22.4997 0.85167 20.6681 1.38408 18.8089L2.58693 14.6084C2.61866 14.4976 2.66509 14.3943 2.7237 14.3002C2.7197 14.2747 2.71762 14.2486 2.71762 14.222V4.39976C2.71762 2.79235 4.03512 1.49976 5.64733 1.49976H12.1265C12.4027 1.49976 12.6265 1.72361 12.6265 1.99976C12.6265 2.2759 12.4027 2.49976 12.1265 2.49976H5.64733ZM20.6586 14.722H3.76901C3.6624 14.722 3.57466 14.7916 3.54829 14.8837L2.34544 19.0842C2.00059 20.2885 2.91509 21.4997 4.20274 21.4997H20.0504C21.3381 21.4997 22.2526 20.2885 21.9077 19.0842L20.6586 14.722ZM10.6142 18.9997C10.6142 18.7236 10.8381 18.4997 11.1142 18.4997H13.139C13.4151 18.4997 13.639 18.7236 13.639 18.9997C13.639 19.2759 13.4151 19.4997 13.139 19.4997H11.1142C10.8381 19.4997 10.6142 19.2759 10.6142 18.9997Z" fill="currentColor"/>
    <path fill-rule="evenodd" clip-rule="evenodd" d="M16.46 2.37882C16.1962 2.61692 16 2.98673 16 3.53051C16 3.80665 15.7761 4.03051 15.5 4.03051C15.2239 4.03051 15 3.80665 15 3.53051C15 2.72062 15.3038 2.07518 15.79 1.63643C16.2676 1.20548 16.8914 1 17.5 1C18.1086 1 18.7325 1.20548 19.21 1.63643C19.6962 2.07518 20 2.72062 20 3.53051C20 4.10154 19.8633 4.53753 19.6448 4.90205C19.458 5.21379 19.2148 5.46259 19.0134 5.66862C18.9917 5.69081 18.9705 5.7125 18.9499 5.73372C18.7263 5.96405 18.5451 6.16498 18.4112 6.4264C18.281 6.68059 18.1822 7.02016 18.1822 7.5305C18.1822 7.80664 17.9583 8.0305 17.6822 8.0305C17.406 8.0305 17.1822 7.80664 17.1822 7.5305C17.1822 6.88054 17.3106 6.3817 17.5212 5.97049C17.7281 5.56652 18.0014 5.27509 18.2323 5.03722C18.2513 5.0176 18.27 4.99844 18.2883 4.97968C18.5026 4.75939 18.6637 4.59383 18.7871 4.38797C18.9095 4.18378 19 3.9264 19 3.53051C19 2.98673 18.8038 2.61692 18.54 2.37882C18.2675 2.13294 17.8914 2 17.5 2C17.1086 2 16.7325 2.13294 16.46 2.37882ZM18.0133 9.64196C18.2232 9.82138 18.2479 10.137 18.0685 10.3469L18.0612 10.3554C17.8818 10.5653 17.5661 10.59 17.3562 10.4106C17.1463 10.2312 17.1216 9.91557 17.301 9.70566L17.3083 9.69716C17.4877 9.48725 17.8033 9.46253 18.0133 9.64196Z" fill="currentColor"/>
</svg>"""

# EVOLUCIÓN HCM CLOUD: Personas y Talento corporativo (trazo fino continuo estilo Línea Directa)
svg_hcm = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M12 2C13.6569 2 15 3.34315 15 5C15 6.65685 13.6569 8 12 8C10.3431 8 9 6.65685 9 5C9 3.34315 10.3431 2 12 2ZM12 3C10.8954 3 10 3.89543 10 5C10 6.10457 10.8954 7 12 7C13.1046 7 14 6.10457 14 5C14 3.89543 13.1046 3 12 3Z" fill="currentColor"/>
    <path fill-rule="evenodd" clip-rule="evenodd" d="M6 14C6 11.7909 8.68629 10 12 10C15.3137 10 18 11.7909 18 14V17C18 17.5523 17.5523 18 17 18H7C6.44772 18 6 17.5523 6 17V14ZM12 11C9.23858 11 7 12.3431 7 14V17H17V14C17 12.3431 14.7614 11 12 11Z" fill="currentColor"/>
    <path fill-rule="evenodd" clip-rule="evenodd" d="M18.5 4C19.6046 4 20.5 4.89543 20.5 6C20.5 7.10457 19.6046 8 18.5 8C17.3954 8 16.5 7.10457 16.5 6C16.5 4.89543 17.3954 4 18.5 4Z" fill="currentColor"/>
    <path fill-rule="evenodd" clip-rule="evenodd" d="M5.5 4C6.60457 4 7.5 4.89543 7.5 6C7.5 7.10457 6.60457 8 5.5 8C4.39543 8 3.5 7.10457 3.5 6C3.5 4.89543 4.39543 4 5.5 4Z" fill="currentColor"/>
    <path d="M18 11.5C19.5 12 21 13 21 15V17H19V15C19 13.8 18.5 12.5 18 11.5Z" fill="currentColor"/>
    <path d="M6 11.5C4.5 12 3 13 3 15V17H5V15C5 13.8 5.5 12.5 6 11.5Z" fill="currentColor"/>
</svg>"""

# CRM OPERACIONAL: Ficha 360° del asegurado omnicanal en trazo fino
svg_crm = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <circle cx="12" cy="7.5" r="3.2" stroke="currentColor" stroke-width="1.2"/>
    <path d="M6.5 17C6.5 14.2 9 12.5 12 12.5C15 12.5 17.5 14.2 17.5 17" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/>
    <circle cx="12" cy="12" r="9.5" stroke="currentColor" stroke-width="1.1" stroke-dasharray="2.5 2"/>
    <circle cx="21" cy="9" r="1.4" fill="currentColor"/>
    <circle cx="3" cy="15" r="1.4" fill="currentColor"/>
    <circle cx="12" cy="21.5" r="1.4" fill="currentColor"/>
</svg>"""

# GESTIÓN DE USUARIOS: Escudo de seguridad y garantía oficial (poliza-otros-seguros-1.svg de Línea Directa)
svg_usuarios = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M3.5 3.11805C3.5 2.25694 4.17909 1.5 5.10858 1.5H18.9144C18.944 1.5 18.9734 1.50125 19.0025 1.5037C19.8764 1.56214 20.5 2.29236 20.5 3.11805V9.05908C20.5 10.8518 20.1504 12.5909 19.4816 14.1926C19.3753 14.4475 19.0824 14.5678 18.8276 14.4614C18.5728 14.355 18.4525 14.0622 18.5588 13.8074C19.176 12.3293 19.5 10.7213 19.5 9.05908V3.11805C19.5 2.78975 19.2557 2.52159 18.9331 2.5013L18.9259 2.50085L18.9187 2.50019L18.9144 2.5H5.10858C4.76338 2.5 4.5 2.77667 4.5 3.11805V9.06588C4.5 9.89959 4.50108 11.0299 4.92654 12.4447C5.35317 13.8635 6.20622 15.5677 7.91125 17.5473L11.571 21.312C11.6916 21.4361 12.3445 21.5 12 21.5C12.1466 21.5 12.3149 21.4383 12.4246 21.317L12.4306 21.3103L15.293 18.51C15.4854 18.312 15.802 18.3075 16 18.5C16.198 18.6925 16.2025 19.009 16.01 19.207L13.1596 21.9951C12.8342 22.3501 12.3844 22.5 12 22.5C11.5726 22.5 11.1574 22.3212 10.854 22.009L7.17379 18.2234L7.15357 18.1999C5.36789 16.1267 4.4404 14.3007 3.9689 12.7327C3.49999 11.1733 3.49999 9.92161 3.5 9.07176V3.11805Z" fill="currentColor"/>
    <path d="M12 5.99995C12.2761 5.99995 12.5 6.22381 12.5 6.49995V12.4999C12.5 12.7761 12.2761 12.9999 12 12.9999C11.7239 12.9999 11.5 12.7761 11.5 12.4999V6.49995C11.5 6.22381 11.7239 5.99995 12 5.99995Z" fill="currentColor"/>
    <path d="M12.3445 15.1272C12.5497 15.3119 12.5664 15.6281 12.3817 15.8333L12.3717 15.8444C12.1869 16.0497 11.8708 16.0663 11.6655 15.8816C11.4603 15.6969 11.4436 15.3807 11.6284 15.1755L11.6384 15.1644C11.8231 14.9591 12.1392 14.9425 12.3445 15.1272Z" fill="currentColor"/>
</svg>"""

# GESTIÓN DE LA INFORMACIÓN: Libro/wiki funcional de conocimiento en trazo fino
svg_info = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M4 19.5V4.5C4 3.67 4.67 3 5.5 3H18.5C19.33 3 20 3.67 20 4.5V19.5C20 20.33 19.33 21 18.5 21H5.5C4.67 21 4 20.33 4 19.5ZM5.5 4C5.22 4 5 4.22 5 4.5V18.5H18.5C18.78 18.5 19 18.28 19 18V4.5C19 4.22 18.78 4 18.5 4H5.5Z" fill="currentColor"/>
    <path d="M7.5 7.5H16.5M7.5 11H14.5M7.5 14.5H16.5" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/>
</svg>"""

# ARQUITECTURA TÉCNICA: Microservicios en trazo fino
svg_arq = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="3" y="3" width="7" height="7" rx="1.5" stroke="currentColor" stroke-width="1.2"/>
    <rect x="14" y="3" width="7" height="7" rx="1.5" stroke="currentColor" stroke-width="1.2" stroke-dasharray="2 1.5"/>
    <rect x="3" y="14" width="7" height="7" rx="1.5" stroke="currentColor" stroke-width="1.2" stroke-dasharray="2 1.5"/>
    <rect x="14" y="14" width="7" height="7" rx="1.5" stroke="currentColor" stroke-width="1.2"/>
    <path d="M10 6.5H14M6.5 10V14M17.5 10V14M10 17.5H14" stroke="currentColor" stroke-width="1.1"/>
</svg>"""

# DEMOS / ARCHIVO HISTÓRICO
svg_demo1 = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <circle cx="12" cy="12" r="8" stroke="currentColor" stroke-width="1.2" stroke-dasharray="2.5 2"/>
    <circle cx="12" cy="12" r="2.5" fill="currentColor"/>
    <line x1="12" y1="2" x2="12" y2="4" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/>
    <line x1="12" y1="20" x2="12" y2="22" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/>
</svg>"""

svg_demo2 = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M12 4L19 8L12 12L5 8L12 4Z" stroke="currentColor" stroke-width="1.2" stroke-linejoin="round"/>
    <path d="M5 12L12 16L19 12" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M5 16L12 20L19 16" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""

svg_archive = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="4" y="4" width="16" height="16" rx="3" stroke="currentColor" stroke-width="1.2" fill="currentColor" fill-opacity="0.08"/>
    <circle cx="12" cy="12" r="3.5" stroke="currentColor" stroke-width="1.1"/>
    <circle cx="12" cy="12" r="1.2" fill="currentColor"/>
</svg>"""

# ==============================================================================
# 2. ACTUALIZAR HTML index.html (CABECERA CON LOGO Y TARJETAS ACTUALIZADAS)
# ==============================================================================
print("[1/3] Actualizando index.html con logo en cabecera e iconografía oficial...")

with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()

# Cabecera con logo oficial de Línea Directa
new_island_brand = """        <!-- Identidad Corporativa Oficial Línea Directa -->
        <a href="#" class="island-brand" title="Inicio - Cuaderno de Bitácora">
            <div class="island-logo-badge">
                <img src="../assets/img/logo_header_lda.png" alt="Línea Directa Aseguradora" class="island-logo-img">
            </div>
            <div class="island-title">
                <span class="island-portal-name">Cuaderno de Bitácora</span>
                <span class="island-badge">Command Center v2.4</span>
            </div>
        </a>"""

html = re.sub(
    r'<a href="#" class="island-brand"[^>]*>.*?</a>',
    new_island_brand,
    html,
    flags=re.DOTALL
)

# Tarjetas Carril 1: Gestión Directa
cards_direct = f"""                    <!-- Evolución HCM Cloud -->
                    <a href="../HCM/index.html" class="apple-card" data-accent="red">
                        <div class="kicker" style="color: var(--lda-red);"><span class="kicker-dot"></span> GESTIÓN DIRECTA</div>
                        <h3 class="title">Evolución HCM Cloud</h3>
                        <p class="desc">Núcleo integral de RR.HH. Migración estratégica de PeopleSoft a Oracle Cloud Fusion, optimizando la gestión del talento, nóminas y estructura organizativa.</p>
                        <div class="card-tags">
                            <span class="tech-tag">Oracle Cloud HCM</span>
                            <span class="tech-tag">Gestión del Talento</span>
                            <span class="tech-tag">Nóminas</span>
                            <span class="tech-tag">PeopleSoft</span>
                        </div>
                        <div class="card-visual" style="color: var(--lda-red);">
                            {svg_hcm}
                        </div>
                    </a>

                    <!-- Transformación y Eficiencia RRHH -->
                    <a href="../IA Area Personas/index.html" class="apple-card" data-accent="red">
                        <div class="kicker" style="color: var(--lda-red);"><span class="kicker-dot"></span> PENDIENTE APROBACIÓN</div>
                        <h3 class="title">Eficiencia RRHH & IA</h3>
                        <p class="desc">Iniciativa estratégica para automatización de consultas internas, asistentes cognitivos con LidIA y optimización operativa en gestión de personas.</p>
                        <div class="card-tags">
                            <span class="tech-tag">Inteligencia Artificial</span>
                            <span class="tech-tag">Copilot M365</span>
                            <span class="tech-tag">Asistente LidIA</span>
                            <span class="tech-tag">Eficiencia Personas</span>
                        </div>
                        <div class="card-visual" style="color: var(--lda-red);">
                            {svg_ia}
                        </div>
                    </a>"""

# Tarjetas Carril 2: Facilitadores (Perseo con coche, Siniestros con taller/reparación, Telefonía con teléfono oficial)
cards_facilitator = f"""                    <!-- Perseo (Core Pólizas Auto) -->
                    <a href="../Perseo/index.html" class="apple-card" data-accent="amber">
                        <div class="kicker" style="color: #f59e0b;"><span class="kicker-dot"></span> FACILITADOR</div>
                        <h3 class="title">Perseo</h3>
                        <p class="desc">Plataforma estratégica core de tramitación y suscripción de pólizas. Arquitectura modular de alto rendimiento para el negocio asegurador.</p>
                        <div class="card-tags">
                            <span class="tech-tag">Pólizas & Clientes</span>
                            <span class="tech-tag">Supervisión Comercial</span>
                            <span class="tech-tag">Speech Analytics</span>
                            <span class="tech-tag">Coaching</span>
                        </div>
                        <div class="card-visual" style="color: #CC3333;">
                            {svg_perseo}
                        </div>
                    </a>

                    <!-- CRM Operacional -->
                    <a href="../CRM Operacional/index.html" class="apple-card" data-accent="amber">
                        <div class="kicker" style="color: #f59e0b;"><span class="kicker-dot"></span> FACILITADOR</div>
                        <h3 class="title">CRM Operacional</h3>
                        <p class="desc">Ecosistema integral de gestión comercial y atención omnicanal a asegurados con visión 360°, automatización y trazabilidad total.</p>
                        <div class="card-tags">
                            <span class="tech-tag">Gestión de Asegurados</span>
                            <span class="tech-tag">Omnicanalidad</span>
                            <span class="tech-tag">Atención Comercial</span>
                            <span class="tech-tag">Expediente Único</span>
                        </div>
                        <div class="card-visual" style="color: #f59e0b;">
                            {svg_crm}
                        </div>
                    </a>

                    <!-- Telefonía - Genesys Cloud CX -->
                    <a href="../Telefonia - Genesis CX/index.html" class="apple-card" data-accent="amber">
                        <div class="kicker" style="color: #f59e0b;"><span class="kicker-dot"></span> FACILITADOR</div>
                        <h3 class="title">Telefonía Genesys CX</h3>
                        <p class="desc">Transformación de la infraestructura de Contact Center a la nube pública de Genesys. Enrutamiento inteligente y analítica en tiempo real.</p>
                        <div class="card-tags">
                            <span class="tech-tag">Genesys Cloud CX</span>
                            <span class="tech-tag">Contact Center</span>
                            <span class="tech-tag">Telefonía IP</span>
                            <span class="tech-tag">Atención Clientes</span>
                        </div>
                        <div class="card-visual" style="color: #f59e0b;">
                            {svg_telefonia}
                        </div>
                    </a>

                    <!-- Reingeniería de Siniestros (Talleres, Reparaciones y Peritación) -->
                    <a href="../Reingenieria Siniestros/index.html" class="apple-card" data-accent="amber">
                        <div class="kicker" style="color: #f59e0b;"><span class="kicker-dot"></span> FACILITADOR</div>
                        <h3 class="title">Reingeniería Siniestros</h3>
                        <p class="desc">Modernización integral del ciclo de vida del siniestro: red de talleres colaboradores, peritación digital, detección de fraude y agilización del pago.</p>
                        <div class="card-tags">
                            <span class="tech-tag">Tramitación Siniestros</span>
                            <span class="tech-tag">Talleres Colaboradores</span>
                            <span class="tech-tag">Peritación Digital</span>
                            <span class="tech-tag">Resolución Rápida</span>
                        </div>
                        <div class="card-visual" style="color: #CC3333;">
                            {svg_siniestros}
                        </div>
                    </a>"""

# Tarjetas Carril 3: Servicios
cards_services = f"""                    <!-- Gestión de Usuarios (IAM y Seguridad de Accesos) -->
                    <a href="../Gestion de Usuarios/index.html" class="apple-card" data-accent="blue">
                        <div class="kicker" style="color: #3b82f6;"><span class="kicker-dot"></span> SERVICIO / IAM</div>
                        <h3 class="title">Gestión de Usuarios</h3>
                        <p class="desc">Gobernanza de identidades y accesos corporativos. Automatización de altas, bajas y cambios de rol con cumplimiento regulatorio.</p>
                        <div class="card-tags">
                            <span class="tech-tag">Identidad Corporativa</span>
                            <span class="tech-tag">Gobernanza IAM</span>
                            <span class="tech-tag">Control de Accesos</span>
                            <span class="tech-tag">Auditoría</span>
                        </div>
                        <div class="card-visual" style="color: #3b82f6;">
                            {svg_usuarios}
                        </div>
                    </a>

                    <!-- Demo Card 3 -->
                    <div class="apple-card disabled-card">
                        <div class="kicker">EN DEFINICIÓN</div>
                        <h3 class="title">Arquitectura Técnica</h3>
                        <p class="desc">Estructura base para la documentación de microservicios, APIs e integraciones de sistemas centrales.</p>
                        <div class="card-visual" style="opacity: 0.65;">
                            {svg_arq}
                        </div>
                    </div>

                    <!-- Demo Card 4 -->
                    <div class="apple-card disabled-card">
                        <div class="kicker">EN DISEÑO</div>
                        <h3 class="title">Nueva Operativa</h3>
                        <p class="desc">Tarjetón genérico preparado para alojar servicios organizacionales futuros.</p>
                        <div class="card-visual" style="opacity: 0.65;">
                            {svg_demo1}
                        </div>
                    </div>

                    <!-- Demo Card 5 -->
                    <div class="apple-card disabled-card">
                        <div class="kicker">PENDIENTE</div>
                        <h3 class="title">Próxima Operativa</h3>
                        <p class="desc">Módulo no definido, espacio visual concebido para balancear el carrusel de servicios.</p>
                        <div class="card-visual" style="opacity: 0.65;">
                            {svg_demo2}
                        </div>
                    </div>"""

# Tarjetas Carril 4: Cerrados
cards_closed = f"""                    <!-- Gestión de la Información (Traspasado a Transformación) -->
                    <a href="../Gobierno de Informacion/index.html" class="apple-card" data-accent="purple" style="border-color: rgba(139, 92, 246, 0.4); background: linear-gradient(135deg, var(--bg-card) 0%, rgba(139, 92, 246, 0.05) 100%);">
                        <div class="kicker" style="color: #8B5CF6;"><span class="kicker-dot"></span> HISTÓRICO TRASPASADO</div>
                        <h3 class="title">Gestión de la Información</h3>
                        <p class="desc">Proyecto de Inteligencia LidIA y metodología GIN transferido al Área de Transformación. Conserva aquí todo el contexto, historial y wiki funcional.</p>
                        <div class="card-tags">
                            <span class="tech-tag">Metodología GIN</span>
                            <span class="tech-tag">Gobierno de Datos</span>
                            <span class="tech-tag">Wiki Funcional</span>
                            <span class="tech-tag">Traspaso Estratégico</span>
                        </div>
                        <div class="card-visual" style="color: #8B5CF6;">
                            {svg_info}
                        </div>
                    </a>

                    <!-- Archivo Histórico Card 1 -->
                    <div class="apple-card disabled-card" data-accent="purple">
                        <div class="kicker" style="color: var(--text-muted);">HISTORIAL ARCHIVADO</div>
                        <h3 class="title" style="color: var(--text-muted);">Archivo de Porfolio</h3>
                        <p class="desc">Espacio reservado para almacenar el historial de proyectos concluidos en ciclos anteriores.</p>
                        <div class="card-tags">
                            <span class="tech-tag">Ciclos Anteriores</span>
                            <span class="tech-tag">Auditoría</span>
                        </div>
                        <div class="card-visual" style="opacity: 0.5;">
                            {svg_archive}
                        </div>
                    </div>

                    <!-- Archivo Histórico Card 2 -->
                    <div class="apple-card disabled-card" data-accent="purple">
                        <div class="kicker" style="color: var(--text-muted);">REPOSITORIO</div>
                        <h3 class="title" style="color: var(--text-muted);">Registro Histórico</h3>
                        <p class="desc">Conservación de memorias técnicas, lecciones aprendidas y acuerdos de gobernanza pasados.</p>
                        <div class="card-tags">
                            <span class="tech-tag">Lecciones</span>
                            <span class="tech-tag">Memorias</span>
                        </div>
                        <div class="card-visual" style="opacity: 0.5;">
                            {svg_archive}
                        </div>
                    </div>"""

# Reemplazos de pistas
html = re.sub(
    r'<div class="carousel-track" id="track-direct"[^>]*>.*?</div>\s*<button class="carousel-btn right',
    f'<div class="carousel-track" id="track-direct" onscroll="updateCarouselButtons(this)">\n{cards_direct}\n                </div>\n                <button class="carousel-btn right',
    html,
    flags=re.DOTALL
)

html = re.sub(
    r'<div class="carousel-track" id="track-facilitator"[^>]*>.*?</div>\s*<button class="carousel-btn right',
    f'<div class="carousel-track" id="track-facilitator" onscroll="updateCarouselButtons(this)">\n{cards_facilitator}\n                </div>\n                <button class="carousel-btn right',
    html,
    flags=re.DOTALL
)

html = re.sub(
    r'<div class="carousel-track" id="track-services"[^>]*>.*?</div>\s*<button class="carousel-btn right',
    f'<div class="carousel-track" id="track-services" onscroll="updateCarouselButtons(this)">\n{cards_services}\n                </div>\n                <button class="carousel-btn right',
    html,
    flags=re.DOTALL
)

html = re.sub(
    r'<div class="carousel-track" id="track-closed"[^>]*>.*?</div>\s*<button class="carousel-btn right',
    f'<div class="carousel-track" id="track-closed" onscroll="updateCarouselButtons(this)">\n{cards_closed}\n                </div>\n                <button class="carousel-btn right',
    html,
    flags=re.DOTALL
)

with open(INDEX_HTML, "w", encoding="utf-8") as f:
    f.write(html)

print("  [+] index.html actualizado con logo en la cabecera y tarjetas sincronizadas.")

# ==============================================================================
# 3. ACTUALIZAR build_unified_core_css.py CON ESTILOS BRANDING LÍNEA DIRECTA
# ==============================================================================
print("[2/3] Integrando diseño oficial de marketing de Línea Directa en CSS...")

with open(CORE_BUILDER, "r", encoding="utf-8") as f:
    css_script = f.read()

lda_marketing_styles = """
/* ==========================================================================
   ESTILO CORPORATIVO OFICIAL LÍNEA DIRECTA (BRANDBOOK & MARKETING coches.lineadirecta.com)
   ========================================================================== */

/* Variables Corporativas Oficiales */
:root {
    --ld-primary-high: #CC3333;
    --ld-primary-active: #CC3333;
    --ld-primary-hover: #B52B2B;
    --ld-primary-low: #F8E3E3;
    --ld-surface-high: #1A1A1A;
    --ld-surface-mid: rgba(26, 26, 26, 0.12);
    --ld-surface-low: rgba(26, 26, 26, 0.04);
    --ld-background-alt: #F7F7F7;
    
    --lda-red: #CC3333;
    --lda-red-hover: #B52B2B;
    --lda-red-glow: rgba(204, 51, 51, 0.18);
    --bg-page: #F7F7F7;
    --bg-card: #FFFFFF;
    --bg-header: #FFFFFF;
    --text-main: #1A1A1A;
    --text-sec: #595959;
    --glass-border: rgba(26, 26, 26, 0.08);
    --shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
    
    --font-family-primary: 'CircularXX', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

[data-theme="dark"] {
    --bg-page: #121214;
    --bg-card: rgba(26, 26, 30, 0.88);
    --bg-header: rgba(20, 20, 24, 0.88);
    --text-main: #F5F5F7;
    --text-sec: #A1A1A6;
    --ld-primary-high: #E04848;
    --lda-red: #E04848;
    --lda-red-hover: #F05555;
    --lda-red-glow: rgba(224, 72, 72, 0.3);
    --glass-border: rgba(255, 255, 255, 0.12);
    --shadow: 0 10px 32px rgba(0, 0, 0, 0.5);
}

/* Tipografía global de Línea Directa */
body, button, input, select, textarea, .title, h1, h2, h3, h4 {
    font-family: var(--font-family-primary) !important;
}

/* Identidad en la cabecera (Island Navbar) */
.island-brand {
    display: flex;
    align-items: center;
    gap: 12px;
    text-decoration: none;
}

.island-logo-badge {
    display: flex;
    align-items: center;
    justify-content: center;
    background: #FFFFFF;
    padding: 4px 10px;
    border-radius: 8px;
    border: 1px solid rgba(0, 0, 0, 0.08);
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03);
}

.island-logo-img {
    height: 24px;
    width: auto;
    display: block;
    object-fit: contain;
}

.island-title {
    display: flex;
    flex-direction: column;
    gap: 2px;
}

.island-portal-name {
    font-size: 0.95rem;
    font-weight: 700;
    color: var(--text-main);
    letter-spacing: -0.01em;
}

.island-badge {
    font-size: 0.68rem;
    color: var(--lda-red);
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
}

/* Breadcrumb global en páginas secundarias (Perseo, HCM, etc.) */
.global-nav-wrapper {
    background: var(--bg-card) !important;
    border: 1px solid var(--glass-border) !important;
    border-radius: 999px !important;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04) !important;
    backdrop-filter: blur(16px) !important;
    -webkit-backdrop-filter: blur(16px) !important;
}

.nav-breadcrumb-item {
    font-size: 0.88rem !important;
    font-weight: 600 !important;
    color: var(--text-sec) !important;
    text-decoration: none !important;
}

.nav-breadcrumb-item.current {
    color: var(--lda-red) !important;
    font-weight: 700 !important;
}

/* Tarjetas Oficiales estilo Marketing Línea Directa */
.apple-card {
    background: var(--bg-card) !important;
    border: 1px solid var(--glass-border) !important;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.03) !important;
    transition: transform 0.28s cubic-bezier(0.16, 1, 0.3, 1),
                box-shadow 0.28s cubic-bezier(0.16, 1, 0.3, 1),
                border-color 0.28s ease !important;
}

.apple-card:hover {
    transform: translateY(-4px) !important;
    border-color: rgba(204, 51, 51, 0.35) !important;
    box-shadow: 0 12px 28px rgba(204, 51, 51, 0.08), 0 4px 10px rgba(0, 0, 0, 0.03) !important;
}

/* Caja de icono (.card-visual) con fondo sutil y halo corporativo */
.card-visual {
    background: rgba(204, 51, 51, 0.02) !important;
    border: 1px solid rgba(204, 51, 51, 0.06) !important;
    border-radius: 14px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    transition: background 0.3s ease, border-color 0.3s ease !important;
}

.apple-card:hover .card-visual {
    background: rgba(204, 51, 51, 0.05) !important;
    border-color: rgba(204, 51, 51, 0.16) !important;
}

.card-visual svg {
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
    filter: drop-shadow(0 2px 5px rgba(204, 51, 51, 0.08)) !important;
}

.apple-card:hover .card-visual svg {
    transform: scale(1.08) !important;
}

/* Badges y Tags estilo Línea Directa */
.tech-tag {
    background: var(--ld-primary-low) !important;
    color: var(--ld-primary-high) !important;
    border: 1px solid rgba(204, 51, 51, 0.15) !important;
    font-size: 0.72rem !important;
    font-weight: 600 !important;
    padding: 3px 8px !important;
    border-radius: 6px !important;
    letter-spacing: 0.02em !important;
}

[data-theme="dark"] .tech-tag {
    background: rgba(224, 72, 72, 0.15) !important;
    color: #FF8585 !important;
    border-color: rgba(224, 72, 72, 0.25) !important;
}

.hero-badge {
    background: var(--ld-primary-high) !important;
    color: #FFFFFF !important;
    border-radius: 999px !important;
    font-weight: 700 !important;
    font-size: 0.74rem !important;
    padding: 5px 14px !important;
    letter-spacing: 0.04em !important;
}
"""

# Reemplazar o concatenar en clean_addons_css
if "BRANDBOOK & MARKETING coches.lineadirecta.com" in css_script:
    css_script = re.sub(
        r'/\* =+\s*ESTILO CORPORATIVO OFICIAL LÍNEA DIRECTA.*?\.hero-badge\s*\{[^}]*\}\s*',
        lda_marketing_styles.strip() + '\n',
        css_script,
        flags=re.DOTALL
    )
else:
    css_script = css_script.replace(
        '"""\n\nfull_core_css = base_css.strip()',
        '\n' + lda_marketing_styles + '\n"""\n\nfull_core_css = base_css.strip()'
    )

with open(CORE_BUILDER, "w", encoding="utf-8") as f:
    f.write(css_script)

# Recompilar CSS
subprocess.run(["python", CORE_BUILDER], check=True)
print("  [+] bitacora-core.css y styles_bitacora.css compilados con diseño de marketing de Línea Directa.")

# ==============================================================================
# 4. AUDITORÍA FINAL
# ==============================================================================
print("[3/3] Ejecutando auditoría de referencias...")
audit_script = os.path.join(BASE_DIR, "scratch", "audit_project.py")
subprocess.run(["python", audit_script], check=True)

print("[OK] ¡Diseño de Marketing, Iconografía Oficial y Marca Línea Directa aplicados con éxito!")
