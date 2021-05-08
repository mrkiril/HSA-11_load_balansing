MAIN_SERVICE = projector_nginx_loadbalanser


up:
	docker-compose up -d
	docker-compose ps

run:
	docker-compose build --parallel --no-cache
	docker-compose up -d
	docker-compose ps

restart:
	docker-compose restart $(MAIN_SERVICE)
	docker-compose ps

rebuild:
	#sudo -S rm -rf ./nginx/cache/*
#	echo "" > ./nginx/log/projector.access.log
#	echo "" >  ./nginx/log/projector.error.log
#	echo "" > ./nginx/log/error.log
#	echo "" >  ./nginx/log/access.log
	docker-compose build --parallel
	docker-compose up -d
	docker-compose ps

