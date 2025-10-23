DATASET=$1
python src/prime_path_extraction/get_prime_path.py $DATASET
python src/prime_path_extraction/create_prime_path_json.py $DATASET