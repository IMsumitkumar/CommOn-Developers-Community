import os
import pickle
from asgiref.sync import sync_to_async

@sync_to_async
def toxic_classifier(data):
    data = [data]
    modulePath = os.path.dirname(__file__)


    toxic_vect = os.path.join(modulePath, 'pkl/toxic_vect.pkl')
    toxic_model = os.path.join(modulePath, 'pkl/toxic_model.pkl')

    severe_toxic_vect = os.path.join(modulePath, 'pkl/severe_toxic_vect.pkl')
    severe_toxic_model = os.path.join(modulePath, 'pkl/severe_toxic_model.pkl')

    obscene_vect = os.path.join(modulePath, 'pkl/obscene_vect.pkl')
    obscene_model = os.path.join(modulePath, 'pkl/obscene_model.pkl')

    threat_vect = os.path.join(modulePath, 'pkl/threat_vect.pkl')
    threat_model = os.path.join(modulePath, 'pkl/threat_model.pkl')

    insult_vect = os.path.join(modulePath, 'pkl/insult_vect.pkl')
    insult_model = os.path.join(modulePath, 'pkl/insult_model.pkl')

    identity_hate_vect = os.path.join(modulePath, 'pkl/identity_hate_vect.pkl')
    identity_hate_model = os.path.join(modulePath, 'pkl/identity_hate_model.pkl')

    #vector

    with open(toxic_vect, "rb") as f:
        tox = pickle.load(f)

    with open(severe_toxic_vect, "rb") as f:
        sev_tox = pickle.load(f)

    with open(obscene_vect, "rb") as f:
        obs = pickle.load(f)

    with open(threat_vect, "rb") as f:
        threat = pickle.load(f)

    with open(insult_vect, "rb") as f:
        insult = pickle.load(f)

    with open(identity_hate_vect, "rb") as f:
        hate = pickle.load(f)

    # module

    with open(toxic_model, "rb") as f:
        tox_model = pickle.load(f)

    with open(severe_toxic_model, "rb") as f:
        sev_model = pickle.load(f)

    with open(obscene_model, "rb") as f:
        obs_model = pickle.load(f)

    with open(threat_model, "rb") as f:
        threat_model = pickle.load(f)

    with open(insult_model, "rb") as f:
        insult_model = pickle.load(f)

    with open(identity_hate_model, "rb") as f:
        hate_model = pickle.load(f)

    # transform

    vect_tox = tox.transform(data)
    pred_tox = tox_model.predict_proba(vect_tox)[:,1]

    vect_sev = sev_tox.transform(data)
    pred_sev = sev_model.predict_proba(vect_sev)[:,1]

    vect_obs = obs.transform(data)
    pred_obs = obs_model.predict_proba(vect_obs)[:,1]

    vect_threat = threat.transform(data)
    pred_threat = threat_model.predict_proba(vect_threat)[:,1]

    vect_insult = insult.transform(data)
    pred_insult = insult_model.predict_proba(vect_insult)[:,1]

    vect_hate = hate.transform(data)
    pred_hate = hate_model.predict_proba(vect_hate)[:,1]

    out_tox = round(pred_tox[0], 2) * 100
    out_sev_tox = round(pred_sev[0], 2) * 100
    out_obs = round(pred_obs[0], 2) * 100
    out_threat = round(pred_threat[0], 2) * 100
    out_insult = round(pred_insult[0], 2) * 100
    out_hate = round(pred_hate[0], 2) * 100

    return out_tox, out_sev_tox, out_obs, out_threat, out_insult, out_hate
