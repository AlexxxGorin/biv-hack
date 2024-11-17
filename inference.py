import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification, pipeline

MODEL_DIR = "./turbo_bert"
INPUT_PATH = "./payments_main.tsv"
OUTPUT_PATH = "./output.tsv"

def predict(input_file: str, output_file: str):
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
    predict(INPUT_PATH, OUTPUT_PATH)
