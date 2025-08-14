oc  apply -f Secret.yaml
oc  apply -f ConfigMap.yaml

oc apply -f mysql-deployment.yaml
oc apply -f mysql-service.yaml

oc apply -f sql-pvs.yaml

docker build -t mypostgres .



