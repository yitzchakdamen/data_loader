oc  apply -f Secret.yaml
oc  apply -f ConfigMap.yaml

oc apply -f mysql-deployment.yaml
oc apply -f mysql-service.yaml

oc apply -f sql-pvs.yaml

docker build -t data_loader .
docker tag data_loader yitzchakdamen/data_loadr:v2
docker push yitzchakdamen/data_loadr:v2

oc apply -f data_loader-deployment.yaml
oc apply -f data_loader-service.yaml
oc  expose service/data-loader