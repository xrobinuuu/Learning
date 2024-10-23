def maxNumberOfBalloons(text: str):
    vst = dict(zip("balloon", [0] * 7))
    for i in text:
        if i in vst:
            vst[i] += 1
    vst["l"] = vst["l"] // 2
    vst["o"] = vst["o"] // 2
    print(vst)
    return min(vst.values())


if __name__ == "__main__":
    Text = "loonbalxballpoon"
    y = maxNumberOfBalloons(Text)
    print(y)
