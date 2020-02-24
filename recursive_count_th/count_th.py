'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word, count=0):
	word_list = list(word)
	# base case, stops recursion when true
	if len(word_list) <= 1:
		return count

	else:
		# check for "th"
		if word_list[0] == "t" and word_list[1] == "h":
			# if yes, add to the count and remove both from word_list array
			count += 1
			word_list.pop(0)
			word_list.pop(0)
			# call this function again with the updated word_list and count
			return count_th(word_list, count)
		else:
			# if no, remove the first item in the word_list array
			word_list.pop(0)
			# call this function again with the updated word_list and count
			return count_th(word_list, count)

print(count_th("monththt"))
	# count = word.count("th")
	# return count