# prometheus_clearwater
Monitoring de l'implémentation ClearWater de VIMS avec Prometheus, Grafana est les Exporters
Prometheus: Outils de monitoring
Grafana: Donne une meuilleur visualisation des sorties de Promeutheus
Exporter:va nous permettre de superviser et de générer des métriques de nos services externes. Ils servent à mésurer:
  -les requêttes http ;
  -etc.

Comment lancer les serveurs?
-lancer prémièrement grafana ou blackbox-exporter avec les commandes:
"docker run -it --rm -d --name grafana -p 3000:3000  grafana/grafana" et " docker run -it --rm --name blackbox-exporter -p 9115:9115 -v /opt/docker/blackbox-exporter/config:/config prom/blackbox-exporter:v0.12.0 --config.file=/config/blackbox.yml"

- et en dernier position, lancer Prometheus avec la commande:
"docker run --rm -ti  --name prometheus -p 9090:9090 -v /opt/docker/prometheus:/etc/prometheus prom/prometheus --config.file=/etc/prometheus/prometheus.yml"

