import pandas as pd
df = pd.read_csv('D:/projects/ds_salary_proj/glassdoor_jobs.csv')

# salary parsing


df['hourly'] = df['Salary Estimate'].apply(lambda x : 1 if 'per hour' in x.lower() else 0)
df['Employer_provided'] = df['Salary Estimate'].apply(lambda x : 1 if 'employer provided salary:' in x.lower() else 0)


df = df [df['Salary Estimate']!='-1']

salary = df['Salary Estimate'].apply(lambda x : x.split('(')[0])
remove_kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

remove_hr = remove_kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary']= remove_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary']= remove_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary']= (df.min_salary+df.max_salary)/2

# company name text only
df['company_text'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis=1)
# state field

#df['state']= df.apply(lambda x: x['Location'].split(',')[1])

df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df.job_state.value_counts()

df['same_state']= df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis=1)

# age of company
df['Company_age']= df.Founded.apply(lambda x: x if x<1 else 2021-x)

# parsing job description
df['Job Description'][0]

#python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)

#r studio
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)

df.R_yn.value_counts()

#spark
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()

#aws
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws.value_counts()

#excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel.value_counts()

#df.columns

df_updated = df.drop(['Unnamed: 0'], axis=1)

df_updated.to_csv('Salary_data_cleaned.csv', index=False)
