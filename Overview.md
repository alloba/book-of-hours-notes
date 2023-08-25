# Overview
This offers a high level page for various things. 
TBD, honestly. 


## Books and Their Study
```dataviewjs 
let books = dv.pages('"books"')
dv.table(
	["File", "Study Aspects"], 
	books.map(x => 
	[
		x.file.link,
		x.aspects
			.filter((k, v) => typeof(k) == 'object' )
			.filter((k,v) => 
				Object.keys(k).some(l => l.startsWith('mystery'))
			)
			.sort()
	]
	)
)
```


## Parts of the Soul

```dataview
table aspects, tags
from "parts-of-the-soul"

```