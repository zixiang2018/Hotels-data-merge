docker image build -t hotel-api .
docker container run -d --name hotel_api -p 5000:5000 hotel-data-merge