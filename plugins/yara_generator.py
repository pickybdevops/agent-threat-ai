def generate_yara_rule(cve):
    return f"rule Detect_{cve['cve'].replace('-', '_')} {{\n  strings:\n    $a = \"{cve['desc']}\"\n  condition:\n    $a\n}}"
