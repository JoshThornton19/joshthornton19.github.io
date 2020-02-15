set /A delayAmount=1000 ::Time in seconds
set ssid=
set profileName= ::Likely the SSID

:start
@CLS
@echo Polling google.com for a connection
@ping -n 1 www.google.com | findstr TTL && goto Connected
@ping -n 1 www.google.com | findstr TTL || goto Disconnected

:Connected
@echo Connection test succeeded
@TIMEOUT %delayAmount%
@goto start

:Disconnected
@echo Connection test failed
@echo Attempting Connection...
@netsh wlan connect ssid=%ssid% name=%profileName%
@TIMEOUT %delayAmount%
goto start



