# implement a simple rule based text tokenizer for english language using regex? 
# your tokenizer should consider punctations and special symbols as separate tokens. Contractions like is'nt should be regarded as two tokens is and nt. 
# Also identify abbreviations (Eg: USA) and internal -ation (Eg ice-cream) as single tokens.

import re

def tokenize(text):
    # Regex order matters
    token_pattern = re.compile(r"""
        (?:[A-Z]\.){2,}[A-Z]?         # Abbreviations with dots (U.S.A, U.K.)
        |[A-Z]{2,}                    # All caps words like USA, NATO
        |\w+(?:'\w+)?(?:-\w+)*        # Words with internal apostrophe or hyphens (isn't, I'm, ice-cream)
        |[.,!?;:'"(){}\[\]<>@#$%^&*_+=/\\|`~]  # punctuation and symbols
    """, re.VERBOSE)

    tokens = token_pattern.findall(text)

    final_tokens = []
    for tok in tokens:
        if "'" in tok:
            # Handle common contraction pattern n't → nt
            if tok.endswith("n't"):
                final_tokens.append(tok[:-3])  # part before n't
                final_tokens.append("nt")
            else:
                parts = tok.split("'")
                if parts[0]:
                    final_tokens.append(parts[0])
                if len(parts) > 1 and parts[1]:
                    final_tokens.append(parts[1])
        else:
            final_tokens.append(tok)

    return final_tokens


# Example usage
text = "He isn't going to the U.S.A, but loves ice-cream and USA!"
print(tokenize(text))

