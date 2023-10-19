# k8s
## Architecture
- Control plane, master node
  - api server, entrypoint to k8s cluster
  - controller manager, watches state of cluster
  - scheduler, schedules workloads to nodes, manages resources
  - etcd, key value store, stores cluster state
- Virtual Network
  - CNI, container network interface
  - Flannel, vxlan
  - Calico, bgp
  - Weave, vxlan
  - Cilium, eBPF
- Multiple worker nodes
  - higher workload
  - much bigger and more resouses

## Main Kubernetes Components
- pod
  - pod is the smallest and simplest unit in the Kubernetes object model that you create or deploy
  - abstraction over container
  - usually one container per pod
  - pod is a group of one or more containers, with shared storage and network resources, and a specification for how to run the containers
  - each pod is assigned a unique IP address
  - new ip address on creation
- configMap
  - configMap is an API object used to store non-confidential data in key-value pairs
- StatefulSet
  - statefulset is a workload API object used to manage stateful applications
- service
- secret
- deployment
- ingress
  - ingress is a collection of rules that allow inbound connections to reach the cluster services
- DaemonSet
  - DaemonSet is a workload API object that you can use to create a Pod that runs on all selected nodes
- vol
  - persistent volume

## statefullset vs statelessset
- DB are often hosted outside of k8s

- http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#/login

```
eyJhbGciOiJSUzI1NiIsImtpZCI6IkpWeTB0MjJrUXJ0XzFVMl9vamQ1dzVmU0FMSW5LQUNvRGxZa1VnZjdiclkifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNjk1NDQyNjMyLCJpYXQiOjE2OTU0MzkwMzIsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJrdWJlcm5ldGVzLWRhc2hib2FyZCIsInNlcnZpY2VhY2NvdW50Ijp7Im5hbWUiOiJhZG1pbi11c2VyIiwidWlkIjoiODczMDA2ZDAtY2VlYy00NTE5LWFjN2QtOTdjZjU0NmEwMjNlIn19LCJuYmYiOjE2OTU0MzkwMzIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDprdWJlcm5ldGVzLWRhc2hib2FyZDphZG1pbi11c2VyIn0.hXl3E8Fy88SzCFNFoavNlm6I6SZ7ptr2O917CpxHBk6wMvETh40JKT2zM0SdzOFccFjJYKUmZlWGgotULedbU4wbjwYVINV-q4aJpxzm-TZ8QuTGV3xB2Jo6Q0O3PjgCeVuYt8ZLANCeyf-RgrH50gZW67_PtN91AvIRask8O7cpuDPh7mk7MvKTHLjg2aHbVjn_VUtOwXYBHFY67IC9G5GhVWkQ-SK7JhAAG4P14kCiWtExAjOqSmCj0ZUZtQXbSC2yLhn3gKzT1O5OLQRqiDrTBSZRijxA1DC1VEARJjwEI9WH3Q0xdGt3HV9NJWeL52HwHlvB7SxQjGjyNjcokg
```

