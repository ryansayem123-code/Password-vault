import csv as csv

team = [["Name","Age","Role","Salary","Holiday_Hours_Remaining"],
        ["Ryan",19,"manager","$120,000", 25],
        ["Adam",29,"CEO","$200,000",25],
        ["Tom",25,"Vice-President","$156,000",25],
        ["Jack",30,"Eningeer","$80,000",25],
        ["Murphy",34,"Senior Engineer","$90,000",25]
]

file_path = "/Users/ryansayem/Desktop/team.csv"
try:
 with open(file_path,"w") as file:
    writer = csv.writer(file)
    for row in team:
        writer.writerow(row)
    print(f"Csv file {file_path} was successfully created".upper())

except FileNotFoundError:
 print("File was not found".upper())
