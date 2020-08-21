#!/usr/bin/env bash

docker exec backend pip check &&
docker exec backend ./src/manage.py check &&
docker exec backend ./src/manage.py makemigrations --check --dry-run &&
docker exec backend ./src/manage.py validate_templates &&
docker-compose -f docker-compose.yml config --quiet &&
docker exec nginx nginx -t &&
docker exec -it backend flake8 ./src &&
docker exec -it backend pytest ./src/tests -s -vv -x --create-db --cov-fail-under=15
