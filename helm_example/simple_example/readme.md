[Example can be found here](https://helm.sh/docs/chart_template_guide/getting_started/)
# Commands has been run
## A Starter Chart
For this guide, we'll create a simple chart called mychart, and then we'll create some templates inside of the chart.
### creating first chart
```
$ helm create mychart
```
### result of running the command
```
$ ls -Rt

charts  templates  values.yaml  Chart.yaml
./charts:
./templates:
tests  NOTES.txt  _helpers.tpl  hpa.yaml  service.yaml  serviceaccount.yaml  deployment.yaml  ingress.yaml
./templates/tests:
test-connection.yaml
```
### what they are
- NOTES.txt: The "help text" for your chart. This will be displayed to your users when they run helm install.
- deployment.yaml: A basic manifest for creating a Kubernetes deployment
- service.yaml: A basic manifest for creating a service endpoint for your deployment
- _helpers.tpl: A place to put template helpers that you can re-use throughout the chart

## simple example
- create configmap.yaml under /helm_example/mychart/templates
```
apiVersion: v1
kind: ConfigMap
metadata:
  name: mychart-configmap
data:
  myvalue: "Hello World"
```
- run ```helm install full-coral ./mychart``` to install the chart
  - minikube might not been started, try ```minikube start``` to start minikube
  - use ```helm get manifest full-coral``` to see the manifest
  - use ```helm uninstall full-coral``` to uninstall the chart

## little more complex example
- update configmap.yaml under /helm_example/mychart/templates
```
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-configmap
data:
  myvalue: "Hello World"
```
- run ```helm install clunky-serval ./mychart``` to install the chart
- notice the name "clunky-serval" in the manifest
```
---
# Source: mychart/templates/configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: clunky-serval-configmap
data:
  myvalue: "Hello World"
```
- lets retry with a different name ```helm install --debug --dry-run good-guppy ./mychart```


## Concentrated commands
- ```helm create <chart_name>``` for creating a chart
- ```helm install <release_name> <chart_name>``` for installing a chart
- ```helm get manifest <release_name>``` for getting the manifest of a release
- ```helm uninstall <release_name>``` for uninstalling a release
- ```helm install --debug --dry-run <release_name> <chart_name>``` for installing a chart with debug and dry-run mode
- ```helm list``` for listing all the releases
