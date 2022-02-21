import json
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv(r"C:\Users\toanp\Downloads\PBMC-LT_Corrlmatrix.txt", sep="\t")
    with open("data.json", "rb") as j:
        data = json.load(j)

        affected_list = set()

        for k in data:
            for i in data[k].split(","):
                i = i.strip()
                affected_list.add(i)

        for i, r in df.iterrows():
            if r["T: Gene names"] in affected_list:
                df.at[i, "Lysotag"] = "+"
                print(r["T: Gene names"])
    df.to_csv("lysotagged.txt", sep="\t", index=False)

