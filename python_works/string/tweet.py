tweet="what a game hats off both teams Well done @benstokes38 @pattcummins30 you have bought test cricket back to life love test cricket @TheBarmyArmy @CricketAus @ECB_cricket"

words=tweet.split(" ")

for w in words:
    if w.startswith("@"):
        print(w)