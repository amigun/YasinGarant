# YasinGarant

## How to start
```
>>> docker build -t yasingarant .
>>> docker run --rm -v resource:/usr/src/app/resources yasingarant
```

### If you get error ```Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?```, you should can:
```
>>> systemctl start docker
```
