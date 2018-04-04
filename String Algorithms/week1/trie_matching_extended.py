# python3
import sys

NA = -1

class Node:
	def __init__ (self):
		self.next = [NA] * 4
		self.patternEnd = False

def solve (text, n, patterns):
	result = []
	trie = construct_trie(patterns)
	start = 0
	while text:
		temp = pre_fix_trie_matching(text,trie)
		if temp:
			result.append(start)
		text = text[1:]
		start += 1

	return result

def pre_fix_trie_matching(text,trie):
	ind = 0
	symbol = text[ind]
	v = trie[0]
	while True:
		# letter in trie, goto
		if symbol in v:
			#check next, if finish, then return true, else continur
			v = trie[v[symbol]]
			if '$' in v:
				return True
			ind += 1
			if ind == len(text):
				return False
			symbol = text[ind]
		else:
			return False

def construct_trie(patterns):
	# trie{0:{A:1}}
	trie = {}
	trie[0] = {}
	max_ind = 0

	for pattern in patterns:
		ind = 0
		for char in pattern:
			if char in trie[ind].keys():
				ind = trie[ind][char]
			else:
				max_ind += 1
				trie[ind][char] = max_ind + 1
				ind = trie[ind][char]
				trie[ind] = {}
		trie[ind]['$'] = '$'
	return trie

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
