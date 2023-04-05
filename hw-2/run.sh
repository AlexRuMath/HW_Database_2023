MONGODB_VERSION=6.0-ubi8
docker run --name mongodb -d -p 27017:27017 -v ${PWD}/dataset:/dataset:ro mongodb/mongodb-community-server:$MONGODB_VERSION
docker exec -it mongodb mongoimport --db article_db --collection article_collection --type csv --file ./dataset/test.csv --headerline