# Build the image:
docker-compose -f docker-compose.yml up -d --build

# Run the container:
docker-compose up -d

# Check for errors in the logs if this doesn't work via 
docker-compose logs -f

# Bring down the development containers (and the associated volumes with the -v flag):
docker-compose down -v

# To see the ip of container
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_name_or_id
# To remove all images & containers, or use 2nd for removing cache ie cleans the builder cache entirely, which will cause a full rebuild on the next run of docker-compose up
docker system prune --all --force
docker builder prune

# Automate key gen
HOSTNAME=$(hostname) ; yes | ssh-keygen -t rsa -C "$HOSTNAME" -f "$HOME/.ssh/id_rsa" -P "" && cat ~/.ssh/id_rsa.pub

# Admin has to go inside docker & do & put it in gitlab
cat ~/.ssh/id_rsa.pub