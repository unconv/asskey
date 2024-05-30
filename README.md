# ASCII Art Generator (Asskey)

Convert images into ASCII art or create ASCII art from scratch with DALL-e 3

## Quick start

```sh
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ ./image_to_ascii.py <input_image> <output_file>
$ ./prompt_to_ascii.py <output_file> <prompt>
```

To use `prompt_to_ascii.py` you need to add your OpenAI API key into a `.env` file (see `.env.sample`)

## Example 1

```sh
$ ./image_to_ascii.py images/dog.webp dog.jpg
```

<img src="examples/dog.jpg">

## Example 2

```sh
$ ./prompt_to_ascii.py girl.jpg "a cute anime girl"
```

<img src="examples/girl.jpg">
