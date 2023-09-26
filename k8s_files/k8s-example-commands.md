# k8s example commands
## start all kubectls
```bash
kubectl apply -f mongo-config.yaml
kubectl apply -f mongo-secret.yaml
kubectl apply -f mongo.yaml
kubectl apply -f webapp.yaml
```

## stop all kubectls
```bash
kubectl delete -f mongo-config.yaml
kubectl delete -f mongo-secret.yaml
kubectl delete -f mongo.yaml
kubectl delete -f webapp.yaml
```

## list all existing pods
```bash
kubectl get pods
```

## create a pod with simple one
```bash
kubectl run nginx --image=nginx
```

## describe a pod
```bash
kubectl describe pod nginx
```

## get all pods
```bash
kubectl get pods -o wide
```

```
NAME                                READY   STATUS    RESTARTS   AGE    IP            NODE       NOMINATED NODE   READINESS GATES
mongo-deployment-85d45f7888-lvfzl   1/1     Running   0          42h    10.244.0.15   minikube   <none>           <none>
nginx                               1/1     Running   0          103s   10.244.0.25   minikube   <none>           <none>
webapp-deployment-f8d7df85d-6rzcb   1/1     Running   0          42h    10.244.0.16   minikube   <none>           <none>
```

## start kubectl dashboard
```bash
minikube apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0/aio/deploy/recommended.yaml
kubectl proxy
```

```bash
# kubectl change replica set
kubectl scale --replicas=3 deployment/webapp-deployment
# kubectl get all sets
kubectl get all
```

```