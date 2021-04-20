## Sub-functions for Whitespace

def Trim_(df):
    for i in df.columns:
        if df[i].dtype == 'object':
            df[i] = df[i].str.strip()
        else:
            pass
    return df
def ReplaceLineBreakWithSpace_(df):
    for i in df.columns:
        if df[i].dtype == 'object':
            df[i] = df[i].str.replace('\n',' ')
        else:
            pass
    return df
def MultipleSpacesToSingle_(df):
    for i in df.columns:
        if df[i].dtype == 'object':
            df[i] = df[i].str.replace('\s+',' ')
        else:
            pass
    return df
def MultipleBlankLinesToSingle_(df):
    for i in df.columns:
        if df[i].dtype == 'object':
            df[i] = df[i].str.replace('\n+','\n')
        else:
            pass
    return df

## Sub-Functions for Characters
def RemovePunctuations_(df):
    for i in df.columns:
        if df[i].dtype == 'object':
            df[i] = df[i].apply(remove_punctuation)
        else:
            pass
    return df

def RemoveEmojis_(df):
    import re
    def deEmojify(text):
        regrex_pattern = re.compile(pattern = "["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags = re.UNICODE)
        return regrex_pattern.sub(r'',text)
    for i in df.columns:
        if df[i].dtype == 'object':
            df[i] = df[i].apply(deEmojify)
        else:
            pass
    return df
def RemoveLetterAccent_(df):
    import unidecode
    def rla(text):
        return unidecode.unidecode(text)
    for i in df.columns:
        if df[i].dtype == 'object':
            df[i] = df[i].apply(rla)
        else:
            pass
    return df
def NonAlphaNumericCharacter_(df):
    def nanc(text):
        return re.sub(r'\W+','',text)
    for i in df.columns:
        if df[i].dtype == 'object':
            df[i] = df[i].apply(nanc)
        else:
            pass
    return df
def NonAscciCharacter_(df):
    def nac(text):
        return re.sub(r'[^\x00-\x7F]','',text)
    for i in df.columns:
        if df[i].dtype == 'object':
            df[i] = df[i].apply(nac)
        else:
            pass
    return df
def NormalizeUnicodeLetters_(df):  # not sure about this block
    def nul(text):
        return unicodedata.normalize(u'NFKD', text).encode('ascii', 'ignore').decode('utf8')
    for i in df.columns:
        if df[i].dtype == 'object':
            df[i] = df[i].apply(nul)
        else:
            pass
    return df


#------------------------  Main Functions ---------------

# Main Function for Whitespace
def Whitespace(df, Trim=False, ReplaceLineBreakWithSpace=False, MultipleSpacesToSingle=False, MultipleBlankLinesToSingle=False):
    if Trim == True:
        new_df = Trim_(df)
    elif ReplaceLineBreakWithSpace == True:
        new_df = ReplaceLineBreakWithSpace_(df)
    elif MultipleSpacesToSingle == True:
        new_df = MultipleSpacesToSingle_(df)
    elif MultipleBlankLinesToSingle == True:
        new_df = MultipleBlankLinesToSingle_(df)
        
    return new_df
        
# Main Function for Characters

def Characters(df, RemovePunctuations=False, RemoveEmojis=False, RemoveLetterAccent=False,
               NonAlphaNumericCharacter=False, NonAscciCharacter=False, NormalizeUnicodeLetters=False):
    if RemovePunctuations == True:
        new_df = RemovePunctuations_(df)
    elif RemoveEmojis == True:
        new_df = RemoveEmojis_(df)
    elif RemoveLetterAccent == True:
        new_df = RemoveLetterAccent_(df)
    elif NonAlphaNumericCharacter == True:
        new_df = NonAlphaNumericCharacter_(df)
    elif NonAscciCharacter == True:
        new_df = NonAscciCharacter_(df)
    elif NormalizeUnicodeLetters == True:
        new_df = NormalizeUnicodeLetters_(df)
        
    return new_df



# dataframe to test

import pandas as pd
df = pd.DataFrame({'Name' : ['       Sun   \t     ny?          ','&amp Bun<head>  ny\U0001f602!','Gin<html>ny ','https://url.com/bla1/blah1/ B\n\n\ninny ','hello    python \n\n hello world','Málaga网 http://url.com/bla1/blah1/ '], 
                    'Age' : [23,44,23,54,22,11],
                    'Blood Group' : [' A+',' B+','O+','O-',' A-','B-'],
                   'Gender' : [' M class="hello"',' M','F','F','F',' F']})


