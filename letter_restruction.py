import csv 
import re 
import pandas as pd
from google.colab import drive
drive.mount('/content/drive/')

# inicializando
drive_root = '/content/drive/My Drive'
data_folder = 'tickets'
input_filename = 'chats-180.csv'
output_filename = 'processed_conversasAda.csv'

# DF
input_file = os.path.join(drive_root, data_folder, input_filename)
output_file = os.path.join(drive_root, data_folder, output_filename)

chats = pd.read_csv(input_file, encoding='utf8')

# Prepare the final DataFrame to store question-answer pairs
final_data = []

# agrupando por ID
grouped_chats = chats.groupby('conversation_id')

# ittterando through each group
for chat_id, group in grouped_chats:
    questions = group[group["message_type"] == "question"]["message"].tolist()
    answers = group[group["message_type"] == "answer"]["message"].tolist()

    # Pair questions and answers
    for question, answer in zip(questions, answers):
        final_data.append({'question': question, 'answer': answer})

    # Handle any remaining questions or answers (if lists are of different lengths)
    if len(questions) > len(answers):
        for question in questions[len(answers):]:
            final_data.append({'question': question, 'answer': None})
    elif len(answers) > len(questions):
        for answer in answers[len(questions):]:
            final_data.append({'question': None, 'answer': answer})

# Convert final_data to a DataFrame
final_df = pd.DataFrame(final_data)

# Salvando no output
final_df.to_csv(output_file, index=False, encoding='utf8')

print(f"novo arquivo é: {output_file}")
