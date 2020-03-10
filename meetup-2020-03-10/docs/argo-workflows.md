## Docs
* <https://argoproj.github.io/docs/argo/docs/getting-started.html>
* <https://www.kubeflow.org/docs/pipelines/pipelines-quickstart/>

## Demo Steps

From command line:
```
oc login --token=***** --server=https://c100-e.eu-gb.containers.cloud.ibm.com:30516
oc apply -f https://gitlab.com/opendatahub/opendatahub-operator/raw/v0.5.1/deploy/crds/argo-crd.yaml
brew install argoproj/tap/argo
argo version
$ oc project
Using project "opendatahub-meetup" on server "https://c100-e.eu-gb.containers.cloud.ibm.com:30516".
argo submit --watch https://raw.githubusercontent.com/argoproj/argo/master/examples/hello-world.yaml
Name:                hello-world-7dwxm
Namespace:           opendatahub-meetup
ServiceAccount:      default
Status:              Running
Created:             Mon Mar 09 09:57:52 +0000 (6 seconds ago)
Started:             Mon Mar 09 09:57:52 +0000 (6 seconds ago)
Duration:            6 seconds

STEP                             PODNAME            DURATION  MESSAGE
 ◷ hello-world-7dwxm (whalesay)  hello-world-7dwxm  6s        ContainerCreating
  525  history 
```
See workflow running in the UI:

<img width="1210" alt="image" src="https://media.github.ibm.com/user/7080/files/99478a00-61ec-11ea-9e51-3be99074b281">

Workflow completed:
<img width="1127" alt="image" src="https://media.github.ibm.com/user/7080/files/1e32a380-61ed-11ea-8e9d-19678d3b1b78">

Workflow container logs:
<img width="519" alt="image" src="https://media.github.ibm.com/user/7080/files/360a2780-61ed-11ea-958d-8ff2bba20983">

More complext sample:
<img width="552" alt="image" src="https://media.github.ibm.com/user/7080/files/6eaa0100-61ed-11ea-8666-e83f557b8fb7">
<img width="1176" alt="image" src="https://media.github.ibm.com/user/7080/files/ad3fbb80-61ed-11ea-92b3-bf8c770a8d8b">
