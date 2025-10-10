# =========================
# 0️⃣ Тушунтириш
# =========================
# Бу скрипт:
# 1. store ва carts иловаларидан эски миграцияларни ўчиради
# 2. db.sqlite3 файлини ўчиради
# 3. Янги миграцияларни яратади
# 4. Барча миграцияларни қўллайди
# 5. Серверни ишга туширади
# =========================

# 1️⃣ Эски миграцияларни ўчириш
Write-Host "⏳ Эски миграцияларни ўчиряпмиз..."

Get-ChildItem -Path ".\store\migrations" -File -Exclude "__init__.py" | Remove-Item
Get-ChildItem -Path ".\carts\migrations" -File -Exclude "__init__.py" | Remove-Item

# 2️⃣ Эски база (SQLite) ни ўчириш
if (Test-Path ".\db.sqlite3") {
    Write-Host "⏳ Эски базани ўчиряпмиз..."
    Remove-Item ".\db.sqlite3"
}

# 3️⃣ Янги миграцияларни яратиш
Write-Host "⏳ Янги миграцияларни яратиш..."
python manage.py makemigrations store
python manage.py makemigrations carts
python manage.py makemigrations

# 4️⃣ Барча миграцияларни қўллаш
Write-Host "⏳ Барча миграцияларни қўллаяпмиз..."
python manage.py migrate

# 5️⃣ Серверни ишга тушириш
Write-Host "✅ Серверни ишга тушираяпмиз..."
python manage.py runserver
