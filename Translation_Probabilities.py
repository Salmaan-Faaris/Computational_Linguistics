from collections import defaultdict

parallel_corpus = [
    (["i", "like", "mango"], ["എനിക്ക്", "മാമ്പഴം", "ഇഷ്ടമാണ്"]),
    (["i", "like", "apple"], ["എനിക്ക്", "ആപ്പിൾ", "ഇഷ്ടമാണ്"]),
    (["she", "eats", "rice"], ["അവൾ", "അരി", "കഴിക്കുന്നു"]),
    (["she", "eats", "mango"], ["അവൾ", "മാമ്പഴം", "കഴിക്കുന്നു"]),
    (["they", "play", "football"], ["അവർ", "ഫുട്ബോൾ", "കളിക്കുന്നു"]),
]


english_vocab = set()
mal_vocab = set()
for e_sent, m_sent in parallel_corpus:
    english_vocab.update(e_sent)
    mal_vocab.update(m_sent)


p_fe = defaultdict(lambda: defaultdict(float))  # P(f|e)
p_ef = defaultdict(lambda: defaultdict(float))  # P(e|f)

for e_sent, m_sent in parallel_corpus:
    for e in e_sent:
        for f in m_sent:
            p_fe[e][f] += 1.0
            p_ef[f][e] += 1.0


for e in p_fe:
    total = sum(p_fe[e].values())
    for f in p_fe[e]:
        p_fe[e][f] /= total

for f in p_ef:
    total = sum(p_ef[f].values())
    for e in p_ef[f]:
        p_ef[f][e] /= total


print("Translation probabilities P(f|e):")
for e in p_fe:
    print(f"\nEnglish word: '{e}'")
    for f, prob in sorted(p_fe[e].items(), key=lambda x: -x[1]):
        print(f"  P({f}|{e}) = {prob:.3f}")

print("\n" + "="*50)
print("Translation probabilities P(e|f):")
for f in p_ef:
    print(f"\nMalayalam word: '{f}'")
    for e, prob in sorted(p_ef[f].items(), key=lambda x: -x[1]):
        print(f"  P({e}|{f}) = {prob:.3f}")
