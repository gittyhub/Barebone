import check
import Modules_List
import sys
import re
import argparse

if __name__=='__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-r', '--write2file', help='write2file the scrapper')
  #parser.add_argument('-w', '--write_from_list_to_file', help='append to the file List2file') 
  parser.add_argument('-ca', '--find_ca_occurance', help='append to the file List2file') 
  parser.add_argument('-z', '--zipping_two_files', help='zipping List2File and FileOfAppendedList')
  args = parser.parse_args()
  x = 'http://sfbay.craigslist.org/search/apa' 
  #a = scrap_app_main_page =  (Modules_List.get_page(x))
  #d = gets_all_available_listing = Modules_List.get_All_AppLinks(scrap_app_main_page) 

 
  if args.write2file:
    scrap_app_main_page = (Modules_List.get_page(x))
    gets_all_posting = Modules_List.get_All_AppLinks(scrap_app_main_page) #list of http links 
    write_all_link_to_file = Modules_List.write_list_to_file(gets_all_posting) #List2File
    write_all_pages_to_file = Modules_List.write_from_list_to_file() #FileOfAppendedList
  elif args.find_ca_occurance:
    Modules_List.find_CA()
  elif args.zipping_two_files:
    Modules_List.listit()

'''  elif int(sys.argv[1]) == 2:
    print(d)
  elif int(sys.argv[1]) == 3:
    Modules_List.write_list_to_file(d)
  elif int(sys.argv[1]) == 0:
    Modules_List.find_CA(gets_all_available_listing)''' 
