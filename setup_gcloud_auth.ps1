# Google Cloud Authentication Setup Script
# استخدم هذا السكريبت لإعداد gcloud authentication

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "   Google Cloud Authentication Setup" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# التحقق من تثبيت gcloud
Write-Host "[1/4] Checking gcloud installation..." -ForegroundColor Yellow
try {
    $gcloudVersion = gcloud --version 2>&1 | Select-Object -First 1
    Write-Host "OK: $gcloudVersion" -ForegroundColor Green
}
catch {
    Write-Host "ERROR: gcloud not found!" -ForegroundColor Red
    Write-Host "`nPlease install Google Cloud SDK from:" -ForegroundColor Yellow
    Write-Host "https://cloud.google.com/sdk/docs/install`n" -ForegroundColor Cyan
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""

# تسجيل الدخول
Write-Host "[2/4] Logging in to Google Cloud..." -ForegroundColor Yellow
Write-Host "Please complete the login in your browser..." -ForegroundColor Cyan
gcloud auth login
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Login failed" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host "OK: Login successful" -ForegroundColor Green
Write-Host ""

# تعيين المشروع
Write-Host "[3/4] Setting project..." -ForegroundColor Yellow
gcloud config set project eg-konecta-sandbox
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to set project" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host "OK: Project set to eg-konecta-sandbox" -ForegroundColor Green
Write-Host ""

# إعداد Application Default Credentials
Write-Host "[4/4] Setting up Application Default Credentials..." -ForegroundColor Yellow
Write-Host "Please complete the login in your browser..." -ForegroundColor Cyan
gcloud auth application-default login
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: ADC setup failed" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host "OK: Application Default Credentials configured" -ForegroundColor Green
Write-Host ""

# اكتمل الإعداد
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   Setup Complete!" -ForegroundColor Green
Write-Host "========================================`n" -ForegroundColor Cyan

# اختبار الإعداد
Write-Host "Testing the configuration..." -ForegroundColor Yellow
python test_gcloud_auth.py

Write-Host ""
Read-Host "Press Enter to exit"
