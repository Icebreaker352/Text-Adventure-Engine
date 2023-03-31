import json, os

# More efficient way to navigate the story
def search(path, json):
  keys = path.split('.')
  story = json
  i = 0
  for key in keys:
      story = story['paths']
      story = story[key]
  return story

# Main Function for moving through the story
def prompt(const, story):
  os.system('clear')
  # Register all arguments, if found
  try: txt = story['text']
  except: txt = ""
  try: paths = story['paths']
  except: paths = {}
  try: redirect = story['redirect']
  except: redirect = None
  # Redirect the user to another part of the story, if needed
  if redirect:
    path = search(redirect, const)
    prompt(const, path)
  # Prompt user with a message
  print(txt)
  # Print out all paths
  i = 0
  for path in paths:
    print(f'({i}) {path}')
    i += 1
  inp = input()
  # Check which option the user picks, and continue the story
  i = 0
  for path in paths:
    if int(inp) == i:
      prompt(const, paths[path])
      break
    i += 1

# Initiate the story
story = json.load(open('story.json'))
prompt(story, story)
