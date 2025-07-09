cd sealbot_webgame
#docker run --name sealbot-db -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=sealbot -p 5432:5432 -d postgres
docker start sealbot-db
poetry shell
uvicorn app.main:app --reload
