# python3
import sys


def find_pattern(pattern, text):
  """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
  result = []
  if len(pattern) > len(text):
    return result
  string = pattern + '$' + text
  s = [0] * len(string)
  cur = 0
  for i in range(1, len(string)):
    while cur > 0 and string[i] != string[cur]:
      cur = s[cur - 1]
    if string[i] == string[cur]:
      cur += 1
    else:
      cur = 0
    s[i] = cur
    if s[i] == len(pattern):
      result.append(i - 2 * len(pattern))
  return result

if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))

