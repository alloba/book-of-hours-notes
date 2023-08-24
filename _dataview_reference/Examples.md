
## External Docs
- [Implicit Metadata on Pages](https://blacksmithgu.github.io/obsidian-dataview/annotation/metadata-pages/)
- [Metadata on Tasks and Lists](https://blacksmithgu.github.io/obsidian-dataview/annotation/metadata-tasks/)
- [Query Language Reference](https://blacksmithgu.github.io/obsidian-dataview/queries/structure/)
## Data Indexing 
You can make use of frontmatter for Dataview. All data within is available to work with. There are no restrictions on what you can put here, so consistency is something you need to worry about on your own. 

```yaml 
---
author: "Bob Dob"
published: 2001
tags: [book, words, fake, etc.]
---
```


You can also inline tags. Same rules apply, but now its just in any old place within the file: 
```markdown 

yadda yadda a normal file. 

## A Heading About a Book
From [author:: Bob Dob], written in (published:: 2001)

yadda yadda normal notes. 
```

## Data Querying 
Data is viewed through queries. 

Three ways to write them: 
- Dataview Query Language
- Inline Statement
- Javascript Query

### Dataview Query Language 

Basically a code block that you mark for Dataview to recognize and operate on. 

```text 
List all files in your vault: 
	```dataview 
	LIST 
	```
```

```text 
List all files that have the poem tag and an author field with value Bob Dob
	```dataview 
	LIST 
	FROM #poems
	WHERE author = "Bob Dob"
	```
```

```text 
	Create a table from all files with a poem tag
	```dataview
	TABLE author, published, file.inlinks as "Mentions"
	FROM #poems
	```
```