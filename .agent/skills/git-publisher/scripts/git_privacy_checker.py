"""
Script de Auditoría de Privacidad y Anonimización Pre-Commit / Pre-Push.
Valida que ni los mensajes de commit ni el contenido preparado (staged)
contengan nombres reales de la empresa, personas o proyectos sensibles.
"""

import sys
import subprocess
import re

# Términos sensibles que activan advertencia de anonimización
# (Expresiones regulares en minúsculas)
SENSITIVE_PATTERNS = [
    r"\bl\xednea\s+directa\b",
    r"\blinea\s+directa\b",
    r"\blda\b",
    r"\bperseo\b",
    r"\bgenesys\b",
    r"\bpeoplesoft\b",
    r"\blidia\b",
    r"\bmaldonado\b",
    r"\bkitt\b",
    r"\blupe\b",
    r"\bquique\s+cid\b",
    r"\benrique\s+cid\b",
    r"\bgerson\b",
]

def check_text(text: str, label: str = "Texto") -> bool:
    """Verifica si un texto contiene términos sensibles."""
    text_lower = text.lower()
    findings = []
    for pattern in SENSITIVE_PATTERNS:
        matches = re.findall(pattern, text_lower)
        if matches:
            findings.append(pattern)

    if findings:
        print(f"\n[ALERTA DE PRIVACIDAD] Se han detectado términos sensibles en {label}:")
        for f in set(findings):
            print(f"  - Patrón detectado: {f}")
        print("\nRECUERDA: Debes usar nombres genéricos como 'Proyecto 1', 'Proyecto 2', 'Entidad', etc.")
        return False
    return True

def check_commit_message(msg: str) -> bool:
    print("-> Verificando mensaje de commit...")
    valid = check_text(msg, "Mensaje de commit")
    if valid:
        print("[OK] Mensaje de commit anonimizado y seguro.")
    return valid

def check_staged_diff() -> bool:
    print("-> Verificando cambios preparados (git diff --cached)...")
    try:
        res = subprocess.run(["git", "diff", "--cached"], capture_output=True, text=True, encoding="utf-8", errors="replace")
        diff_text = res.stdout
        if not diff_text.strip():
            print("[INFO] No hay cambios en el área de preparación (stage).")
            return True
        current_file = ""
        added_lines = []
        for line in diff_text.splitlines():
            if line.startswith("diff --git"):
                current_file = line
            elif "git_privacy_checker.py" in current_file:
                continue
            elif line.startswith("+") and not line.startswith("+++"):
                raw_text = line[1:]
                # En enlaces Markdown [[ruta|texto visible]], inspeccionamos el texto visible
                clean_text = re.sub(r'\[\[[^|\]]+\|([^\]]+)\]\]', r'\1', raw_text)
                # En enlaces estándar [texto](ruta), inspeccionamos el texto visible
                clean_text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', clean_text)
                added_lines.append(clean_text)
        full_added = "\n".join(added_lines)
        valid = check_text(full_added, "Líneas añadidas en git stage")
        if valid:
            print("[OK] Cambios preparados verificados sin fugas de privacidad detectadas.")
        return valid
    except Exception as e:
        print(f"[ERROR] No se pudo ejecutar git diff: {e}")
        return False

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--check-staged":
        ok = check_staged_diff()
        sys.exit(0 if ok else 1)
    elif len(sys.argv) > 1 and sys.argv[1] == "--check-msg":
        msg = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else ""
        ok = check_commit_message(msg)
        sys.exit(0 if ok else 1)
    else:
        print("Uso:")
        print("  python git_privacy_checker.py --check-msg 'tu mensaje de commit'")
        print("  python git_privacy_checker.py --check-staged")

if __name__ == "__main__":
    main()
