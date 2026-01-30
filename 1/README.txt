### MongoDB

You can use MongoDB Atlas or run a local MongoDB instance using Docker:

```bash
docker run -d \
  --name mongo-local \
  -p 27017:27017 \
  -v mongo_data:/data/db \
  mongo:7