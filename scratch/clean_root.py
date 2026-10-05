import os
import shutil

BASE_DIR = r"C:\Proyectos_Claude\Proyecto Cuaderno de Bitacora"
DEST_DIR = os.path.join(BASE_DIR, "scratch", "legacy_tools")
os.makedirs(DEST_DIR, exist_ok=True)

KEEP = {
    ".agent",
    "01_Proyectos",
    "02_Conocimiento",
    "03_Recursos",
    "scratch",
    ".git",
    ".gitignore",
    "Índice del Vault.md"
}

moved = []
for item in os.listdir(BASE_DIR):
    if item in KEEP:
        continue
    src = os.path.join(BASE_DIR, item)
    dst = os.path.join(DEST_DIR, item)
    try:
        shutil.move(src, dst)
        moved.append(item)
    except Exception as e:
        print(f"Error moving {item}: {e}")

print(f"Successfully moved {len(moved)} items to scratch/legacy_tools:")
for m in moved:
    print(f" - {m}")
