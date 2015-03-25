import check
import Modules_List
import sys
import re

if __name__=='__main__':
  x = 'http://sfbay.craigslist.org/search/apa' 
  gets_app_search_page =  (Modules_List.get_page(x))
  gets_all_available_listing = Modules_List.get_All_AppLinks(gets_app_search_page) 
  
  if int(sys.argv[1]) == 1:
    print(gets_app_search_page);
  elif int(sys.argv[1]) == 2:
    d = Modules_List.get_All_AppLinks(gets_app_search_page)
    print(gets_all_available_listing)
  elif int(sys.argv[1]) == 3:
    d = Modules_List.get_All_AppLinks(gets_app_search_page)
    Modules_List.write_list_to_file(d)
