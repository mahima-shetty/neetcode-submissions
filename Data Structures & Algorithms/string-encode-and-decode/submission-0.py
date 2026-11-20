class Solution:
    def encode(self, s: List[str]) -> str:
        if not s:
            return ""
        sizes, res = [], []

        for item in s:
            sizes.append(len(item))

        for i in sizes:
            res.append(str(i))
            res.append(",")
        res.append("#")

        for item in s:
            res.append(item)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res = [], []
        i = 0
        while s[i] != "#":
            j = i
            while s[j] != ",":
                j += 1
            sizes.append(int(s[i:j]))
            i = j + 1
        i += 1
        for sz in sizes:
            res.append(s[i : i + sz])
            i += sz
        return res
