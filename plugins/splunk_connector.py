def find_assets_for_cve(cve):
    if "apache" in cve["desc"].lower():
        return ["host-web-01", "host-web-02"]
    return ["host-core-01"]
