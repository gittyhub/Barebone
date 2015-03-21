#--------------gets all links without query craigslist wanted or SF bay area in it
def get_AllLinks1(x,q): #x is the site, and q is the date
  index_site = [] #<< creates an empty list
  website = get_page(x) #<< opens http://sfbay.craigslist.com/acc
  a_href2 = re.findall('a href="/.*?</a>', website) #<< from the above, finds all a href links, and title of the links 
  for x in a_href2:
    if not ('query' in x or 'craigslist' in x or 'SF bay area' in x or 'wanted' in x):
      link = re.search('(?<=a href=").*?.html',x) #<< gets the linke of the job, without the a href's
      job =  'http://sfbay.craigslist.com'+link.group() #attachs the http start to the link completing the hyperlink 
      if q in get_page(job): #grabs all links with 5/15 in the page, but probably grabbing it from the title tag and if not in the body, it will get picked up but your prog wont find it if is only looking in the body, so you may need another function that looks for the price in the title with 5/15 so you dont get completly stuck causing exceptioin
        index_site.append(job)
      else:
        continue
    else:
      continue
  return index_site

