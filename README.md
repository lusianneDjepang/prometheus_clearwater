# prometheus_clearwater
Monitoring de l'implémentation ClearWater de VIMS avec Prometheus, Grafana est les Exporters
Prometheus: Outils de monitoring
Grafana: Donne une meuilleur visualisation des sorties de Promeutheus
Container-Exporter:va nous permettre de superviser et de générer des métriques de nos services externes. Ils servent à mésurer:
  -les requêttes http ;
  -etc.

Comment lancer les serveurs?
-lancer prémièrement grafana ou container-exporter avec les commandes:
"docker run -it --rm -d --name grafana -p 3000:3000  grafana/grafana" et " docker run -p 9104:9104 -v /sys/fs/cgroup:/cgroup            -v /var/run/docker.sock:/var/run/docker.sock prom/container-exporter"

- et en dernier position, lancer Prometheus avec la commande:
"docker run --rm -ti  --name prometheus -p 9090:9090 -v /opt/docker/prometheus:/etc/prometheus prom/prometheus --config.file=/etc/prometheus/prometheus.yml"

