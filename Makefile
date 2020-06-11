clean:
	-find -name "*.un~" -exec rm {} \;
	-find -name "*.swp" -exec rm {} \;
	-find -name "*.pyc" -exec rm {} \;
	-find -name "*.pickle" -exec rm {} \;

run:
	python3 src/app.py

test:
	python3 -m pytest tests

docker_run: docker_image_remove_dangling
	docker build -t toy-web-server -f docker/Dockerfile .
	docker run -it --rm -p 8070:8070 --name toy-server toy-web-server python3 ./src/app.py

docker_test: docker_image_remove_dangling
	docker build -t toy-web-server -f docker/Dockerfile .
	docker run -it --rm -p 8070:8070 --name toy-server toy-web-server python3 -m pytest ./tests

docker_image_remove: docker_image_remove_dangling
	-docker rmi $$(docker images -q -f reference=toy-web-server)

docker_image_remove_dangling:
	-docker rmi $$(docker images -q -f dangling=true)
