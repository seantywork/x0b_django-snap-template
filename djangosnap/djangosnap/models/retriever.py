import pandas as pd
import re
from pathlib import Path
import os

def retriever(z,clf):
    BASE_DIR = Path(__file__).resolve().parent
    entrypath = os.path.join(BASE_DIR, 'entrydb.csv')
    textpath = os.path.join(BASE_DIR, 'textdb.csv')
    entrydb = pd.read_csv(entrypath)
    textdb = pd.read_csv(textpath)



    result = list()
    match_total_count = 0


    if clf == 1:
        for query in z:
            touched = 0
            for i in range(len(entrydb)):
                #check = re.search('\\b'+query+'\\b',entrydb.at[i,'ENTRY'],flags= re.I)
                if str(query).casefold() == str(entrydb.at[i,'ENTRY']).casefold():
                    if entrydb.at[i,'COUNT'] >= 1 :
                        idxs = str(entrydb.at[i,'INDEX']).split(',')
                        idxslist = [int(x) for x in idxs]
                        match_total_count += 1
                        touched = 1
                        for j in idxslist :
                            result.append([query,textdb.at[j,'USAGE'],entrydb.at[i,'COUNT']])
                    else :
                        touched = 1
                        result.append([query,'No Usage',0])

            if touched == 0:
                result.append([query,'No Entry',0])

            touched = 0



    elif clf == 2 :
        for query in z:
            touched = 0
            query_li = query.split()
            match = list()
            idxs = list()
            idxs_fin = list()
            idxs_tmp = list()
            check_len = len(query_li)
            check_inc = 0

            for q in query_li :
                for i in range(len(entrydb)):
                    #check = re.search('\\b'+q+'\\b',entrydb.at[i,'ENTRY'],flags= re.I)
                    if str(q).casefold() == str(entrydb.at[i,'ENTRY']).casefold() :
                        if entrydb.at[i,'COUNT'] >= 1 :
                            idxslist = str(entrydb.at[i,'INDEX']).split(',')
                            idxs.append([int(x) for x in idxslist])
                            match.append(1)


            if len(match) != check_len :
                result.append([query,'No Entry',0])
                continue

            for i in idxs :
                for j in i :
                    idxs_tmp.append(j)

            for i in range(len(idxs_tmp)) :
                for j in range(len(idxs_tmp)):
                    if idxs_tmp[i] == idxs_tmp[j] :
                        check_inc += 1
                if check_len == check_inc:
                    idxs_fin.append(idxs_tmp[i])
                check_inc = 0

            if len(idxs_fin) == 0:
                result.append([query,'No Entry',0])
                continue

            set_tmp = set(idxs_fin)
            idxs_fin = list(set_tmp)

            for i in idxs_fin :
                ascend_check = list()
                ascend_if = 1
                for q in query_li :
                    check_start = re.search('\\b'+q+'\\b',textdb.at[i,'USAGE'],flags=re.I)
                    ascend_check.append(check_start.start())
                for j in range(len(ascend_check)-1):
                    if ascend_check[j] > ascend_check[j+1]:
                        ascend_if = 0
                if ascend_if == 1:
                    match_total_count += 1
                    touched = 1
                    result.append([query,textdb.at[i,'USAGE'],len(idxs_fin)])

            if touched == 0:
                result.append([query,'No Entry',0])

            touched = 0

    elif clf == '2022wlswkaehtjrhks0514P@' :
        for i in range(len(entrydb)):
            if entrydb.at[i,'COUNT'] >= 1:
                idxs = str(entrydb.at[i,'INDEX']).split(',')
                idxslist = [int(x) for x in idxs]
                for j in idxslist :
                    result.append([entrydb.at[i,'ENTRY'],textdb.at[j,'USAGE'],entrydb.at[i,'COUNT']])
            else :
                result.append([entrydb.at[i,'ENTRY'],'No Usage',0])

    if match_total_count != 0 :
        for i in range(len(result)):
            x = result[i][0].split()
            for j in range(len(x)):
                start = 0
                end = 0
                check = re.search('\\b'+x[j]+'\\b',result[i][1],flags=re.I)
                start = check.start()
                end = check.end()
                str_tmp = result[i][1][:start] + '^' + result[i][1][start:end] + '^' + result[i][1][end:]+'\n'
                result[i][1] = str_tmp


    result_df = pd.DataFrame(result,columns=['ENTRY','USAGE','COUNT'])

    return result_df