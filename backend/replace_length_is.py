import os
import re
import shutil

# Шаблонлар жойлашган асосий папка
TEMPLATES_DIR = r"C:\Users\Брокер\Downloads\Telegram Desktop\energopribor\backend\templates"

# length_is фильтрни length==N га алмаштириш учун regex
pattern = re.compile(r'(\{\%\s*if\s+.+?)\|length_is:(\d+)(.*?\%\})')

def backup_file(file_path):
    backup_path = file_path + ".bak"
    shutil.copy2(file_path, backup_path)
    print(f"[Backup] {backup_path} created.")

def replace_length_is(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content, count = pattern.subn(r'\1|length == \2\3', content)

    if count > 0:
        backup_file(file_path)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"[Updated] {count} occurrence(s) in {file_path}")

def walk_and_replace(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                replace_length_is(file_path)

if __name__ == "__main__":
    walk_and_replace(TEMPLATES_DIR)
    print("✅ All length_is filters replaced. Backups created with .bak extension.")
