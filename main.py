from plugins import threat_parser, splunk_connector, yara_generator, edr_mock
from planner.planner import get_plan
from executor import soar_mock, notify_slack
from memory.vector_store import store

feed = threat_parser.parse_feed()

for cve in feed:
    plan = get_plan(cve)
    print(f"🧠 Plan for {cve['cve']}:\n{plan}\n")

    hosts = splunk_connector.find_assets_for_cve(cve)
    yara = yara_generator.generate_yara_rule(cve)

    # Store to memory
    store(cve["desc"], cve["cve"])

    # Action
    soar_mock.create_ticket(cve, hosts, yara)
    edr_mock.isolate_hosts(hosts)
    notify_slack.notify(f"📣 {cve['cve']} mitigated on {', '.join(hosts)}")
