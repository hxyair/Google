#Regular expression operations

import re
def check_aei (text):
	#. ^ $ * + ? { } [ ] \ | ( )
  result = re.search(r"a.a", text)
  re.search(r"[a-z]way", "hello always")
  re.search(r"[^a-z]way", "hello always")#[^5] will match any character except '5',
  re.search(r"cat|dog", "hello always")
  re.findall(r"cat|dog", "I like both cats and dogs.")
  re.search(r"Py.*n", "Python Programming always")#ab* will match ‘a’, ‘ab’, or ‘a’ followed by any number of ‘b’s.
  re.search(r"Py[a-z]*n", "Python Programming always")
  re.search(r"m+a+", "Python Programming always")#ab+ will match ‘a’ followed by any non-zero number of ‘b’s; it will not match just ‘a’.
  re.search(r"p?each","I like peaches")#ab? will match either ‘a’ or ‘ab’.
  re.search(r"\.com","I came for peaches.com")
  re.search(r"^A.*a$","Azerbaijan")
  #By adding a dollar sign to our pattern, we've made it clear that we only want to match lines that begin and end with the letter a.
  return result != None

  #a{6} will match exactly six 'a' characters, but not five.


print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True
'''
grep l.rts spider.txt
grep ^fruit spider.txt
grep cat$ spider.txt
#Match the start and the end of a line (the circumflex and the dollar sign specifically match the start and end of a line.)
'''

import re
def repeating_letter_a(text):
  result = re.search(r"[aA].*a", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True


import re
def check_web_address(text):
  pattern = r"^[A-Za-z._-][^/@]*$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True

import re
def check_time(text):
  pattern =r"^(?:1[0-2]|0?[1-9]):(?:[0-5]?[0-9])(?:\s?[AP]M|[ap]m)?$"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False


import re
def check_zip_code (text):
  result = re.search(r"(?!\A)\b\d{5}(?:-\d{4})?\b", text)
  #Matches if ... doesn’t match next. This is a negative lookahead assertion. For example, Isaac (?!Asimov) will match 'Isaac ' only if it’s not followed by 'Asimov'.
  #\A Matches only at the start of the string.
  #\b Matches the empty string, but only at the beginning or end of a word. 
  #\d Matches any decimal digit; this is equivalent to [0-9].
  #This means that r'\bfoo\b' matches 'foo', 'foo.', '(foo)', 'bar foo baz' but not 'foobar' or 'foo3'.
  #For example, the expression (?:a{6})* matches any multiple of six 'a' characters.
  #ab? will match either ‘a’ or ‘ab’.
  # (?!...) Matches if ... doesn’t match next. This is a negative lookahead assertion. For example, Isaac (?!Asimov) will match 'Isaac ' only if it’s not followed by 'Asimov'.
  return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False


import re
def contains_acronym(text):
  pattern = r"\([A-Za-z0-9]{2,}\)"
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True

print(ruslt.groups())
"{} {}".format(result[2],result[1])

import re
def rearrange_name(name):
  result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)



import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]\: ([A-Z]*)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1],result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)




import re
def transform_record(record):
  new_record = re.sub(r',(?=\d)', r',+1-', record)#(?=\d) is a positive lookahead it means match , that are followed by a digit.
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer


import re
def multi_vowel_words(text):
  pattern = r"\b\w*[aeiou]{3,}\w*\b"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []



import re
def convert_phone_number(phone):
  result = re.sub(r'[ ](?<!\S)(\d{3})-', r' (\1) ', phone)
  #(?<!\S) - a left-hand whitespace boundary
  #(\d{3}) - Capturing group #1: three digits
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300





#!/usr/bin/env python3

import re
import csv


def contains_domain(address, domain):
  """Returns True if the email address contains the given,domain,in the domain position, false if not."""
  domain = r'[\w\.-]+@'+domain+'$'
  if re.match(domain,address):
    return True
  return False


def replace_domain(address, old_domain, new_domain):
  """Replaces the old domain with the new domain in the received address."""
  old_domain_pattern = r'' + old_domain + '$'
  address = re.sub(old_domain_pattern, new_domain, address)
  return address

def main():
  """Processes the list of emails, replacing any instances of the old domain with the new domain."""
  old_domain, new_domain = 'abc.edu', 'xyz.edu'
  csv_file_location = '<csv_file_location>'
  report_file = '<path_to_home_directory>' + '/updated_user_emails.csv'
  user_email_list = []
  old_domain_email_list = []
  new_domain_email_list = []

  with open(csv_file_location, 'r') as f:
    user_data_list = list(csv.reader(f))
    user_email_list = [data[1].strip() for data in user_data_list[1:]]

    for email_address in user_email_list:
      if contains_domain(email_address, old_domain):
        old_domain_email_list.append(email_address)
        replaced_email = replace_domain(email_address,old_domain,new_domain)
        new_domain_email_list.append(replaced_email)

    email_key = ' ' + 'Email Address'
    email_index = user_data_list[0].index(email_key)

    for user in user_data_list[1:]:
      for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
        if user[email_index] == ' ' + old_domain:
          user[email_index] = ' ' + new_domain
  f.close()

  with open(report_file, 'w+') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(user_data_list)
    output_file.close()

main()