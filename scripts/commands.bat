

oc  apply -f Secret.yaml
oc  apply -f ConfigMap.yaml


----
mysql

oc apply -f mysql-pvs.yaml
oc apply -f mysql-deployment.yaml
oc apply -f mysql-service.yaml

----

app-docker

docker build -t data_loader .
docker tag data_loader yitzchakdamen/data_loadr:v4.4
docker push yitzchakdamen/data_loadr:v4.4


app-k8s

oc apply -f data_loader-deployment.yaml
oc apply -f data_loader-service.yaml
oc  expose service/data-loader-service

-----

mongo

oc apply -f mongo-pvs.yaml
oc apply -f mongo-deployment.yaml
oc apply -f mongo-service.yaml

