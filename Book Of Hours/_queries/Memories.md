# Memories
```dataviewjs
let containsAspects = (item, valids) => {
	if(! item.aspects) return false
	return item.aspects.map(x => x.name).some(y => valids.includes(y))
}

let working_set = dv.pages('"Book Of Hours/memories-and-lessons"')


dv.table(
	['Item', 'Aspects'],
	working_set
	.filter(x => x.aspects)
	.filter(x => !containsAspects(x, ['lesson']))
	.map(x => 
	[
		x.file.link,
		x.aspects.map(z => z.name + ' ' + z.amount),
	]
	) 
)
```
