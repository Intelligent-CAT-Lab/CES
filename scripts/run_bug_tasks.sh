MODEL=$1
DATASET=$2
CACHE=$3
## Run Bug Repair
python src/bug_related_tasks/br.py --model $MODEL --dataset $DATASET --cache $CACHE --add_tests
python src/bug_related_tasks/test_br.py --model $MODEL --dataset $DATASET
## Run Bug Prediction
python src/bug_related_tasks/bp.py --model $MODEL --dataset $DATASET --cache $CACHE --add_tests
python src/bug_related_tasks/test_bp.py --model $MODEL --dataset $DATASET
## Run Bug Localization
python src/bug_related_tasks/bl.py --model $MODEL --dataset $DATASET --cache $CACHE --add_tests
python src/bug_related_tasks/test_bl.py --model $MODEL --dataset $DATASET
## Run CES
python src/ces/run.py --model $MODEL --dataset $DATASET --cache $CACHE
python src/ces/parse_results.py --model $MODEL --dataset $DATASET
python src/ces/evaluate.py --model $MODEL --dataset $DATASET