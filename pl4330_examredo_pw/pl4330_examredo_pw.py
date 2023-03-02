

#programming language exam 1 redo project work

import re

#lets you know if a string is an email address or not 
def is_valid_email(email):
	emailpattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9]+\.[A-Za-z]$'
	if not re.match(emailpattern, email):
		return False
	
	if ".." in email.split("@")[0]:
	    return False
	  
	local_part = email.split("@")[0]
	if local_part.startswith(".") or local_part.endswith:
		return False 
	local_part_pattern = r'^[A-Za-z0-9#%!$‘&+*\-/=?^_`{|}~]'
	if not re.match(local_part_pattern):
		return False
	domain_pattern = r'^[A-Za-z0-9-]+(\.[A-Za-z0-9-])*$'
	domain_name = email.split("@")[1]
	if not re.match(domain_pattern, domain_name):
	    return False
	return True


#9 lets you know if a string is an floating point literal or not
def is_valid_flotingP(str):
	floatingPointPattern = r'^[+-]?(\d+\.\d*)|\.\d+)([eE]\d+)?$'
	return bool(re.match(floatingPointPattern, str))


#10 lets you know if a string is an integer literal or not.
def is_valid_integerConstant(str):
	integerconstantpattern = r'^[+-]?\d+$'
	return bool(re.match(integerconstantpattern, str))

#14 determine if a string matches even number of a’s and an odd number of b’s followed by any number of c’s or d’s OR a pattern of even occurrences of the string ‘cbad
def is_valid_EaOb(name):
    patternEaOb = '(aa|bb|aabb |abab| abba | baba |baab |bbaa)b| b(aa|bb|aabb |abab| abba | baba |baab |bbaa)| (aa|bb|aabb |abab| abba | baba |baab |bbaa)b(aa|bb|aabb |abab| abba | baba |baab |bbaa) ie evenAB = (aa|bb|aabb |abab| abba | baba |baab |bbaa)* b(evenAB) | (evenAB)b | evenAB (b) evenAB'
    return re.match(patternEaOb, name) is not None

#a regular expression to see if a string could be a variable, class, or method
def is_valid_name(name):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return re.match(pattern, name) is not None

