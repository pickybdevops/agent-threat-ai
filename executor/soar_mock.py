def create_ticket(cve, hosts, yara_rule):
    print(f"[SOAR] Created ticket for {cve['cve']} affecting {hosts}")
    print(f"[SOAR] Attached YARA rule:\n{yara_rule}")
