# functions-from-zero
Live Training

[![Python application test with Github Actions](https://github.com/AlphaNerdFx/functions-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/AlphaNerdFx/functions-from-zero/actions/workflows/main.yml)

### To call Microservice
Use code with the following format
```bash
curl -X 'POST' \
  'http://0.0.0.0:8080/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Microsoft",
  "length": 3
}'
```

### Build container
```
docker build -t myapp:latest
```

```
docker image ls
```

### Run container
```
docker run -p 127.0.0.1:8080:8080 <image_tag>
```

### Invoke POST request
run `invoke.sh`