```dataviewjs
let containsAspects = (item, valids) => {
	if(! item.aspects) return false
	return item.aspects.map(x => x.name).some(y => valids.includes(y))
}

let working_set = dv.pages('"Book Of Hours/things"')

dv.table(
	['Item', 'Aspects'],
	working_set
	.filter(x => x.aspects)
	.filter(x => containsAspects(x, ['ink']))
	.map(x => 
	[
		x.file.link,
		x.aspects.map(z => z.name + ' ' + z.amount),
	]
	) 
)
```
