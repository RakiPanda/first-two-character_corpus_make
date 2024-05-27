import pandas as pd

# ファイルの読み込み
file_path = 'unigram_freq.csv'
df = pd.read_csv(file_path)

# データフレームの 'word' 列に float 値が含まれている可能性があるため、文字列に変換してからペアを作成
df['word'] = df['word'].astype(str)

# 最初の2文字と元の単語のペアを作成
pairs = df['word'].apply(lambda x: f"{x[:2]}/{x}")

# 結果をファイルに保存する関数
def save_pairs_to_file(pairs, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for pair in pairs:
            file.write(f"{pair}\n")

# 結果をファイルに保存
output_file = 'first-two-char_corpus.txt'
save_pairs_to_file(pairs, output_file)
