import argparse
import pdftotext
import pandas as pd

'''
    Works for only Tezpur University folks.
'''

parser = argparse.ArgumentParser()
parser.add_argument('-i','--infile',type=str,help='Input PDF file of result',default='Results_finalsem_spring_2019.pdf', required=True)
parser.add_argument('-r','--roll',type=str,help='Your roll number',default='not_supplied',required=True)
parser.add_argument('-c','--cgpa',type=str,help='Output file name for individual cgpa file',default='cgpa.csv')
parser.add_argument('-d','--deptcgpa',type=str,help='Output file name for department cgpa file',default='cgpa_dept.csv')
args = parser.parse_args()

with open(f'{args.infile}', "rb") as f:
    pdf = pdftotext.PDF(f)
def float_convertible(word):
    '''
        Function to return cgpa if exists or -1 if not
    '''
    try:
        x = float(word)
        return x
    except:
        return -1

cgpa_dict = {} #dictionary of roll number:cgpa

for page in pdf:
    #print(page)
    for string in page.split('\n'):
        string_list = string.split()
        if(len(string_list)>=4):
            res = float_convertible(string_list[-1])
            if(res!=-1):
                cgpa_dict[string_list[0]]=res

df = pd.DataFrame({'roll_no':list(cgpa_dict.keys())},columns=['roll_no'])
df['cgpa'] = df['roll_no'].map(cgpa_dict)
#aggegate by department
df['dept_code'] = df['roll_no'].apply(lambda x : x[:3])
df['start_year'] = df['roll_no'].apply(lambda x : x[3:5])
df.to_csv(f'{args.cgpa}',index=False)
dfdept = df.groupby(['dept_code','start_year']).agg({'cgpa':'mean'}).reset_index().round(2)
dfdept.to_csv(f'{args.deptcgpa}',index=False)

if(args.roll!='not_supplied'):
    dfyou = df[df['roll_no']==args.roll]
    if(len(dfyou)==0):
        print('Either you entered an invalid roll or you are withheld in the result pdf!')
    else:
        your_cgpa = dfyou['cgpa'].iloc[0]
        your_deptcode = dfyou['dept_code'].iloc[0]
        your_startyear = dfyou['start_year'].iloc[0]
        your_deptcgpa = dfdept[(dfdept['dept_code']==your_deptcode)&(dfdept['start_year']==your_startyear)]['cgpa'].iloc[0]
        print(f'Your cgpa is :',your_cgpa)
        print(f'Your department\'s average cgpa is :',your_deptcgpa)