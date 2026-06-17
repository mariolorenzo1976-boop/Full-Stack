from core import *
from data import *

def stadistic():

    apy_clean_data = clean_data(data)
    
    apy_acumulator_user = acumulator_for_km("user",apy_clean_data)
    apy_acumulator_sport = acumulator_for_km("sport",apy_clean_data)

    apy_top_user = top_for_km("user", apy_acumulator_user)
    apy_top_sport = top_for_km("sport", apy_acumulator_sport)

    



    return apy_acumulator_user, apy_acumulator_sport, apy_top_user, apy_top_sport