#!/bin/bash
# generate_log.sh
# Creates fake web server access log with 200 entries
LOGFILE="logs/access.log"
rm -f "$LOGFILE"
IPS=("192.168.1.10" "10.0.0.5" "172.16.0.3" "192.168.1.25" "10.0.0.99")
PATHS=("/index.html" "/about.html" "/login" "/api/data" "/images/logo.png" "/admin" "/contract")
METHODS=("GET" "GET" "GET" "POST" "GET" "GET" "DELETE")
STATUSES=("200" "200" "200" "404" "500" "200" "403")
echo "Generating log file..."
for i in $(seq 1 200); do
	IP=${IPS[$((RANDOM % 5))]}
	PATH_=${PATHS[$((RANDOM % 7))]}
	METHOD=${METHODS[$((RANDOM % 7))]}
	STATUS=${STATUSES[$((RANDOM % 7))]}
	BYTES=$((RANDOM % 5000 + 100))
	TIMESTAMP="29/May/2026$(printf '%02d' $((RANDOM % 14 + 8))):
$(printf '%02d' $((RANDOM % 60))):$(printf '%02d' $((RANDOM % 60)))"
	echo "$IP - - [$TIMESTAMP] \"$METHOD $PATH_ HTTP/1.1\" 
$STATUS $BYTES" >> "$LOGFILE"
done

echo "Done. Log file: $LOGFILE"
echo "Total lines: $(wc -l < $LOGFILE)"


