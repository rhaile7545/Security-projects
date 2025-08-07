# PowerShell Firewall Bypass Example (For Educational Use Only)
New-NetFirewallRule -DisplayName "AllowAllOut" -Direction Outbound -Action Allow -Protocol TCP -Enabled True
