MODEL=$1
DATASET=$2
CACHE=$3

python run.py --model $1 --dataset $2 --cache $3
python evaluate_new.py --model $1 --dataet $2