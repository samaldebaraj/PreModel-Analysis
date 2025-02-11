import pandas as pd
import EDA

#BOF = pd.read_excel('data/BOF_Data.xlsx',sheet_name='1')
BOF = pd.read_csv('data/DATA.csv')
#BOF = BOF.fillna(0);
#OtherFeatures = ['GRADE','HM_SI', 'HM_P','ACT_LIME','ACT_DOLO','ACT_ORE', 'ACT_TEMP', 'TAP_TO_TAP_TIME']
eda = EDA.EDA(BOF,title='Data Analysis')
#eda.TargetAnalysis('ACT_LIME')
eda.EDAToHTML()

