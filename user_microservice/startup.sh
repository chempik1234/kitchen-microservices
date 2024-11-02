# TODO: start grpc
alembic upgrade head
uvicorn src.main:app --reload --port=$PORT --host=0.0.0.0
echo susickkk