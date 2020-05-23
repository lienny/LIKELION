import requests 
from bs4 import BeautifulSoup 
from naverbook_note import extract_info
import csv

file = open("naverbook.csv", mode="w", newline="")
writer = csv.writer(file)
writer.writerow(["title", "img_src", "link", "author", "publisher"])
final_result = []
for i in range(1,8): 
    print(f'{i+1}page')
    naverbook_html = request.get(f"https://book.naver.com/category/index.nhn?cate_code=100&tab=new_book&list_type=list&sort_type=publishday&page={i+1}")
    naverbook_soup = BeautifulSoup(naverbook_html.text, "html.parser")
    naverbook_list_box = naverbook_soup.find("ol", {"class" : "basic"})
    naverbook_list = naverbook_list_box.find_all("li")
    result = extract_info(naverbook_list)
    final_result += final_result +  result
for note in final_result: 
    row=[]
    row.append(note['title'])
    row.append(note['img_src'])
    row.append(note['link'])
    row.append(note['author'])
    row.append(note['publisher'])
    writer.writerow(row)