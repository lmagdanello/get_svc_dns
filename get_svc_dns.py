#!/usr/bin/env python3

import subprocess
import json
import sys

def get_svc_endpoint(namespace):
    try:
        cmd = f"kubectl get svc -n {namespace} -o json"
        result = subprocess.check_output(cmd, shell=True)
        service_data = json.loads(result)

        services_info = {}
        for service in service_data.get("items", []):
            service_name = service["metadata"]["name"]
            ports = []
            for port_info in service["spec"].get("ports", []):
                port_name = port_info.get("name", "N/A")
                port_number = port_info.get("port", "N/A")
                dns_and_port = f"{service_name}.{namespace}.svc.cluster.local:{port_number}"
                ports.append(dns_and_port)
            services_info[service_name] = ports

        return services_info
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./get_svc_endpoint.py <namespace>")
        sys.exit(1)

    namespace = sys.argv[1]
    service_info = get_svc_endpoint(namespace)
    print(json.dumps(service_info, indent=2))


