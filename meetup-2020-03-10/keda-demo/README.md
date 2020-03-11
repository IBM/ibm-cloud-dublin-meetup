# KEDA Demo

## Helm 3 install steps

Install helm: <https://helm.sh/docs/intro/install/>

```bash
# Create namespace
oc create namespace demo
# Build image for broker-demo
cd broker-demo
make build
make release
make docker-auth
make push
# Add Helm repo
helm repo add kedacore https://kedacore.github.io/charts
# Update Helm repo
helm repo update
# Install keda Helm chart
helm install keda kedacore/keda --namespace demo
# Install broker demo
helm install broker-demo broker-demo -n demo
#keda broker
helm install keda-broker-demo keda-broker-demo -n demo
#keda jobs
helm install keda-job-demo keda-job-demo -n demo
```

## Additional Info

### KEDA

* <https://keda.sh/#>  
* <https://keda.sh/#scalers> 
* [KubeCon 2019 Session on KEDA](https://www.youtube.com/watch?v=ZK2SS_GXF-g)
* [RedHat/Microsoft Collaboration on KEDA Announcement](https://www.redhat.com/en/blog/red-hat-collaborates-microsoft-keda-enable-azure-functions-openshift)
* [KEDA 1.0 Release announcement on RedHat Blog](https://www.redhat.com/en/blog/celebrating-keda-10-providing-event-driven-scale-capability-any-container-workload)
* [KEDA 1.0 Release announcement on Microsoft Cloud Opensource Blog](https://cloudblogs.microsoft.com/opensource/2019/11/19/keda-1-0-release-kubernetes-based-event-driven-autoscaling/)

### Redis on IBM Cloud

* [General Product Info - IBM Cloud Databases for Redis](https://www.ibm.com/cloud/databases-for-redis)
* [Quick guide to IBM Cloud Databases for Redis](https://www.ibm.com/cloud/blog/announcements/a-quick-guide-to-ibm-cloud-databases-for-redis)
* [IBM Cloud - Learn Redis](https://www.ibm.com/cloud/learn/redis)
* [Redis on IBM Cloud - Getting started docs](https://cloud.ibm.com/docs/services/databases-for-redis?topic=databases-for-redis-getting-started)


