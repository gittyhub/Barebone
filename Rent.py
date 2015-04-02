import check
import Modules_List
import sys
import re

if __name__=='__main__':
  x = 'http://sfbay.craigslist.org/search/apa' 
  #a = gets_app_main_search_page =  (Modules_List.get_page(x))
  #d = gets_all_available_listing = Modules_List.get_All_AppLinks(gets_app_main_search_page) 
 

 
  if int(sys.argv[1]) == 0:
    a = gets_app_main_search_page =  (Modules_List.get_page(x))
    d = gets_all_available_listing = Modules_List.get_All_AppLinks(gets_app_main_search_page) 
  elif int(sys.argv[1]) == 1:
    print(a);
  elif int(sys.argv[1]) == 2:
    print(d)
  elif int(sys.argv[1]) == 3:
    Modules_List.write_list_to_file(d)
  elif int(sys.argv[1]) == 0:
    Modules_List.find_CA(gets_all_available_listing) 
