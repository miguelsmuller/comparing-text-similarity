import sys

from sentence_transformers import SentenceTransformer, util
from thefuzz import fuzz
from torch import Tensor


def compare_with_model(text1: str, text2: str):
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    embedding_1: Tensor = model.encode(text1, convert_to_tensor=True)
    embedding_2: Tensor = model.encode(text2, convert_to_tensor=True)

    similarity = util.pytorch_cos_sim(embedding_1, embedding_2)[0][0].item()

    return similarity


def compare_with_fuzz(text1: str, text2: str):
    similarity = fuzz.ratio(text1, text2) / 100

    return similarity


if len(sys.argv) != 3:
    print("Please provide exactly two sentences as arguments.")
    sys.exit(1)

sentence1 = sys.argv[1]
sentence2 = sys.argv[2]

model_similarity = compare_with_model(sentence1, sentence2)
fuzz_similarity = compare_with_fuzz(sentence1, sentence2)

print("Sentence Transformers:", model_similarity)
print("Fuzzy:", fuzz_similarity)
