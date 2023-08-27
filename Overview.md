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

## Consumables
```dataviewjs
let items = dv.pages('"things"')
let valids = [
	'grail', 'winter', 'lantern', 'nectar', 'heart', 
	'sky', 'forge', 'moth', 'moon', 'scale', 'edge', 'rose',
	
]

let working_set = items
	.filter(x => x.aspects)
	.filter(x => x.aspects
				.map(y => y.name)
				.some(z => ['beverage', 'sustenance'].includes(z)) 
	)
let containsAspects = (item, valids) => {
	if(! item.aspects) return false
	return item.aspects.map(x => x.name).some(y => valids.includes(y))
}

dv.table(
	['Item', 'Aspects'],
	working_set
	.filter(x => containsAspects(x, valids))
	.map(x => 
	[
		x.file.link,
		x.aspects
			.filter(z => valids.includes(z.name))
			.map(z => z.name + ' ' + z.amount)
			.sort()
	]
	) 
)
```

## Searching Things
```dataviewjs
let containsAspects = (item, valids) => {
	if(! item.aspects) return false
	return item.aspects.map(x => x.name).some(y => valids.includes(y))
}

let working_setz = dv.pages('"things"')

dv.table(
	['Item', 'Aspects'],
	working_setz
	.filter(x => containsAspects(x, ['tool', 'ink']))
	.map(x => 
	[
		x.file.link,
		x.aspects.filter(z => z.name == 'heart').map(z => z.name + ' ' + z.amount)
	]
	) 
)
```
