# analyze.py
# Log File Analyzer
# CNM Code & Command Workshop - Python Afternoon

logfile = "logs/access.log"

with open(logfile, "r") as f:
	lines = f.readlines()

print(f"Total log lines: {len(lines)}")

ip_counts = {}
status_counts = {}
path_counts = {}

for line in lines:
	parts = line.split()
	
	if len(parts) < 9:
		continue
	ip = parts[0]
	status = parts[7]
	path = parts[5]

	ip_counts[ip] = ip_counts.get(ip, 0) + 1
	status_counts[status] = status_counts.get(status, 0) + 1
	path_counts[path] = path_counts.get(path, 0) + 1

print("Top IP Addresses")
for ip, count in sorted(ip_counts.items(), key=lambda x: x[1], reverse=True):
	print(f" {ip:<20} {count} requests")
print()
print("Status Code Breakdown")
labels = {"200": "OK", "404": "Not Found", "500": "Server Error", "403": 
"Forbidden"}
for status, count in sorted(status_counts.items(), key=lambda x:x[1], 
reverse=True):
	label = labels.get(status, "Other")
	print(f" {status} ({label:<15}) {count} times")
print()
print("Most Visited Pages")
for path, count in sorted(path_counts.items(), key=lambda x: x[1], 
reverse=True)[:5]:
	print(f" {path:<25} {count} hits")
print()

print("Security Alerts")
alerts_found = False

for ip, count in ip_counts.items():
	if count > 30:
		print(f" WARNING {ip} made {count} requests - possible brute force")
		alerts_found = True

if "500" in status_counts and status_counts["500"] > 10:
	print(f" WARNING {status_counts['500']} server errors detected Investigate the app")
	alerts_found = True
if "/admin" in path_counts and path_counts["/admin"] > 5:
	print(f" WARNING /admin accessed {path_counts['/admin']} times check who")
	alerts_found = True
if not alerts_found:
	print(" Ok No suspicious patterns detected")



report_file = "logs/report.txt"

with open(report_file, "w") as r:
	r.write("LOG ANALYSIS REPORT\n")
	r.write("==============\n\n")
	r.write(f"Total requests: {len(lines)}\n\n")
	
	r.write("Top IP Addresses:\n")
	for ip, count in sorted(ip_counts.items(), key=lambda x:x[1], reverse=True):
		r.write(f" {ip:<20} {count}\n")
	r.write("\nStatus Codes:\n")
	for status, count in sorted(status_counts.items(), key=lambda x: x[1], reverse=True):
		r.write(f" {status} {count}\n")
	r.write("\nTop Pages:\n")
	for path, count in sorted(path_counts.items(), key=lambda x: x[1], reverse=True):
		r.write(f" {path:<25} {count}\n")
print()
print(f"Report saved to: {report_file}")
