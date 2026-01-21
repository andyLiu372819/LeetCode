def findSubstring(s: str, words: list[str]) -> list[int]:
    res = []
    d = {}
    word_len = len(words[0])
    num = len(words)
    n = len(s)
    for i in words:
        if not i in d:
            d[i] = 1
        else:
            d[i] += 1

    for i in range(word_len):
        seen = d.copy()
        left, right = i, i
        count = 0

        while right + word_len <= n:
            temp_word = s[right: right + word_len]
            right += word_len

            if temp_word in seen:
                seen[temp_word] -= 1
                count += 1

                while seen[temp_word] < 0:
                    left_temp_word = s[left: left + word_len]
                    seen[left_temp_word] += 1
                    left += word_len
                    count -= 1

                if count == num:
                    res.append(left)
            else:
                seen = d.copy()
                count = 0
                left = right
    return res


if __name__ == "__main__":
    s = "abaababbaba"
    words = ["ab", "ba", "ab", "ba"]
    print(findSubstring(s, words))