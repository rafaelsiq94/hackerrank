def timeConversion(s):
  if "PM" in s:
    s = s.replace("PM", "")
    s = s.split(":")
    if s[0] == "12":
      pass
    else:
      s[0] = str(int(s[0]) + 12)
    s = ':'.join(s)
  else:
    s = s.replace("AM", "")
    s = s.split(":")
    if s[0] == "12":
      s[0] = "00"
    s = ':'.join(s)
  return s

if __name__ == '__main__':

  result = timeConversion("07:05:45PM")

  print(result)
