# magic
Minimal static site generator

## setting up

In your root folder, create the following tree

```
- assets
- content
- magic
- public
- templates
```

Each page in content must start with a header like so

```
---
title:  
---

# rest of content

lorem ipsum
```

```magic``` will parse these files and return a page dictionary with the headers and a content value.

```templates``` can then use these dictionaries like so

```
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>{page[title]}</title>
</head>
<body>
  {page[content]}
</body>
</html>
```

The entire assets folder will be copied to public, so you can reference stylesheets that way
