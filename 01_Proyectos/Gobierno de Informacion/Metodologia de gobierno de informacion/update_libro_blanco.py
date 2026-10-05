import sys

backup_file = r"c:\Users\ldaecc\.gemini\antigravity\scratch\Documentacion\02_Proyectos\Gobierno de Informacion\Backup versiones\infografia_metodologia - copia (2).html"
target_file = r"c:\Users\ldaecc\.gemini\antigravity\scratch\Documentacion\02_Proyectos\Gobierno de Informacion\Lidia\libro_blanco.html"

# Read backup file
with open(backup_file, "r", encoding="utf-8") as f:
    backup_lines = f.readlines()

# Extract lines 3661 to 4457 (inclusive). 0-indexed: 3660 to 4457
manual_content = backup_lines[3660:4457]

# Let's adjust the first line to remove ' hidden'
if 'hidden' in manual_content[0]:
    manual_content[0] = manual_content[0].replace(' hidden', '')

manual_content_str = "".join(manual_content)
# Ensure it closes with </div>
if not manual_content_str.strip().endswith('</div>'):
    # Let's append an extra div closure just in case, wait, line 4457 is '        </div>\n'
    # Actually, line 4456 is '        </div>\n'
    pass

# Read target file
with open(target_file, "r", encoding="utf-8") as f:
    target_lines = f.readlines()

# In target file, the div starts at line 46 ("    <div class=\"container view-section\" id=\"view-manual\">\n")
# and ends at line 409 ("    </div>\n")
# We'll find them programmatically to be safe.

start_idx = -1
end_idx = -1

for i, line in enumerate(target_lines):
    if '<div class="container view-section" id="view-manual">' in line:
        start_idx = i
        break

for i in range(start_idx + 1, len(target_lines)):
    if '    <script src="../scripts_infografia.js"></script>' in target_lines[i] or '</body>' in target_lines[i]:
        # The line before this should be the closing div
        end_idx = i - 1
        # Let's refine the end idx to exactly the last </div> before the script tag that we can find
        while end_idx > start_idx and '</div>' not in target_lines[end_idx]:
             end_idx -= 1
        break

if start_idx != -1 and end_idx != -1:
    new_target_lines = target_lines[:start_idx] + manual_content + target_lines[end_idx+1:]
    with open(target_file, "w", encoding="utf-8") as f:
        f.writelines(new_target_lines)
    print("Successfully updated libro_blanco.html")
else:
    print(f"Could not find exact bounds in target file. Start: {start_idx}, End: {end_idx}")
