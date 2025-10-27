MODEL=$1
DATASET=$2
CACHE=$3

python src/ces/run.py --model $1 --dataset $2 --cache $3
python src/ces/parse_results.py --model $1 --dataset $2
python src/ces/evaluate.py --model $1 --dataset $2
python src/ces/print_results.py --model $1 --dataset $2