### OpenCV and ZeroMQ with Docker
- Based on [Harr Cascade by OpenCV](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html)

### Working Environment
Server
- ubuntu: 20.04
- python: 3.8
- cmake: 3.20.4
- pyzmq: 22.1.0
- opencv 4.5.2.54

Client
- ubuntu: 20.04
- python: 3.8
- pyzmq: 22.1.0

Docker Compose (Server)

Camera Window
```sh
environment: 
      - DISPLAY=$DISPLAY

```
Camera
```sh
devices: 
      - /dev/video0:/dev/video0
```

### Usage
Start the docker-compose !
```sh
docker-compose up
```