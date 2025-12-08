# ========================================
# Local Deployment Script - AI Applications
# Uses Service Account JSON for authentication
# ========================================

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   AI Applications - Local Runner" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Set the working directory to script location
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptPath

# Set Google Cloud credentials using service account JSON
$serviceAccountPath = Join-Path $scriptPath "service-account-key.json"
$env:GOOGLE_APPLICATION_CREDENTIALS = $serviceAccountPath
$env:GOOGLE_CLOUD_PROJECT = "eg-konecta-sandbox"
$env:VERTEX_AI_LOCATION = "us-central1"
$env:USE_VERTEX_AI = "true"

Write-Host "[OK] Service Account: $serviceAccountPath" -ForegroundColor Green
Write-Host "[OK] Project: $env:GOOGLE_CLOUD_PROJECT" -ForegroundColor Green
Write-Host "[OK] Location: $env:VERTEX_AI_LOCATION" -ForegroundColor Green
Write-Host ""

# Check if service account file exists
if (-not (Test-Path $serviceAccountPath)) {
    Write-Host "[ERROR] Service Account file not found!" -ForegroundColor Red
    Write-Host "Please ensure service-account-key.json exists in the project folder." -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "Choose which application to run:" -ForegroundColor Yellow
Write-Host ""
Write-Host "[1] Electric Web App (Customer Service - Port 8080)"
Write-Host "[2] Newsletter Web App (AI Newsletter - Port 5000)"
Write-Host "[3] Smart DMS (Document Management - Port 5000)"
Write-Host "[4] Telegram Bot (Health Insurance Bot)"
Write-Host "[5] Test Service Account Connection"
Write-Host "[0] Exit"
Write-Host ""
$choice = Read-Host "Enter your choice (0-5)"

switch ($choice) {
    "1" {
        Write-Host ""
        Write-Host "Starting Electric Web App..." -ForegroundColor Cyan
        Write-Host "Access at: http://localhost:8080" -ForegroundColor Green
        Write-Host ""
        python electric_web_app.py
    }
    "2" {
        Write-Host ""
        Write-Host "Starting Newsletter Web App..." -ForegroundColor Cyan
        Write-Host "Access at: http://localhost:5000" -ForegroundColor Green
        Write-Host ""
        python web_app.py
    }
    "3" {
        Write-Host ""
        Write-Host "Starting Smart DMS..." -ForegroundColor Cyan
        Write-Host "Access at: http://localhost:5000" -ForegroundColor Green
        Write-Host ""
        python smart_dms_app.py
    }
    "4" {
        Write-Host ""
        Write-Host "Starting Telegram Bot..." -ForegroundColor Cyan
        Write-Host ""
        python telegram_bot.py
    }
    "5" {
        Write-Host ""
        Write-Host "Testing Service Account Connection..." -ForegroundColor Cyan
        Write-Host ""
        python test_service_account.py
        Read-Host "Press Enter to continue"
    }
    "0" {
        Write-Host "Goodbye!" -ForegroundColor Yellow
        exit 0
    }
    default {
        Write-Host "Invalid choice!" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "Application stopped." -ForegroundColor Yellow
