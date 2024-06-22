import google.generativeai as genai
from block import *
from encode import *
import zlib
import os

gemini_api_secret_name = 'GOOGLE_API_KEY'  # @param {type: "string"}

try:
  GOOGLE_API_KEY = os.environ.get("API_KEY")
  genai.configure(api_key=GOOGLE_API_KEY)

except Exception as e:
  # unknown error
  print(f"There was an unknown error. Ensure you have a secret {gemini_api_secret_name} stored in Colab and it's a valid key from https://makersuite.google.com/app/apikey")
  raise e

with open("human.txt", "r") as file:
    dna_sequence = file.read()

text = f"""
Je travaille sur une étude épigénétique concernant l'effet d'un régime alimentaire riche en graisses sur l'expression du gène FASN (Fatty Acid Synthase) au fil du temps. Voici les données que j'ai recueillies :

1. **Séquence d'ADN étudiée** : {dna_sequence}
2. **Observation épigénétique initiale** (T0) :
   - Méthylation de l'ADN : 10% des sites CpG
   - Expression du gène : élevée

3. **Observation après 3 mois de régime riche en graisses** (T1) :
   - Méthylation de l'ADN : 40% des sites CpG
   - Expression du gène : diminuée

4. **Observation après 6 mois de régime riche en graisses** (T2) :
   - Méthylation de l'ADN : 70% des sites CpG
   - Expression du gène : fortement réduite

Je souhaite analyser ces données pour comprendre les effets épigénétiques de ce régime alimentaire. Pouvez-vous m'aider à :

1. Identifier les motifs et les tendances dans l'évolution de la méthylation de l'ADN et l'expression du gène FASN.
2. Comparer ces résultats avec d'autres études similaires pour voir si des conclusions générales peuvent être tirées.
3. Proposer des mécanismes biologiques possibles expliquant ces modifications épigénétiques.
4. Suggérer des implications potentielles pour la santé humaine, en particulier en ce qui concerne les maladies métaboliques.

Merci de fournir une analyse détaillée basée sur ces données.

"""

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

response = chat.send_message(text)
print(response.text)
with open('file.txt', 'w') as file:
    file.write(response.text)
print("File 'file.txt' has been created and written successfully.")


synthese = {
  "analyse": response.text,
  "DNA DATA": dna_to_bytes(dna_sequence)
}

print("\n--------------------------\n")
print(mine_block(synthese))