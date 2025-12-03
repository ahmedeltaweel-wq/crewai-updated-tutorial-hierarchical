# Fix All Fly.io Apps Script
# Run this in PowerShell

Write-Host "🚀 Starting to fix all Fly.io apps..." -ForegroundColor Green

# Refresh PATH
$env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")

# 1. Fix AI Newsletter Crew
Write-Host "`n📰 Fixing AI Newsletter Crew..." -ForegroundColor Cyan

Write-Host "Setting Google API key..."
flyctl secrets set GOOGLE_API_KEY=AIzaSyB3m8Pm-7V6y8uf9rwl5gGiwKpO7DiAkRw -a ai-newsletter-crew

Write-Host "Destroying failed machines..."
flyctl machines destroy 48e36edce35ee8 -a ai-newsletter-crew --force
flyctl machines destroy 683952dc163638 -a ai-newsletter-crew --force

Write-Host "Deploying fresh machines..."
Push-Location "ai-newsletter-crew-main"
flyctl deploy -a ai-newsletter-crew
Pop-Location

# 2. Prevent auto-suspend for Telegram Bot
Write-Host "`n🤖 Configuring Telegram Bot..." -ForegroundColor Cyan

Write-Host "Setting minimum machines to 1..."
flyctl scale count 1 -a telegram-health-bot

# 3. Check all apps status
Write-Host "`n✅ Checking all apps status..." -ForegroundColor Green
flyctl apps list

Write-Host "`n✅ Done! All apps should be fixed now." -ForegroundColor Green
Write-Host "Check status with: flyctl status -a APP_NAME" -ForegroundColor Yellow
