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


## Concentrated commands
- ```kubectl get pod``` for getting all the pod
- ```kubectl get pod -o wide``` for getting all the pod with more details
- ```kubectl describe pod <pod_name>``` for getting the details of a pod
- ```kubectl delete pod <pod_name>``` for deleting a pod
- ```kubectl run <pod_name> --image=<image_name>``` for creating a pod with specific image
- ```kubectl get deployment``` for getting all the deployment
- ```kubectl get deployment -o wide``` for getting all the deployment with more details
- ```kubectl describe deployment <deployment_name>``` for getting the details of a deployment
- ```kubectl delete deployment <deployment_name>``` for deleting a deployment
- ```kubectl exec -it my-connor-app-deployment -- curl http://localhost:30001/health``` for executing a command in a pod
- ```kubctl create deployment <deployment_name> --image=<image_name>``` for creating a deployment with specific image
- ```kubectl scale --replicas=<number_of_replicas> deployment/<deployment_name>``` for scaling a deployment
- ```kubectl get service``` for getting all the service
- ```kubectl get service -o wide``` for getting all the service with more details
- ```kubectl describe service <service_name>``` for getting the details of a service
- ```kubectl delete service <service_name>``` for deleting a service
- ```kubectl expose deployment <deployment_name> --type=NodePort --port=<port_number>``` for exposing a deployment
- ```kubectl get all``` for getting all the resources
- ```kubectl get all -o wide``` for getting all the resources with more details
- ```kubectl describe all``` for getting the details of all the resources
- ```kubectl delete all --all``` for deleting all the resources
- ```kubectl apply -f <file_name>``` for applying a file
- ```kubectl delete -f <file_name>``` for deleting a file
- 