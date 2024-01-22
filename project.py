import pandas as pd
import re

def main():
    file_loc = input('Files location : ').replace('\/','\\')
    file_loc = file_loc.replace('"','')
    print(file_loc)
    df = import_data(file_loc)
    hashtag_ls,content_without_hashtags = split_out_hashtags(df)
    username_ls = username_edit(df)
    handle_missing_and_none(df)
    new_df = intregate_df(df,hashtag_ls,content_without_hashtags,username_ls)
    export_as_csv(df,new_df)
    
def import_data(data_loc):
    df = pd.read_csv(data_loc,encoding='utf-8')
    return df

def split_out_hashtags(df):
    hashtags_ls = []
    content_without_hashtags_ls = []
    content = df.iloc[:,2]
    for i in range(len(content)):
        try:
            hastag_i = re.findall("#.*", content[i])
            content_none = re.search('#.+',content[i])
            loc_start = content_none.span()[0]
            content_none_ht = content[i][:loc_start]
        except:
            hastag_i = ['None Value']
            content_none_ht = 'Nothing'
        content_without_hashtags_ls.append(content_none_ht)
        hashtags_ls.append(', '.join(hastag_i))
    return hashtags_ls, content_without_hashtags_ls

def username_edit(df):
    usernames_col = df.iloc[:,1]
    username_ls = []
    for i in range(len(usernames_col)):
        try:
            text = usernames_col[i].replace('\n', '')
            matchs = re.search('^.+·',text)
            if matchs:
                match = re.match(r'^(.+)@([^·]+)·(.+)$', text)
                Username = match.group(1)
                User_id = '@'+match.group(2)
                Text_timed = match.group(3)
            else:
                Username = 'Unknown'
                User_id = '@Unknown'
                Text_timed = 'Unknown'
            username_ls.append([Username,User_id,Text_timed])
        except:
            username_ls.append(['Unknown','@Unknown','Unknown'])
    return username_ls
    
def handle_missing_and_none(df):
    numberic_col = df.iloc[:,3:6]
    for head in numberic_col.columns:
        for i in range(len(numberic_col[head])):
            try:
                if 'k' or 'K' in numberic_col[head][i]:
                    numberic_col[head][i] = int(float(numberic_col[head][i][:-1])*1000)
                else:
                    numberic_col[head][i] = int(numberic_col[head][i])
            except:
                numberic_col[head][i] = 0

def intregate_df(df,hashtag_ls,content_without_hashtags,username_ls):
    data_dict = {
        'Content-without-hashtags' : content_without_hashtags,
        'hashtags' : hashtag_ls,
        'Username' : [i[0] for i in username_ls],
        'UserID' : [i[1] for i in username_ls],
        'Tweet_Date' : [i[2] for i in username_ls]
    }
    dict_df = pd.DataFrame.from_dict(data_dict)
    new_df = pd.concat([df.iloc[:,[0,2]],dict_df],axis=1)
    return new_df

def export_as_csv(df,new_df):
    print('Original Dataset     :',df.columns)
    print('Preprocess Dataset   :',new_df.columns)
    new_df.to_csv('new_dataset_preprocessed.csv',encoding='utf-8-sig',index=False)
    print('CSV export successfully')

if __name__ == "__main__":
    main()