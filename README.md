# prometheus_clearwater
Monitoring and implamentation of __VIMS-ClearWater__ wich __Prometheus__, __Grafana__ and __containers-Exporters__

----------------
## Prerequisites
To start you need to install [__docker__ and __docker-compose__](https://websiteforstudents.com/how-to-install-docker-and-docker-compose-on-ubuntu-16-04-18-04/)

## Getting Started


Comment lancer les serveurs?
-lancer prémièrement grafana ou container-exporter avec les commandes:
"docker run -it --rm -d --name grafana -p 3000:3000  grafana/grafana" et " docker run -p 9104:9104 -v /sys/fs/cgroup:/cgroup            -v /var/run/docker.sock:/var/run/docker.sock prom/container-exporter"

- et en dernier position, lancer Prometheus avec la commande:
"docker run --rm -ti  --name prometheus -p 9090:9090 -v /opt/docker/prometheus:/etc/prometheus prom/prometheus --config.file=/etc/prometheus/prometheus.yml"

# Contributing

We'd love for you to contribute to this container. You can request new features by creating an issue, or submit a pull request with your contribution.

