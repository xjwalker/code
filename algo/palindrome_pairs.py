def palindrome_pairs(words: list):
    if type(words) is not type([]) or len(words) == 1:
        return []

    candidates = {}
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if words[i] + words[j] not in candidates:
                candidates[words[i] + words[j]] = (i, j)
            if words[j] + words[i] not in candidates:
                candidates[words[j] + words[i]] = (i, j)

    palindromes = []
    for candidate in candidates:
        if candidate == candidate[::-1]:
            palindromes.append(candidate)

    return palindromes


def palindrome_pairs_gpt(words: list) -> list:
    if not isinstance(words, list) or len(words) < 2:
        return []

    palindromes = []
    word_indices = {word: i for i, word in enumerate(words)}

    for i, word in enumerate(words):
        for j in range(len(word) + 1):
            prefix = word[:j]
            suffix = word[j:]
            reversed_prefix = prefix[::-1]
            reversed_suffix = suffix[::-1]

            if j > 0 and prefix == reversed_prefix:
                reversed_suffix_index = word_indices.get(reversed_suffix, -1)
                if reversed_suffix_index != i:
                    palindromes.append([reversed_suffix +  word])

            if suffix == reversed_suffix:
                reversed_prefix_index = word_indices.get(reversed_prefix, -1)
                if reversed_prefix_index != i:
                    palindromes.append([word + reversed_prefix])

    return palindromes


def main():
    words = ['car', 'race']
    print(palindrome_pairs(words))
    words = ['car', 'racece']
    print(palindrome_pairs(words))
    words = ['gab', 'cat', 'bag', 'alpha']
    print(palindrome_pairs(words))
    words = ['run', 'nu']
    print(palindrome_pairs(words))
    print(palindrome_pairs('words'))
    print(palindrome_pairs([]))

    words = ['car', 'race']
    print(palindrome_pairs_gpt(words))
    words = ['car', 'racece']
    print(palindrome_pairs_gpt(words))
    words = ['gab', 'cat', 'bag', 'alpha']
    print(palindrome_pairs_gpt(words))
    words = ['run', 'nu']
    print(palindrome_pairs_gpt(words))


if __name__ == '__main__':
    main()
