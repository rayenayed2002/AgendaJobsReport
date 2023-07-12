import pymongo
import pandas as pd
from matplotlib import pyplot as plt
from fpdf import FPDF
import numpy as np
client = pymongo.MongoClient('localhost')
db = client["admin"]
col = db["agenda"]
x = col.find()
df = pd.DataFrame(x)
df['mail'] = df['data'].apply(lambda x: x.get('mail'))
df['fileSize'] = df['data'].apply(lambda x: x.get('fileSize'))
df['teacher'] = df['data'].apply(lambda x: x.get('teacher'))
df['fileOriginalName']= df['data'].apply(lambda x: x.get('fileOriginalName'))
df['langExt']= df['data'].apply(lambda x: x.get('langExt'))
df['homoglyph']= df['data'].apply(lambda x: x.get('homoglyph'))
df['submitter']= df['data'].apply(lambda x: x.get('submitter'))
df['analysedLink']= df['data'].apply(lambda x: x.get('analysedLink'))
df['LibraryBool']= df['data'].apply(lambda x: x.get('LibraryBool'))
df['blackSource'] = df['data'].apply(lambda x: x.get('teacher', {}).get('blackSource') if x is not None and x.get('teacher') is not None else None)
df['isAnalysisRun'] = df['data'].apply(lambda x: x.get('teacher', {}).get('isAnalysisRun') if x is not None and x.get('teacher') is not None else None)
df['isAnalysisEnd'] = df['data'].apply(lambda x: x.get('teacher', {}).get('isAnalysisEnd') if x is not None and x.get('teacher') is not None else None)
df['isPlagDataBase'] = df['data'].apply(lambda x: x.get('teacher', {}).get('isPlagDataBase') if x is not None and x.get('teacher') is not None else None)
df['firstname'] = df['data'].apply(lambda x: x.get('teacher', {}).get('firstname') if x is not None and x.get('teacher') is not None else None)
df['lastname'] = df['data'].apply(lambda x: x.get('teacher', {}).get('lastname') if x is not None and x.get('teacher') is not None else None)
df['isMyData'] = df['data'].apply(lambda x: x.get('teacher', {}).get('isMyData') if x is not None and x.get('teacher') is not None else None)
df['__v'] = df['data'].apply(lambda x: x.get('teacher', {}).get('__v') if x is not None and x.get('teacher') is not None else None)
df['userID'] = df['data'].apply(lambda x: x.get('userID'))
df['userFirstName'] = df['data'].apply(lambda x: x.get('userFirstName'))
df['userLastName'] = df['data'].apply(lambda x: x.get('userLastName'))
df['userEmail'] = df['data'].apply(lambda x: x.get('userEmail'))
df['fileName'] = df['data'].apply(lambda x: x.get('archive', {}).get('fileName') if x is not None and x.get('archive') is not None else None)
df['isAnalysis'] = df['data'].apply(lambda x: x.get('archive', {}).get('isAnalysis') if x is not None and x.get('archive') is not None else None)
df['isDeleted'] = df['data'].apply(lambda x: x.get('archive', {}).get('isDeleted') if x is not None and x.get('archive') is not None else None)
df['isDone'] = df['data'].apply(lambda x: x.get('archive', {}).get('isDone') if x is not None and x.get('archive') is not None else None)
df['isFirstTime'] = df['data'].apply(lambda x: x.get('archive', {}).get('isFirstTime') if x is not None and x.get('archive') is not None else None)
df['isFolder'] = df['data'].apply(lambda x: x.get('archive', {}).get('isFolder') if x is not None and x.get('archive') is not None else None)
df['isLibrary'] = df['data'].apply(lambda x: x.get('archive', {}).get('isLibrary') if x is not None and x.get('archive') is not None else None)
df['isPermanentlyDeleted'] = df['data'].apply(lambda x: x.get('archive', {}).get('isPermanentlyDeleted') if x is not None and x.get('archive') is not None else None)
df['isPublic'] = df['data'].apply(lambda x: x.get('archive', {}).get('isPublic') if x is not None and x.get('archive') is not None else None)
df['isTranslated'] = df['data'].apply(lambda x: x.get('archive', {}).get('isTranslated') if x is not None and x.get('archive') is not None else None)
df['isPlagPrevent'] = df['data'].apply(lambda x: x.get('archive', {}).get('isPlagPrevent') if x is not None and x.get('archive') is not None else None)
df['size'] = df['data'].apply(lambda x: x.get('archive', {}).get('size') if x is not None and x.get('archive') is not None else None)
df['submitterr'] = df['data'].apply(lambda x: x.get('archive', {}).get('submitter') if x is not None and x.get('archive') is not None else None)
df_name = df['name']
lastModifiedBy=df['lastModifiedBy']
df_priority=df['priority']
df['_id'] = df['_id'].astype(str)
df_id=df['_id']
blacklisted_sources = df['blackSource'].explode().value_counts()
teacher_companies = df['data'].apply(lambda x: x.get('teacher', {}).get('company') if x is not None and x.get('teacher') is not None else None)
company_counts = teacher_companies.value_counts()
file_sizes = df['fileSize']
test=[]
print("10%")
yahoo=[]
gmail=[]
uvt=[]
names=[]
__v=[]
priority=[]
finalFileDetailSize=[]
start_scanning_adminn=[]
start_indexingg=[]
start_scanningg=[]
start_Adding_Linkk=[]
start_arabicc=[]
nameCountt=[]
firstname=[]
lastname=[]
userFirstName=[]
userLastName=[]
langueValues=[]
homoglyphValues=[]
submitterValues=[]
submitterArchivee=[]
isTranslatedd=[]
isPublicc=[]
isPermanentlyDeletedd=[]
isLibraryy=[]
isFirstTimee=[]
isDonee=[]
isDeletedd=[]
isAnalysiss=[]
fileNamee=[]
isPlagPreventt=[]
sizee=[]
name_countt=[]
priorityCountt=[]
whenAnalyseRunTrue=[]
mylist = ["yahoo", "gmail", "uvt"]
priorityValuePlot=["0","10","20"]
fileTypes= ["docx", "pdf", "doc", "txt", "pptx", "png", "ppt", "xlsx", "gif", "jpg"]
top_5_companies = company_counts.head(5)
top_5_companies_ids = top_5_companies.index.astype(str).tolist()
top_5_companies = top_5_companies.astype(int).tolist()
graphe=[]
g=0
y=0
u=0
file_formats = df['fileOriginalName'].str.split('.').str[-1]
start_times = pd.to_datetime(df['lastRunAt'])
end_times = pd.to_datetime(df['lastFinishedAt'])
file_format_counts = file_formats.value_counts()
time_duration = end_times - start_times
fileDetailSize=[]
analyseRunDetail=[]
analyseEndDetail=[]
analysePlagDatabaseDetail=[]
teacherMyDataDetail=[]
analysebooleanNames=['true','false','None']
analysebooleanNamesPlot=np.array(analysebooleanNames)
whenAnalyseRunNotnull=[]
whenAnalyseRunfalse=[]
analysedlinkkk=[]
userEmaill=[]
maill=[]
LibraryBooll=[]
def get_names(df):
    names_found=df['name'].value_counts().head()
    return names_found
def size(df):
    sizee=df["size"].mean()
    return sizee
def isPlagPrevent(df):
    isPlagPreventt=df["isPlagPrevent"].value_counts().head(5)
    return isPlagPreventt
def submitterArchive(df):
    submitterArchivee=df["submitterr"].value_counts().head(5)
    return submitterArchivee
def isTranslated(df):
    isTranslatedd=df["isTranslated"].value_counts().head(5)
    return isTranslatedd
def isPublic(df):
    isPublicc=df["isPublic"].value_counts().head(5)
    return isPublicc
def isPermanentlyDeleted(df):
    isPermanentlyDeletedd=df["isPermanentlyDeleted"].value_counts().head(5)
    return isPermanentlyDeletedd
def isLibrary(df):
    isLibraryy=df["isLibrary"].value_counts().head(5)
    return isLibraryy
def isFirstTime(df):
    isFirstTimee=df["isFirstTime"].value_counts().head(5)
    return isFirstTimee
def isDone(df):
    isDonee=df["isDone"].value_counts().head(5)
    return isDonee
def isDeleted(df):
    isDeletedd=df["isDeleted"].value_counts().head(5)
    return isDeletedd
def isAnalysis(df):
    isAnalysiss=df["isAnalysis"].value_counts().head(5)
    return isAnalysiss
def fileName(df):
    fileNamee=df["fileName"].value_counts().head(5)
    return fileNamee
def LibraryBool(df):
     LibraryBooll=df["LibraryBool"].value_counts().head()
     return LibraryBooll
def mail(df):
    maill=df["mail"].value_counts().head()
    return maill
def userEmail(df):
    userEmaill=df["userEmail"].value_counts().head()
    return userEmaill
def analysedLink(df):
    analysedLinkk = df["analysedLink"].astype(str).value_counts().head(3)
    analysedLinkkkk=analysedLinkk
    return analysedLinkkkk
def submitter(df):
    submitterFunction=df["submitter"].value_counts().head()
    return submitterFunction
def homoglyph(df):
    homoglyphFunction=df["homoglyph"].value_counts().head()
    return homoglyphFunction
def langue(df):
    langueFunction=df["langExt"].value_counts().head()
    return langueFunction    
def first_name_count(df):
    first_names = df['firstname'].value_counts().head(5)
    return first_names
def last_name_count(df):
     last_names = df['lastname'].value_counts().head(5)
     if ' ' in last_names.index:
        last_names.rename(index={' ': None}, inplace=True)
     return last_names
def user_first_name_count(df):
    first_names = df['userFirstName'].value_counts().head(5)
    return first_names
def user_last_name_count(df):
     last_names = df['userLastName'].value_counts().head(5)
     if ' ' in last_names.index:
        last_names.rename(index={' ': None}, inplace=True)
     return last_names
def unique_ids(df):
    ids=[]
    a=0
    b=0
    for e in df['userID']:
         if e not in ids:
           ids.append(e)  
           a+=1
         elif e in ids:
           b+=1
    return a
def whenAnalyseRuntrue(df):
    isplagdatabaseNone=0
    isplagdatabseTrue=0
    isplagdatabaseNotNullCountFalse=0
    isAnalyseEndNone=0
    isAnalyseEndTrue=0
    isAnalyseEndNotNullCountFalse=0
    isMyDataNone=0
    isMyDataTrue=0
    isMyDataNotNullCountFalse=0
    
    for e in df['teacher']:
        if e is not None and hasattr(e, 'get'):
            analyseRun = e.get('isAnalysisRun')
            if analyseRun == 1:
                isplagdatabase = e.get('isPlagDataBase')
                analyseEnd = e.get('isAnalysisEnd')
                ismydata = e.get('isMyData')

                if isplagdatabase == None:
                    isplagdatabaseNone+=1
                elif isplagdatabase ==0:
                     isplagdatabaseNotNullCountFalse += 1
                else:
                    isplagdatabseTrue+=1
                    
                if analyseEnd == None:
                    isAnalyseEndNone+=1
                elif analyseEnd ==0:
                     isAnalyseEndNotNullCountFalse += 1
                else:
                    isAnalyseEndTrue+=1
                    
                if ismydata == None:
                    isMyDataNone+=1
                elif ismydata ==0:
                     isMyDataNotNullCountFalse += 1
                else:
                    isMyDataTrue+=1    
                    
    df_isAnalysedRun = pd.DataFrame({
    'name': ['name','isAnalysedEnd', 'isPlagDatabase', 'isMyData'],
    'True': ['True',isAnalyseEndTrue, isplagdatabseTrue, isMyDataTrue],
    'false': ['False',isAnalyseEndNotNullCountFalse, isplagdatabaseNotNullCountFalse, isMyDataNotNullCountFalse],
    'None': ['None',isAnalyseEndNone, isplagdatabaseNone, isMyDataNone]
})
    return df_isAnalysedRun                 
def whenAnalyseRunNotNull(df):
    analyseRunNotNullCount = 0
    isplagdatabaseNotNullCount = 0
    analyseEndNotNullCount = 0
    ismydataNotNullCount = 0
    isplagdatabaseNotNullCountFalse = 0
    analyseEndNotNullCountFalse = 0
    ismydataNotNullCountFalse = 0
    count=0
    final_isAnalysedEnd=0
    final_isPlagDatabase=0
    final_isMyData=0
    for e in df['teacher']:
        count+=1
        if e is not None and hasattr(e, 'get'):
            analyseRun = e.get('isAnalysisRun')
            if analyseRun is not None:
                isplagdatabase = e.get('isPlagDataBase')
                analyseEnd = e.get('isAnalysisEnd')
                ismydata = e.get('isMyData')

                if isplagdatabase is not None:
                    isplagdatabaseNotNullCount += 1
                    if isplagdatabase ==0:
                       isplagdatabaseNotNullCountFalse += 1
                if analyseEnd is not None:
                    analyseEndNotNullCount += 1
                    if analyseEnd ==0:
                       analyseEndNotNullCountFalse += 1
                if ismydata is not None:
                    ismydataNotNullCount += 1
                    if ismydata ==0:
                        ismydataNotNullCountFalse += 1
                analyseRunNotNullCount += 1
    df_isAnalysedRun = pd.DataFrame({
    'name': ['name','isAnalysedEnd', 'isPlagDatabase', 'isMyData'],
    'True': ['True',analyseEndNotNullCount-analyseEndNotNullCountFalse, isplagdatabaseNotNullCount-isplagdatabaseNotNullCountFalse, ismydataNotNullCount-ismydataNotNullCountFalse],
    'false': ['False',analyseEndNotNullCountFalse, isplagdatabaseNotNullCountFalse, ismydataNotNullCountFalse],
    'None': ['None',final_isAnalysedEnd, final_isPlagDatabase, final_isMyData]
})
    return df_isAnalysedRun

def whenAnalyseRunFalse(df):
    isplagdatabaseNone=0
    isplagdatabseTrue=0
    isplagdatabaseNotNullCountFalse=0
    isAnalyseEndNone=0
    isAnalyseEndTrue=0
    isAnalyseEndNotNullCountFalse=0
    isMyDataNone=0
    isMyDataTrue=0
    isMyDataNotNullCountFalse=0
    
    for e in df['teacher']:
        if e is not None and hasattr(e, 'get'):
            analyseRun = e.get('isAnalysisRun')
            if analyseRun == 0:
                isplagdatabase = e.get('isPlagDataBase')
                analyseEnd = e.get('isAnalysisEnd')
                ismydata = e.get('isMyData')

                if isplagdatabase == None:
                    isplagdatabaseNone+=1
                elif isplagdatabase ==0:
                     isplagdatabaseNotNullCountFalse += 1
                else:
                    isplagdatabseTrue+=1
                    
                if analyseEnd == None:
                    isAnalyseEndNone+=1
                elif analyseEnd ==0:
                     isAnalyseEndNotNullCountFalse += 1
                else:
                    isAnalyseEndTrue+=1
                    
                if ismydata == None:
                    isMyDataNone+=1
                elif ismydata ==0:
                     isMyDataNotNullCountFalse += 1
                else:
                    isMyDataTrue+=1    
                    
    df_isAnalysedRun = pd.DataFrame({
    'name': ['name','isAnalysedEnd', 'isPlagDatabase', 'isMyData'],
    'True': ['True',isAnalyseEndTrue, isplagdatabseTrue, isMyDataTrue],
    'false': ['False',isAnalyseEndNotNullCountFalse, isplagdatabaseNotNullCountFalse, isMyDataNotNullCountFalse],
    'None': ['None',isAnalyseEndNone, isplagdatabaseNone, isMyDataNone]
})
    return df_isAnalysedRun
def analyseRun(df):
    analyseRunTrue=0
    analyseRunFalse=0
    analyseRunNull=0
    analyseRunDetail=[]
    for e in df['isAnalysisRun'] :
        if e == 1:
            analyseRunTrue+=1
        elif e== 0 :
            analyseRunFalse+=1
        else:
            analyseRunNull+=1
    analyseRunDetail=[analyseRunTrue,analyseRunFalse,analyseRunNull]
    return analyseRunDetail
def analyseEnd(df):
    analyseEndTrue=0
    analyseEndFalse=0
    analyseEndNull=0
    analyseEndDetail=[]
    for e in df['isAnalysisEnd'] :
        if e == 1:
            analyseEndTrue+=1
        elif e== 0 :
            analyseEndFalse+=1
        else:
            analyseEndNull+=1
    analyseEndDetail=[analyseEndTrue,analyseEndFalse,analyseEndNull]
    return analyseEndDetail
def analysePlagDatabase(df):
    analysePlagDatabaseTrue=0
    analysePlagDatabaseFalse=0
    analysePlagDatabaseNull=0
    analysePlagDatabaseDetail=[]
    for e in df['isPlagDataBase'] :
        if e == 1:
            analysePlagDatabaseTrue+=1
        elif e== 0 :
            analysePlagDatabaseFalse+=1
        else:
            analysePlagDatabaseNull+=1
    analysePlagDatabaseDetail=[analysePlagDatabaseTrue,analysePlagDatabaseFalse,analysePlagDatabaseNull]
    return analysePlagDatabaseDetail
def teacherMyData(df):
    isMyDataTrue=0
    isMyDataFalse=0
    isMyDataNull=0
    isMyDataDetail=[]
    for e in df['isMyData'] :
        if e == 1:
            isMyDataTrue+=1
        elif e== 0 :
            isMyDataFalse+=1
        else:
           isMyDataNull+=1
    isMyDataDetail=[isMyDataTrue,isMyDataFalse,isMyDataNull]
    return isMyDataDetail
def fileSizeCount(df):
    docxFilesSize=0
    docxFilesSizeCount=0
    pdfFilesSize=0
    pdfFilesSizeCount=0
    docFilesSize=0
    docFilesSizeCount=0
    txtFilesSize=0
    txtFilesSizeCount=0
    pptxFilesSize=0
    pptxFilesSizeCount=0
    pngFilesSize=0
    pngFilesSizeCount=0
    pptFilesSize=0
    pptFilesSizeCount=0
    xlsxFilesSize=0
    xlsxFilesSizeCount=0
    gifFilesSize=0
    gifFilesSizeCount=0
    jpgFilesSize=0
    jpgFilesSizeCount=0
    fileDetailSize=[]
    fileDetailSizeCount=[]
    fileAllDetails=[]
    for e in df['data']:
       file_original_name = e.get('fileOriginalName')
       if file_original_name is not None:
            file_format = file_original_name.split('.')[-1]
            if file_format == 'docx':
              docxFilesSize=docxFilesSize+e.get('fileSize')
              docxFilesSizeCount+=1
            elif file_format == 'pdf':
                pdfFilesSize=pdfFilesSize+e.get('fileSize')
                pdfFilesSizeCount+=1
            elif file_format == 'doc':
                docFilesSize=docFilesSize+e.get('fileSize')
                docFilesSizeCount+=1
            elif file_format == 'txt':
                txtFilesSize=txtFilesSize+e.get('fileSize')
                txtFilesSizeCount+=1
            elif file_format == 'pptx':
                pptxFilesSize=pptxFilesSize+e.get('fileSize')
                pptxFilesSizeCount+=1
            elif file_format == 'png':
                pngFilesSize=pngFilesSize+e.get('fileSize')
                pngFilesSizeCount+=1
            elif file_format == 'ppt':
               pptFilesSize=pptFilesSize+e.get('fileSize')
               pptFilesSizeCount+=1
            elif file_format == 'xlsx':
               xlsxFilesSize=xlsxFilesSize+e.get('fileSize')
               xlsxFilesSizeCount+=1
            elif file_format == 'gif':
                 gifFilesSize= gifFilesSize+e.get('fileSize')
                 gifFilesSizeCount+=1
            elif file_format == 'jpg':
                jpgFilesSize=jpgFilesSize+e.get('fileSize')
                jpgFilesSizeCount+=1
    fileDetailSize=[docxFilesSize,pdfFilesSize,docFilesSize,txtFilesSize,pptxFilesSize,pngFilesSize,pptFilesSize,xlsxFilesSize,gifFilesSize,jpgFilesSize]
    fileDetailSizeCount=[docxFilesSizeCount,pdfFilesSizeCount,docFilesSizeCount,txtFilesSizeCount,pptxFilesSizeCount,pngFilesSizeCount,pptFilesSizeCount,xlsxFilesSizeCount,gifFilesSizeCount,jpgFilesSizeCount]
    fileAllDetails=fileDetailSize+fileDetailSizeCount
    return  fileAllDetails
def get_mails(df):
    yahoo=[]
    gmail=[]
    uvt=[]
    graphe=[]
    g=0
    y=0
    u=0
    for e in df['mail']:
         if e is not None:
             if '@gmail' in e:
              gmail.append('a')  
              g=g+1
             elif '@yahoo' in e:
              yahoo.append('b')
              y=y+1
             elif '@uvt' in e:
              uvt.append('c')
              u=u+1
    graphe=gmail+yahoo+uvt
    
    return graphe

def start_scanning(df):
    start_scanningCount20=0
    start_scanningCount10=0
    start_scanningCount0=0
    start_scanningData=[]
    for _, row in df.iterrows():
        nom = row['name']
        if nom == 'start scanning':
            priorityy = row['priority']
            if priorityy == 20:
                    start_scanningCount20+=1
            elif priorityy == 10: 
                    start_scanningCount10+=1
            elif priorityy == 0:     
                    start_scanningCount0+=1
    start_scanningData=[start_scanningCount0,start_scanningCount10,start_scanningCount20]      
    return start_scanningData         
  
def start_indexing(df):
    start_indexingCount20=0
    start_indexingCount10=0
    start_indexingCount0=0
    start_indexingData=[]
    for _, row in df.iterrows():
        nom = row['name']
        if nom == 'start indexing':
            priorityy = row['priority']
            if priorityy == 20:
                    start_indexingCount20+=1
            if priorityy == 10: 
                    start_indexingCount10+=1
            if priorityy == 0:     
                    start_indexingCount0+=1
    start_indexingData=[start_indexingCount0,start_indexingCount10,start_indexingCount20]      
    return start_indexingData         
def start_Adding_Link(df):
    start_Adding_LinkCount20=0
    start_Adding_LinkCount10=0
    start_Adding_LinkCount0=0
    start_Adding_LinkData=[]
    for _, row in df.iterrows():
        nom = row['name']
        if nom == 'start adding link':
            priorityy = row['priority']
            if priorityy == 20:
                    start_Adding_LinkCount20+=1
            elif priorityy == 10: 
                    start_Adding_LinkCount10+=1
            elif priorityy == 0:     
                   start_Adding_LinkCount0+=1
    start_Adding_LinkData=[start_Adding_LinkCount0,start_Adding_LinkCount10,start_Adding_LinkCount20]      
    return start_Adding_LinkData         
def start_arabic(df):
    start_arabicCount20=0
    start_arabicCount10=0
    start_arabicCount0=0
    start_arabicData=[]
    for _, row in df.iterrows():
        nom = row['name']
        if nom == 'start arabic':
            priorityy = row['priority']
            if priorityy == 20:
                    start_arabicCount20+=1
            elif priorityy == 10: 
                    start_arabicCount10+=1
            elif priorityy == 0:     
                    start_arabicCount0+=1
    start_arabicData=[start_arabicCount0,start_arabicCount10,start_arabicCount20]      
    return start_arabicData         
  
def start_scanning_admin(df):
    start_scanning_adminCount20=0
    start_scanning_adminCount10=0
    start_scanning_adminCount0=0
    start_scanning_adminData=[]
    for _, row in df.iterrows():
        nom = row['name']
        if nom == 'start scanning admin':
            priorityy = row['priority']
            if priorityy == 20:
                    start_scanning_adminCount20+=1
            elif priorityy == 10: 
                    start_scanning_adminCount10+=1
            elif priorityy == 0:     
                    start_scanning_adminCount0+=1
    start_scanning_adminData=[start_scanning_adminCount0,start_scanning_adminCount10,start_scanning_adminCount20]      
    return start_scanning_adminData         
             


def get_unique_priority(df):
   
    priorityy=[]
    for e in df_priority:
         if e is not None:
             if e not in priorityy:
              priorityy.append(e)  
              
    return priorityy
def get_unique_name(df):
   
    namee=[]
    for e in df_name:
         if e is not None:
             if e not in namee:
              namee.append(e)  
              
    return namee
def nameCount(df):
    start_scanningCount=0
    start_scanning_adminCount=0
    start_indexingCount=0
    start_arabicCount=0
    start_adding_linkCount=0
    nameCount=[]
    for e in df_name:
        if e =='start scanning':
            start_scanningCount+=1
        if e =='start scanning admin':
             start_scanning_adminCount+=1
        if e =='start indexing':
            start_indexingCount+=1
        if e =='start arabic':
            start_arabicCount+=1
        if e =='start adding link':  
            start_adding_linkCount+=1
    nameCount=[start_scanningCount,start_indexingCount,start_arabicCount,start_adding_linkCount,start_scanning_adminCount]   
    return nameCount     
def priorityCount(df):
    prio20Count=0
    prio10Count=0
    prio0Count=0
    prioCountData=[]
    for e in df_priority:
        if e == 20:
            prio20Count+=1
        if e == 10:
            prio10Count+=1
        if e == 0:  
            prio0Count+=1
    prioCountData=[prio0Count,prio10Count,prio20Count]    
    return prioCountData
def get_unique_gmail(df):
   
    gmail=[]
    g=0
    for e in df['mail']:
         if e is not None:
             if '@gmail' in e:
              gmail.append('a')  
              g=g+1
    return g
def get_unique_yahoo(df):
    yahoo=[]
    y=0
    for e in df['mail']:
         if e is not None:
             if '@yahoo' in e:
              yahoo.append('b')
              y=y+1
    return y
def get_unique_uvt(df):
    uvt=[]
    u=0
    for e in df['mail']:
         if e is not None:
             if '@uvt' in e:
              uvt.append('c')
              u=u+1
    
    return u
print("20%")
isPlagPreventt=isPlagPrevent(df)
sizee=size(df)
submitterArchivee=submitterArchive(df)
isTranslatedd=isTranslated(df)
isPublicc=isPublic(df)
isPermanentlyDeletedd=isPermanentlyDeleted(df)
isLibraryy=isLibrary(df)
isFirstTimee=isFirstTime(df)
isDonee=isDone(df)
isDeletedd=isDeleted(df)
isAnalysiss=isAnalysis(df)
fileNamee=fileName(df)
LibraryBooll=LibraryBool(df)
maill=mail(df)
userEmaill=userEmail(df)
analysedlinkkk=analysedLink(df)
submitterValues=submitter(df)
homoglyphValues=homoglyph(df)
langueValues=langue(df)
__v=df['__v'].value_counts()
userFirstName=user_first_name_count(df)
userLastName=user_last_name_count(df)
firstname=first_name_count(df)
lastname=last_name_count(df)
p=0
print("30%")
p=unique_ids(df)
priorityCountt=priorityCount(df)
name_countt=get_names(df)
name_count=np.array(name_countt.index)
nameCountt=nameCount(df)
start_indexingg=start_indexing(df)
start_scanningg=start_scanning(df) 
start_Adding_Linkk=start_Adding_Link(df)
start_arabicc=start_arabic(df)
start_scanning_adminn=start_scanning_admin(df)
priority=get_unique_priority(df)
names=get_unique_name(df)
whenAnalyseRunfalse=whenAnalyseRunFalse(df)
whenAnalyseRunNotnull=whenAnalyseRunNotNull(df)
whenAnalyseRunTrue=whenAnalyseRuntrue(df)
teacherMyDataDeatil=teacherMyData(df)
analysePlagDatabaseDetail=analysePlagDatabase(df)
analyseEndDetail=analyseEnd(df)
analyseRunDetail=analyseRun(df)
fileDetailSize=fileSizeCount(df)
uvt=get_unique_uvt(df)
gmail=get_unique_gmail(df)
yahoo=get_unique_yahoo(df)
getMail = get_mails(df)
print("40%")
dff = pd.DataFrame({'getMail': getMail})
plt.subplot(1, 2, 1) # row 1, col 2 index 1
a=dff['getMail'].value_counts()
plt.pie(a, labels= mylist)
plt.title("mail type!")
plt.subplot(1, 2, 2) # index 2
mylist2= np.array([yahoo,gmail,uvt])
plt.bar(mylist,mylist2)
plt.title("mail!")
plt.subplots_adjust(wspace=0.8)
plt.savefig('./example_chart.png', 
           transparent=False,  
           facecolor='white', 
           bbox_inches="tight")

# Plot the file size distribution
plt.figure(figsize=(8, 6))
file_format_counts.plot(kind='bar', edgecolor='black')
plt.xlabel('File Format')
plt.ylabel('Count')
plt.title('File Format Counts')
plt.xticks(rotation=45)
plt.savefig('./example2_chart.png', 
           transparent=False,  
           facecolor='white', 
           bbox_inches="tight")
plt.show()
plt.figure(figsize=(8, 6))
plt.hist(time_duration.dt.total_seconds() / 60, bins=30, color='blue')
plt.xlabel('Time Duration (minutes)')
plt.ylabel('Frequency')
plt.title('Time Duration Analysis')
plt.grid(True)
plt.savefig('./time_duration_histogram.png', dpi=300, bbox_inches='tight')
plt.show()
plt.figure(figsize=(14, 6))
blacklisted_sources.plot(kind='bar', color='skyblue')
plt.xlabel('Blacklisted Source')
plt.ylabel('Count')
plt.title('Blacklisted Source Analysis')
plt.xticks(rotation=45, ha='right')
plt.grid(True)
plt.savefig('./blacklisted_sources.png', dpi=300, bbox_inches='tight')
plt.show()
plt.figure(figsize=(15, 6))
plt.bar(top_5_companies_ids, top_5_companies)
plt.xlabel('Company ID')
plt.ylabel('Frequency')
plt.title('Top 5 Companies')
plt.savefig('./company_counts.png', dpi=300, bbox_inches='tight')
plt.show()
plt.figure(figsize=(15, 6))
finalFileDetailSize=[fileDetailSize[0]/fileDetailSize[10],fileDetailSize[1]/fileDetailSize[11],fileDetailSize[2]/fileDetailSize[12],fileDetailSize[3]/fileDetailSize[13],fileDetailSize[4]/fileDetailSize[14],fileDetailSize[5]/fileDetailSize[15],fileDetailSize[6]/fileDetailSize[16],fileDetailSize[7]/fileDetailSize[17],fileDetailSize[8]/fileDetailSize[18],fileDetailSize[9]/fileDetailSize[19]]
fileTypesA=np.array(fileTypes)
fileDetailSizeA=np.array(finalFileDetailSize)
plt.bar(fileTypesA,fileDetailSizeA )
plt.xlabel('fileTypesA ID')
plt.ylabel('fileDetailSizeA')
plt.title('Top 5 fileDetailSizeA')
plt.savefig('./averagefilesize.png', dpi=300, bbox_inches='tight')
plt.show()
print("50%")
analyseRunDetailPlot=np.array(analyseRunDetail)
plt.figure(figsize=(15, 6))
plt.bar(analysebooleanNamesPlot,analyseRunDetailPlot )
plt.xlabel(' analysisRun results')
plt.ylabel('analysisRun results count')
plt.title('analysisRun')
plt.savefig('./analyseRunDetailPlot.png', dpi=300, bbox_inches='tight')
plt.show()
analyseEndDetailPlot=np.array(analyseEndDetail)
plt.figure(figsize=(15, 6))
plt.bar(analysebooleanNamesPlot,analyseEndDetailPlot, color='black' )
plt.xlabel(' analysisEnd results')
plt.ylabel('analysisEnd results count')
plt.title('analysisEnd')
plt.savefig('./analyseEndDetailPlot.png', dpi=300, bbox_inches='tight')
plt.show()
analysePlagDatabaseDetailPlot=np.array(analysePlagDatabaseDetail)
plt.figure(figsize=(15, 6))
plt.bar(analysebooleanNamesPlot,analysePlagDatabaseDetailPlot, color='red' )
plt.xlabel(' analysePlagDatabaseDetail results')
plt.ylabel('analysePlagDatabaseDetail results count')
plt.title('analysePlagDatabaseDetail')
plt.savefig('./analysePlagDatabaseDetailPlot.png', dpi=300, bbox_inches='tight')
plt.show()
teacherMyDataDeatilPlot=np.array(teacherMyDataDeatil)
plt.figure(figsize=(15, 6))
plt.bar(analysebooleanNamesPlot,teacherMyDataDeatilPlot, color='green' )
plt.xlabel(' isMyDataDetail results')
plt.ylabel('isMyDataDetail results count')
plt.title('isMyDataDetail')
plt.savefig('./teacherMyDataDetailPlot.png', dpi=300, bbox_inches='tight')
plt.show()
priorityCounttPlot=np.array(priorityCountt)
plt.figure(figsize=(15, 6))
plt.bar(priorityValuePlot,priorityCounttPlot, color='black' )
plt.xlabel(' priority  results')
plt.ylabel('priority results count')
plt.title('priority count')
plt.savefig('./priorityCounttPlot.png', dpi=300, bbox_inches='tight')
plt.show()
nameCounttPlot=np.array(nameCountt)
plt.figure(figsize=(15, 6))
plt.bar(name_count,nameCounttPlot, color='blue' )
plt.xlabel(' name results')
plt.ylabel('name results count')
plt.title('names count')
plt.savefig('./nameCounttPlot.png', dpi=300, bbox_inches='tight')
plt.show()
start_indexinggPlot=np.array(start_indexingg)
plt.figure(figsize=(15, 6))
plt.bar(priorityValuePlot,start_indexinggPlot, color='pink' )
plt.xlabel(' start indexing results')
plt.ylabel('start indexing results count')
plt.title('start indexing name')
plt.savefig('./startIndexingPlot.png', dpi=300, bbox_inches='tight')
plt.show()
start_scanninggPlot=np.array(start_scanningg)
plt.figure(figsize=(15, 6))
plt.bar(priorityValuePlot,start_scanninggPlot, color='violet' )
plt.xlabel(' start scanning results')
plt.ylabel('start scanning  results count')
plt.title('startScanning')
plt.savefig('./StartScanning.png', dpi=300, bbox_inches='tight')
plt.show()
start_Adding_LinkkPlot=np.array(start_Adding_Linkk)
plt.figure(figsize=(15, 6))
plt.bar(priorityValuePlot,start_Adding_LinkkPlot, color='green' )
plt.xlabel(' start adding link results')
plt.ylabel('start adding linkresults count')
plt.title('start adding link')
plt.savefig('./start_adding_linkPlot.png', dpi=300, bbox_inches='tight')
plt.show()
start_arabiccPlot=np.array(start_arabicc)
plt.figure(figsize=(15, 6))
plt.bar(priorityValuePlot,start_arabiccPlot, color='black' )
plt.xlabel(' start_arabic results')
plt.ylabel('start_arabic results count')
plt.title('start arabic')
plt.savefig('./startArabicPlot.png', dpi=300, bbox_inches='tight')
plt.show()
start_scanning_adminnPlot=np.array(start_scanning_adminn)
plt.figure(figsize=(15, 6))
plt.bar(priorityValuePlot,start_scanning_adminnPlot, color='pink' )
plt.xlabel(' start scanning admin results')
plt.ylabel('start scanning admin results count')
plt.title('start scanning admin ')
plt.savefig('./start_scanning_admin_Plot.png', dpi=300, bbox_inches='tight')
plt.show()
plt.figure(figsize=(14, 6))
firstname.plot(kind='bar', color='black')
plt.xlabel('first name')
plt.ylabel('Count')
plt.title('first name')
plt.xticks(rotation=1, ha='right')
plt.savefig('./firstname.png', dpi=300, bbox_inches='tight')
plt.show()
plt.figure(figsize=(14, 6))
lastname.plot(kind='bar', color='blue')
plt.xlabel('last name')
plt.ylabel('Count')
plt.title('last name')
plt.xticks(rotation=1, ha='right')
plt.savefig('./lastname.png', dpi=300, bbox_inches='tight')
plt.show()
plt.figure(figsize=(14, 6))
userFirstName.plot(kind='bar', color='black')
plt.xlabel('user first name')
plt.ylabel('Count')
plt.title('user first name count')
plt.xticks(rotation=1, ha='right')
plt.savefig('./userfirstname.png', dpi=300, bbox_inches='tight')
plt.show()
plt.figure(figsize=(14, 6))
userLastName.plot(kind='bar', color='red')
plt.xlabel('user last name')
plt.ylabel('Count')
plt.title('user last name count')
plt.xticks(rotation=1, ha='right')
plt.savefig('./userlastname.png', dpi=300, bbox_inches='tight')
plt.show()
plt.figure(figsize=(14, 6))
__v.plot(kind='bar', color='pink')
plt.xlabel('values')
plt.ylabel('Count')
plt.title('__v count')
plt.xticks(rotation=1, ha='right')
plt.savefig('./__v.png', dpi=300, bbox_inches='tight')
plt.show()
print("60%")
plt.figure(figsize=(14, 6))
langueValues.plot(kind='bar', color='cyan')
plt.xlabel('langueValues')
plt.ylabel('Count')
plt.title('langue values count')
plt.xticks(rotation=1, ha='right')
plt.savefig('./langueValues.png', dpi=300, bbox_inches='tight')
plt.show()
plt.figure(figsize=(14, 6))
homoglyphValues.plot(kind='bar', color='green')
plt.xlabel('homoglyphValues')
plt.ylabel('Count')
plt.title('homoglyphValues  count')
plt.xticks(rotation=1, ha='right')
plt.savefig('./homoglyphValues.png', dpi=300, bbox_inches='tight')
plt.show()

plt.figure(figsize=(14, 6))
submitterValues.plot(kind='bar', color='black')
plt.xlabel('submitterValues')
plt.ylabel('Count')
plt.title('submitterValues  count')
plt.xticks(rotation=45, ha='right')
plt.savefig('./submitterValues.png', dpi=300, bbox_inches='tight')
plt.show()
plt.figure(figsize=(14, 10))
userEmaill.plot(kind='bar', color='red')
plt.xlabel('userEmail values')
plt.ylabel('Count')
plt.title('userEmail  count')
plt.xticks(rotation=45, ha='right')
plt.savefig('./userEmail.png', dpi=300, bbox_inches='tight')
plt.show()

plt.figure(figsize=(14, 6))
LibraryBooll.plot(kind='bar', color='green')
plt.xlabel('LibraryBool values')
plt.ylabel('Count')
plt.title('LibraryBool  count')
plt.xticks(rotation=0, ha='right')
plt.savefig('./LibraryBool.png', dpi=300, bbox_inches='tight')
plt.show()
plt.figure(figsize=(14, 6))
fileNamee.plot(kind='bar', color='blue')
plt.xlabel('fileName values')
plt.ylabel('Count')
plt.title('fileName  count')
plt.xticks(rotation=45, ha='right')
plt.savefig('./fileName.png', dpi=300, bbox_inches='tight')
plt.show()
plt.figure(figsize=(14, 6))
isAnalysiss.plot(kind='bar', color='red')
plt.xlabel('isAnalysis values')
plt.ylabel('Count')
plt.title('isAnalysis  count')
plt.xticks(rotation=0, ha='right')
plt.savefig('./isAnalysis.png', dpi=300, bbox_inches='tight')
plt.show()
plt.figure(figsize=(14, 6))
isDeletedd.plot(kind='bar', color='black')
plt.xlabel('isDeleted values')
plt.ylabel('Count')
plt.title('isDeleted  count')
plt.xticks(rotation=0, ha='right')
plt.savefig('./isDeleted.png', dpi=300, bbox_inches='tight')
plt.show()
plt.figure(figsize=(14, 6))
isDonee.plot(kind='bar', color='pink')
plt.xlabel('isDone values')
plt.ylabel('Count')
plt.title('isDone  count')
plt.xticks(rotation=0, ha='right')
plt.savefig('./isDone.png', dpi=300, bbox_inches='tight')
plt.show()
plt.figure(figsize=(14, 6))
isFirstTimee.plot(kind='bar', color='green')
plt.xlabel('isFirstTime values')
plt.ylabel('Count')
plt.title('isFirstTime  count')
plt.xticks(rotation=0, ha='right')
plt.savefig('./isFirstTime.png', dpi=300, bbox_inches='tight')
plt.show()
plt.figure(figsize=(14, 6))
isLibraryy.plot(kind='bar', color='blue')
plt.xlabel('isLibrary values')
plt.ylabel('Count')
plt.title('isLibrary  count')
plt.xticks(rotation=1, ha='right')
plt.savefig('./isLibrary.png', dpi=300, bbox_inches='tight')
plt.show()
plt.figure(figsize=(14, 6))
isPermanentlyDeletedd.plot(kind='bar', color='red')
plt.xlabel('isPermanentlyDeleted values')
plt.ylabel('Count')
plt.title('isPermanentlyDeleted  count')
plt.xticks(rotation=0, ha='right')
plt.savefig('./isPermanentlyDeleted.png', dpi=300, bbox_inches='tight')
plt.show()
plt.figure(figsize=(14, 6))
isPublicc.plot(kind='bar', color='black')
plt.xlabel('isPublic values')
plt.ylabel('Count')
plt.title('isPublic  count')
plt.xticks(rotation=0, ha='right')
plt.savefig('./isPublic.png', dpi=300, bbox_inches='tight')
plt.show()
plt.figure(figsize=(14, 6))
isTranslatedd.plot(kind='bar', color='pink')
plt.xlabel('isTranslated values')
plt.ylabel('Count')
plt.title('isTranslated  count')
plt.xticks(rotation=0, ha='right')
plt.savefig('./isTranslated.png', dpi=300, bbox_inches='tight')
plt.show()
plt.figure(figsize=(14, 6))
submitterArchivee.plot(kind='bar', color='green')
plt.xlabel('submitterArchive values')
plt.ylabel('Count')
plt.title('submitterArchive  count')
plt.xticks(rotation=0, ha='right')
plt.savefig('./submitterArchive.png', dpi=300, bbox_inches='tight')
plt.show()
plt.figure(figsize=(14, 6))
isPlagPreventt.plot(kind='bar', color='blue')
plt.xlabel('isPlagPrevent values')
plt.ylabel('Count')
plt.title('isPlagPrevent  count')
plt.xticks(rotation=0, ha='right')
plt.savefig('./isPlagPrevent.png', dpi=300, bbox_inches='tight')
plt.show()
plt.figure(figsize=(8, 6))
plt.hist(df["size"], bins=30, color='blue')
plt.axvline(sizee, color='red', linestyle='dashed', linewidth=1)
plt.xlabel('File Size')
plt.ylabel('Frequency')
plt.title('File Size Analysis')
plt.grid(True)
plt.legend(['Average Size'])
plt.savefig('./size.png', dpi=300, bbox_inches='tight')
plt.show()
i=0
print("70%")
class PDF(FPDF):
    def __init__(self):
        super().__init__()
    def header(self):
        if self.page_no()==1 :
                self.set_font('Arial', 'B', 25)
                pdf.set_text_color(r= 255, g= 0, b = 0)
                self.cell(0, 12, 'Statistics report', 0, 1, 'C') 
        elif   self.page_no()==2 :
                self.set_font('Arial', 'B', 25)
                pdf.set_text_color(r= 255, g= 0, b = 0)
                self.cell(0, 12, 'Statistics report', 0, 1, 'C') 
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', '', 12)
        self.cell(0, 6, f'Page {self.page_no()}', 0, 0, 'C')
    def add_page(self):
        super().add_page()
        self.rect(10, 10, self.w - 20, self.h - 20)
pdf = PDF()
pdf.add_page()  
pdf.image('./ssc.png',   x = 50, y = 100, w = 120, h =100, type = 'PNG')
pdf.add_page()
pdf.ln(15)
pdf.set_font('Arial', 'B', 18)
pdf.set_text_color(r= 0, g= 0, b = 255)
pdf.cell(w=30, h=10, txt="Date: ", ln=0)
pdf.set_font('Arial', '', 13)
pdf.set_text_color(r=0, g= 0, b = 0)
pdf.cell(w=30, h=10, txt="  06/20/2023", ln=1)
pdf.set_font('Arial', 'B', 18)
pdf.set_text_color(r= 0, g= 0, b = 255)
pdf.cell(w=30, h=10, txt="Author: ", ln=0)
pdf.set_font('Arial', '', 13)
pdf.set_text_color(r=0, g= 0, b = 0)
pdf.cell(w=30, h=10, txt="admin", ln=1)
pdf.ln(15)
pdf.multi_cell(w=0, h=10, txt='In this report, we present the analysis of the dataset collected from our research team. The dataset comprises agenda jobs. Our objective is to explore the dataset and uncover key insights and patterns through statistical analysis and visualization techniques')
pdf.image('./example_chart.png', 
          x = 40, y = None, w = 100, h = 0, type = 'PNG')
pdf.ln(15)
pdf.multi_cell(w=0, h=10, txt='using those 2 figures, we can see the most used types of emails between those 3:gmail,yahoo,uvt . we choosed them because they are the most known 3 types of emails nowadays')
pdf.add_page()
pdf.ln(15)
pdf.image('./userEmail.png', 
          x = 18, y = 15, w = 170, h = 160, type = 'PNG')
pdf.ln(90)
pdf.multi_cell(w=0, h=10, txt='here, we can see the most used emails in the dataset.This information can be valuable for understanding the email landscape and identifying potential communication channels' )
pdf.image('./time_duration_histogram.png', 
          x = 50, y = 150, w = 100, h = 0, type = 'PNG')
pdf.ln(90)
#Bar plot displaying the counts of each file format.we notice that the most common format is pdf then docx,those two were used in 99% of the files in the dataset
pdf.multi_cell(w=0, h=10, txt='time_duration help us identify if there is problems while compiling,the operations should ')
pdf.add_page()
pdf.ln(15)
pdf.image('./example2_chart.png', 
          x = 18, y = 15, w = 160, h = 120, type = 'PNG')
print("75%")
pdf.ln(90)
pdf.multi_cell(w=0, h=10, txt='This distribution provides insights about the most used type of files in the database')
pdf.image('./averagefilesize.png', 
          x = 18, y = 150, w = 170, h = 70, type = 'PNG')
pdf.ln(100)
pdf.multi_cell(w=0, h=10, txt='in this plot, we used the most known file types and we calculated the total size of each of them in the dataset ')

pdf.add_page()
pdf.ln(15)
pdf.image('./analyseEndDetailPlot.png', 
         x = 18, y = 15, w = 170, h = 70, type = 'PNG')
pdf.ln(90)
pdf.multi_cell(w=0, h=10, txt='this is statistique for analyse end detail')
pdf.image('./teacherMyDataDetailPlot.png', 
          x = 18, y = 150, w = 170, h = 70, type = 'PNG')
pdf.ln(100)
pdf.multi_cell(w=0, h=10, txt='this is teacher my data statistique')
pdf.add_page()
pdf.ln(15)
pdf.image('./analysePlagDatabaseDetailPlot.png', 
         x = 18, y = 15, w = 170, h = 70, type = 'PNG')
pdf.ln(90)
pdf.multi_cell(w=0, h=10, txt='this is analyse plagdatabse details')
pdf.image('./priorityCounttPlot.png', 
          x = 18, y = 150, w = 170, h = 70, type = 'PNG')
pdf.ln(100)
pdf.multi_cell(w=0, h=10, txt='this is the stats for priority in the dataset')
pdf.add_page()
pdf.ln(15)
print("80%")
for i in range(len(whenAnalyseRunTrue)):
        feature1 = str(whenAnalyseRunTrue['name'].iloc[i])
        feature2 = str(whenAnalyseRunTrue['True'].iloc[i])
        feature3 = str(whenAnalyseRunTrue['false'].iloc[i])
        feature4 = str(whenAnalyseRunTrue['None'].iloc[i])
        pdf.cell(49, 10, feature1, border=1, ln=0, align='C')
        pdf.cell(47, 10, feature2, border=1, ln=0, align='C')
        pdf.cell(47, 10, feature3, border=1, ln=0, align='C')
        pdf.cell(47, 10, feature4, border=1, ln=1, align='C')
pdf.ln(15)    
pdf.multi_cell(w=0, h=10, txt='when analyseRun is false,this the values of the other data')
pdf.ln(80)
for i in range(len(whenAnalyseRunfalse)):
        feature1 = str(whenAnalyseRunfalse['name'].iloc[i])
        feature2 = str(whenAnalyseRunfalse['True'].iloc[i])
        feature3 = str(whenAnalyseRunfalse['false'].iloc[i])
        feature4 = str(whenAnalyseRunfalse['None'].iloc[i])
        pdf.cell(49, 10, feature1, border=1, ln=0, align='C')
        pdf.cell(47, 10, feature2, border=1, ln=0, align='C')
        pdf.cell(47, 10, feature3, border=1, ln=0, align='C')
        pdf.cell(47, 10, feature4, border=1, ln=1, align='C')
pdf.ln(15)
pdf.multi_cell(w=0, h=10, txt='when analyseRun is false,this the values of the other data')
pdf.ln(15)   

pdf.add_page()
pdf.ln(15)
pdf.image('./nameCounttPlot.png',
         x = 18, y = 15, w = 170, h = 70, type = 'PNG')
pdf.ln(90)
pdf.multi_cell(w=0, h=10, txt='here we have the count of the names of the operations')
pdf.image('./startIndexingPlot.png', 
          x = 18, y = 150, w = 170, h = 70, type = 'PNG')
pdf.ln(100)
pdf.multi_cell(w=0, h=10, txt='thoses plots shows the relation between the priority and the names')
pdf.add_page()
pdf.ln(15)
pdf.image('./StartScanning.png', 
         x = 18, y = 15, w = 170, h = 70, type = 'PNG')
pdf.ln(90)
pdf.multi_cell(w=0, h=10, txt='the priority counts on the name start scanning')
pdf.image('./start_adding_linkPlot.png', 
          x = 18, y = 150, w = 170, h = 70, type = 'PNG')
pdf.ln(100)
pdf.multi_cell(w=0, h=10, txt='the priority counts on the name start adding link')
pdf.add_page()
pdf.ln(15)
pdf.image('./startArabicPlot.png', 
          x = 18, y = 15, w = 170, h = 70, type = 'PNG')
pdf.ln(90)
pdf.multi_cell(w=0, h=10, txt='the priority counts on the name start arabic plot')
pdf.image('./start_scanning_admin_Plot.png', 
          x = 18, y = 150, w = 170, h = 70, type = 'PNG')
pdf.ln(100)
pdf.multi_cell(w=0, h=10, txt='the priority counts on the name start scanning admin')
print("85%")
pdf.add_page()
pdf.ln(15)
pdf.image('./firstname.png', 
          x = 18, y = 15, w = 170, h = 70, type = 'PNG')
pdf.ln(90)
pdf.multi_cell(w=0, h=10, txt='the most common first names')
pdf.image('./lastname.png', 
         x = 18, y = 150, w = 170, h = 70, type = 'PNG')
pdf.ln(100)
pdf.multi_cell(w=0, h=10, txt=' the most common last names')
pdf.add_page()
pdf.ln(15)
pdf.image('./userfirstname.png', 
          x = 18, y = 15, w = 170, h = 70, type = 'PNG')
pdf.ln(90)
pdf.multi_cell(w=0, h=10, txt='the most common users first name')
pdf.image('./userlastname.png', 
         x = 18, y = 150, w = 170, h = 70, type = 'PNG')
pdf.ln(100)
pdf.multi_cell(w=0, h=10, txt='the most common users last name')
pdf.add_page()
pdf.ln(15)
pdf.image('./__v.png', 
         x = 18, y = 15, w = 170, h = 70, type = 'PNG')
pdf.ln(90)
pdf.multi_cell(w=0, h=10, txt='__v counts ')
pdf.image('./langueValues.png',
          x = 18, y = 150, w = 170, h = 70, type = 'PNG')
pdf.ln(100)
pdf.multi_cell(w=0, h=10, txt='the most used languages ')
pdf.add_page()
pdf.ln(15)
pdf.image('./homoglyphValues.png',
          x = 18, y = 15, w = 170, h = 70, type = 'PNG')
pdf.ln(90)
print("90%")
pdf.multi_cell(w=0, h=10, txt='the values of homoglyph')
pdf.image('./submitterValues.png',
          x = 18, y = 150, w = 170, h = 70, type = 'PNG')
pdf.ln(100)
pdf.multi_cell(w=0, h=10, txt='top submitters in the database')

pdf.add_page()
pdf.cell(0, 10, "the most used Analysed Links:", ln=True)
pdf.ln(2)
for link, count in analysedlinkkk.items():
    line =f" {link}: {count}"
    pdf.multi_cell(0, 10, line, align="L")
    pdf.ln(5)     
pdf.add_page()
pdf.ln(15)
pdf.image('./LibraryBool.png',
          x = 18, y = 15, w = 170, h = 70, type = 'PNG')
pdf.ln(90)
pdf.multi_cell(w=0, h=10, txt='libraryBool values')
pdf.image('./company_counts.png', 
          x = 18, y = 150, w = 170, h = 70, type = 'PNG')
pdf.ln(100)
pdf.multi_cell(w=0, h=10, txt='the most used user email')
pdf.add_page()
pdf.ln(15)
pdf.image('./fileName.png',
          x = 13, y = 15, w = 170, h = 100, type = 'PNG')
pdf.ln(90)
pdf.multi_cell(w=0, h=10, txt='filename values in archive')
pdf.image('./isAnalysis.png', 
          x = 18, y = 150, w = 170, h = 70, type = 'PNG')
pdf.ln(100)
pdf.multi_cell(w=0, h=10, txt='isAnalysis values in archive')
pdf.add_page()
pdf.ln(15)
pdf.image('./isDeleted.png',
          x = 18, y = 15, w = 170, h = 70, type = 'PNG')
pdf.ln(90)
pdf.multi_cell(w=0, h=10, txt='isDeleted values in archive')
pdf.image('./isDone.png', 
          x = 18, y = 150, w = 170, h = 70, type = 'PNG')
pdf.ln(100)
pdf.multi_cell(w=0, h=10, txt='isDone values in archive')
pdf.add_page()
pdf.ln(15)
pdf.image('./isFirstTime.png',
          x = 18, y = 15, w = 170, h = 70, type = 'PNG')
pdf.ln(90)
pdf.multi_cell(w=0, h=10, txt='isFirstTime values in archive')
pdf.image('./isLibrary.png', 
          x = 18, y = 150, w = 170, h = 70, type = 'PNG')
pdf.ln(100)
print("95%")
pdf.multi_cell(w=0, h=10, txt='isLibrary values in archive')
pdf.add_page()
pdf.ln(15)
pdf.image('./isPermanentlyDeleted.png',
          x = 18, y = 15, w = 170, h = 70, type = 'PNG')
pdf.ln(90)
pdf.multi_cell(w=0, h=10, txt='isPermanentlyDeleted values in archive')
pdf.image('./isPublic.png', 
          x = 18, y = 150, w = 170, h = 70, type = 'PNG')
pdf.ln(100)
pdf.multi_cell(w=0, h=10, txt='isPublic values in archive')
pdf.add_page()
pdf.ln(15)
pdf.image('./isTranslated.png',
          x = 18, y = 15, w = 170, h = 70, type = 'PNG')
pdf.ln(90)
pdf.multi_cell(w=0, h=10, txt='isTranslated values in archive')
pdf.image('./submitterArchive.png',
          x = 18, y = 150, w = 170, h = 70, type = 'PNG')
pdf.ln(100)
pdf.multi_cell(w=0, h=10, txt='submitterArchive values in archive')

pdf.add_page()
pdf.ln(15)
pdf.image('./isPlagPrevent.png',
          x = 18, y = 15, w = 170, h = 70, type = 'PNG')
pdf.ln(90)
pdf.multi_cell(w=0, h=10, txt='isPlagPrevent values in archive')
pdf.image('./size.png', 
          x = 18, y = 130, w = 170, h = 100, type = 'PNG')
print("99%")
pdf.ln(130)
pdf.multi_cell(w=0, h=10, txt='size values in archive')
print("100%")
pdf.output(f'./37.pdf', 'F')