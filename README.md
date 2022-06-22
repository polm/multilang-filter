# Multilang Preprocessor

This is a simple script for preprocessing multilingual Markdown documents or Jupyter notebooks. This was developed for the book [Introduction to Japanese Natural Language Processing](https://www.japanesenlp.com/) (JANLP). 

The goal of the formatting used here is to compose a document in multiple languages but in a single file, without breaking existing formatting or tools, or adding excessive overhead for the authors.  

## Usage

```
python multilang.py <lang> <file.md>
```

`lang` should be a language code specified at the top of the script. `file.md` is the file to process. The result of filtering the input will be printed to stdout.

To test it, you can use it with the `demo.md` file in this repo. Try these commands:

```
python multilang.py en demo.md
python multilang.py ja demo.md
```

## Formatting Notes

The basic principle is that lines marked as belonging to a language will only be output when that language is designated. Unmarked lines are always passed through, and sigils are always stripped from output.

There are two kinds of formatting:

1. single line declarations
2. block declarations

Languages to be used should be declared at the top of the file. By default `en`, `ja`, and `xx` are declared. These codes are only used internally, and don't have to correspond to any standard.

### Single Line Declarations

Single line declarations just use a "sigil" for a language anywhere on a line. A sigil is a colon followed by a language code, like `:en`. 

```
# HTML

The title of this section is language-neutral, so it's unmarked. But this line is in English. :en
```

### Block Declarations

Sometimes when you have a lot of short lines, or preformatted text, it may be easier to declare a block than to mark every line with a sigil. A block starts with a sigil on a line on its own and ends with a line that is just `:end`. 

```
Sometimes you need to buy groceries. (This line is not in a block declaration.) :en

:en
- this is inside a block declaration
- carrots
- eggs
- milk
:end
```

## License

This code is offered under the terms of the MIT or WTFPL license, as you prefer, and may be used freely. Please copy it far and wide.
