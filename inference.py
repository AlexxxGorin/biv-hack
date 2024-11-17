import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification, pipeline
import argparse

MODEL_DIR = "Deenchik/bert-turbo-biv"

def predict(input_file: str, output_file: str):
    # Загрузка модели
    model = pipeline(task="text-classification", model=MODEL_DIR)

    # Загрузка входного файла
    data = pd.read_csv(input_file, sep="\t")

    predictions = list(map(lambda x: x['label'], model(data.iloc[:, 3].to_list()))) 

    result_df = pd.DataFrame({
        0: data.iloc[:, 0].values,
        1: predictions
    })

    # Сохранение результата в выходной файл
    result_df.to_csv(output_file, sep="\t", index=False, header=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run inference on TSV file.")
    parser.add_argument("input_file", type=str, help="Path to the input TSV file.")
    parser.add_argument("output_file", type=str, help="Path to the output TSV file.")
    args = parser.parse_args()

    predict(args.input_file, args.output_file)
