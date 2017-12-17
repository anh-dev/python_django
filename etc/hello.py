import multiproccessing

bind = '0.0.0.0:8080'
workers = multiproccessing.cpu_count() * 2 + 1
