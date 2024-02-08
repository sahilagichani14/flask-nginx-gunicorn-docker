# Build the image:
docker-compose -f docker-compose.yml up -d --build

# Run the container:
docker-compose up -d

# Check for errors in the logs if this doesn't work via 
docker-compose logs -f

# Bring down the development containers (and the associated volumes with the -v flag):
docker-compose down -v
