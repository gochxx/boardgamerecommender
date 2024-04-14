import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import joblib
from sklearn.metrics.pairwise import euclidean_distances

def queryReco (recoInputs):
    inputdata = pd.read_pickle("data/recodata.pkl")

    inputdata = pd.DataFrame([[0]*len(inputdata.columns)], columns=inputdata.columns)

    inputdata["yearpublished"] = recoInputs["yearpublished"]
    inputdata["playingtime"] = recoInputs["playingtime"]
    inputdata["age"] = recoInputs["age"]
    for x in recoInputs["sub"]:
        inputdata[x]=1
    for x in recoInputs["cat"]:
        inputdata[x]=1
    for x in recoInputs["mec"]:
        inputdata[x]=1

    pca_cat = joblib.load('data/pca_cat.pkl')
    ncomp = pca_cat.n_components_ 
    categories_pca = pd.DataFrame(pca_cat.transform(inputdata[[x for x in inputdata.columns if x[:4]=="cat_"]]), columns=["catp_" + str(x) for x in range(ncomp)])

    pca_mec = joblib.load('data/pca_mec.pkl')
    ncomp = pca_mec.n_components_ 
    mechanic_pca = pd.DataFrame(pca_mec.transform(inputdata[[x for x in inputdata.columns if x[:4]=="mec_"]]), columns=["mecp_" + str(x) for x in range(ncomp)])

    allfeat = ['yearpublished', 'playingtime', 'age', 'sub_AbstractGames', 'sub_CustomizableGames', 'sub_FamilyGames', 
           'sub_PartyGames', 'sub_StrategyGames', 'sub_ThematicGames', 'sub_Wargames'] 
    for x in allfeat:
        scaler = joblib.load(f'data/scaler_{x}.pkl')
        inputdata[x] = scaler.transform(inputdata[x].values.reshape(-1, 1))

    y_test = inputdata[allfeat].copy()
    y_test = pd.concat([y_test,categories_pca], axis=1)
    y_test = pd.concat([y_test,mechanic_pca], axis=1)

    x_train = joblib.load('data/x_train.pkl')
    recos = pd.DataFrame(euclidean_distances( x_train, y_test))
    bgdata = pd.read_pickle("data/bg_data20240412.pkl")

    recos = pd.concat([recos, bgdata["name"]], axis=1)
    return (recos.sort_values(0).iloc[:10,1].to_list())


myInputs = {"yearpublished": 2020, "playingtime": 60, "age": 10, 
            "sub": ["sub_StrategyGames"], 
              "cat": ["cat_CardGame", "cat_ScienceFiction", "cat_Dice", "cat_Animals"], 
              "mec": ["mec_DiceRolling", "mec_ModularBoard"]}

print(queryReco (myInputs))
