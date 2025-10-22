DATASET=$1
python src/data_extraction/branch_extraction.py --dataset $DATASET
python src/data_extraction/condition_extraction.py --dataset $DATASET
python src/data_extraction/loop_extraction.py --dataset $DATASET
python src/data_extraction/extract_if.py --dataset $DATASET