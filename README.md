# List Services as Internal DNS Entry Points

To obtain information about services and their internal DNS entry points within a specific namespace, follow these simple steps:

```bash
    chmod +x get_svc_dns.py
   ./get_svc_dns.py <namespace>
```

---

### Example

```shell
./get_svc_dns.py kube-prometheus
{
  "alertmanager-operated": [
    "alertmanager-operated.kube-prometheus.svc.cluster.local:9093",
    "alertmanager-operated.kube-prometheus.svc.cluster.local:9094",
    "alertmanager-operated.kube-prometheus.svc.cluster.local:9094"
  ],
  "monitoring-kube-prometheus-alertmanager": [
    "monitoring-kube-prometheus-alertmanager.kube-prometheus.svc.cluster.local:9093",
    "monitoring-kube-prometheus-alertmanager.kube-prometheus.svc.cluster.local:8080"
  ],
  "monitoring-kube-prometheus-operator": [
    "monitoring-kube-prometheus-operator.kube-prometheus.svc.cluster.local:443"
  ],
  "monitoring-kube-prometheus-prometheus": [
    "monitoring-kube-prometheus-prometheus.kube-prometheus.svc.cluster.local:9090",
    "monitoring-kube-prometheus-prometheus.kube-prometheus.svc.cluster.local:8080"
  ],
  "monitoring-kube-state-metrics": [
    "monitoring-kube-state-metrics.kube-prometheus.svc.cluster.local:8080"
  ],
  "monitoring-prometheus-node-exporter": [
    "monitoring-prometheus-node-exporter.kube-prometheus.svc.cluster.local:9100"
  ],
  "prometheus-operated": [
    "prometheus-operated.kube-prometheus.svc.cluster.local:9090"
  ]
}
```
