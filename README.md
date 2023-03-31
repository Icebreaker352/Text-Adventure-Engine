# Text Adventure Engine
This is a very simple game engine designed specifically for text adventures. This file should help you learn how to use it in your own games.

# Writing a story
To write a story, you will need to look at the `story.json` file. This is where the majority of your story will be.
In this file, there are many different features that you can use. To prompt the user with text, use the `"text": "Hello World!"` key,and enter text in the empty quotes.
To give the user options, define a `"paths": { "a": {}, "b": {}, "c": {} }` key, and add as many options as you want. Inside of these options, you can put more text, and more options.
Another key is `"redirect": "path.goes.here"`. In this path, use '.' for delimeters, and do not the "paths" key of anything, it will be automatically included.
This key, true to it's name, will redirect the user to another part of the  story

# Example
```
{
  "text": "Yes or  no?",
  "paths": {
    "Yes": {
      "text": "Are you sure?",
      "paths": {
        "No": {
          "text": "You said no!"
        },
        "Yes": {
          "text": "You said yes!"
        },
        "Maybe": {
          "text": "Okay, maybe you'll decide later."
        }
      }
    },
    "No": {
      "redirect": "Yes.No"
    }
  }
}
```