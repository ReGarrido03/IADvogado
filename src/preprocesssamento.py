# Integrantes:
# Gustavo Fugulin Soares da Silva - RA 10418552
# Otto Martins Mota - RA 10418170
# Renan Garrido - RA 10417093
# Rodrigo Roveratti Guerrero - RA 10417090

import re
import pandas as pd


def limpar_texto(texto: str) -> str:
    texto = texto.lower()
    texto = re.sub(r"\s+", " ", texto)
    texto = re.sub(r"[^\w\sà-úÀ-Ú.,;:!?()-]", "", texto)
    return texto.strip()


def carregar_dataset(caminho_arquivo: str) -> pd.DataFrame:
    df = pd.read_csv(caminho_arquivo, encoding="utf-8")
    df["texto_limpo"] = df["texto_original"].apply(limpar_texto)
    return df


if __name__ == "__main__":
    caminho = "../dataset/dados_juridicos.csv"
    df = carregar_dataset(caminho)

    print("Dataset carregado com pré-processamento:")
    print(df[["id", "tipo_texto", "texto_original", "texto_limpo"]].head())
