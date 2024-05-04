# Books and Their Study
```dataviewjs 
let books = dv.pages('"Book Of Hours/books"')

let titlecase = (x) => {
	return x.replace( /\w\S*/g,
	    (txt) => txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase()
  );
}

dv.table(
	["File", "Study Aspects", "Studied"], 
	books
	.map(b => [
		b.file.link,
		b.aspects
		  .filter(x => x.name.startsWith('mystery'))
		  .map(x => titlecase(x.name.replace('mystery:', '')) + ' ' + x.amount),
		b.tags.includes('studied') ? 'Yes' : ''
	])
	.sort(x => x[1])
)
```
