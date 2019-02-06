docker run -d --name=gra --network licen --network-alias grafana -p 3000:3000 grafana/grafana
docker run -d --name=inf --network licen --network-alias influx -p 8086:8086 influxdb
docker run -td --name=py --network licen --network-alias py -v $(pwd):/home python:3.6