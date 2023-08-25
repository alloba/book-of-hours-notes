# Overview
This offers a high level page for various things. 
TBD, honestly. 


## Books and Their Study
```dataviewjs 
let books = dv.pages('"books"')

let titlecase = (x) => {
	return x.replace( /\w\S*/g,
	    (txt) => txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase()
  );
}

dv.table(
	["File", "Study Aspects"], 
	books
	.map(b => [
		b.file.link,
		b.aspects
		  .filter(x => x.name.startsWith('mystery'))
		  .map(x => titlecase(x.name.replace('mystery:', '')) + ' ' + x.amount)
		  
	])
	.sort(x => x[1])
)
```


## Parts of the Soul

```dataview
table aspects, tags
from "parts-of-the-soul"

```